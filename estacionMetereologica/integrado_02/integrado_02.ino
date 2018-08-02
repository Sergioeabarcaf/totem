/*
 * Sensores_lluvia_viento.ino
 * Created: 6/13/2017 10:30:59 AM
 * Author: protein-2017
 * URL: https://learn.sparkfun.com/tutorials/weather-shield-hookup-guide
 * URL github: https://github.com/sparkfun/Weather_Shield/blob/master/firmware/Weather_Shield_Weather_Station/Weather_Shield_Weather_Station.ino
 * Version: 2.0 (solo info sin procesar)
 * Circuito: Solo se necesita conectar una resistencia de 10K @ 5V en la salida de la VELETA (pin4 de roseta) y un condensador (1e-6 o 100e-9F) a TIERRA (véase datasheet).
 *				Toda la otra parte de la circuitería, es conexión a los puertos digitales/analogos de acuerdo a lo indicado en el programa.
 */ 


//Hardware pin definitions
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
// digital I/O pins
const byte WSPEED = 3;
const byte RAIN = 2;

// analog I/O pins
const byte WDIR_ADC = A0;
const byte LUMENS_ADC = A2;
const byte UV_ADC = A1;
const byte REF_3V3_UV = A3; //3.3V power on the Arduino board
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

//Global Variables
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
long lastSecond; //The millis counter to see when a second rolls by
byte seconds; //When it hits 60, increase the current minute
byte seconds_2m; //Keeps track of the "wind speed/dir avg" over last 2 minutes array of data
byte minutes; //Keeps track of where we are in various arrays of data
byte minutes_10m; //Keeps track of where we are in wind gust/dir over last 10 minutes array of data

long			lastWindCheck = 0;
volatile long	lastWindIRQ = 0;
volatile byte	windClicks = 0;

byte windspdavg[120]; //120 bytes to keep track of 2 minute average

#define WIND_DIR_AVG_SIZE 120
int		winddiravg[WIND_DIR_AVG_SIZE];		//120 ints to keep track of 2 minute average
float	windgust_10m[10];					//10 floats to keep track of 10 minute max
int		windgustdirection_10m[10];			//10 ints to keep track of 10 minute max
volatile float rainHour[60];			//60 floating numbers to keep track of 60 minutes of rain

//These are all the weather values that underground expects:
int		winddir = 0;			// [0-360 instantaneous wind direction]
char*	_nameWDir = "";
float	windspeed_kph = 0;	// [[kph instantaneous wind speed]

float	windgust_kph = 0;		// [[kph current wind gust]
int		windgustdir = 0;		// [0-360 using software specific time period]

float	windspd_kph_avg2m = 0;	//[kph 2 min average wind speed on kph]

int		winddir_avg2m = 0;		// [0-360 2 minute average wind direction]
float	windgust_kph_10m = 0;		//[kph past 10min wind gust mph]

int		windgustdir_10m = 0;	// [0-360 past 10 minutes wind gust direction]

float	rainin = 0;			// [rain inches over the past hour)] -- the accumulated rainfall in the past 60 min

volatile float dailyrainin = 0; // [rain inches so far today in local time]

// volatiles are subject to modification by IRQs
volatile unsigned long raintime, rainlast, raininterval, rain;

char* nameDirWind[]	={	"N","NNE","NE","ENE",
						"E","ESE","SE","SSE",
						"S","SSO","SO","OSO",
						"O","ONO","NO","NNO"	};	// 16 elementos

int numDirWind[]	={	0,23,45,68,
						90,113,135,158,
						180,203,225,248,
						270,293,315,338			}; // 16 elementos

//Variables para UV / Lumens
boolean	flag_consulta=false;
int		lect, sensorUV;
float	conv, lux, Vsig;
long	sum;

//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

//Interrupt routines (these are called by the hardware interrupts, not by the main code)
//-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


void rainIRQ()		//VMH: Se modifica los valores para kilometros por hora (kph)
// Count rain gauge bucket tips as they occur
// Activated by the magnet and reed switch in the rain gauge, attached to input D2
{
    raintime = millis();				// grab current time
    raininterval = raintime - rainlast; // calculate interval between this and last event

    if (raininterval > 10)				// ignore switch-bounce glitches less than 10mS after initial edge
    {
        dailyrainin += 0.2794;			//Each dump is 0.2794mm of water	(dump: volcado)
		rainHour[minutes] += 0.2794;	//Increase this minute's amount of rain rainHour[0] +0.2794
        rainlast = raintime;			// set up for next event
    }
}


void wspeedIRQ()		//VMH: Sin modificaciones IRQ
// Activated by the magnet in the anemometer (2 ticks per rotation), attached to input D3
{
    if (millis() - lastWindIRQ > 10) // Ignore switch-bounce glitches less than 10ms (142MPH max reading) after the reed switch closes
    {
        lastWindIRQ = millis(); //Grab the current time
        windClicks++; //There is 1.492MPH for each click per second.
    }
}


void setup()
{
    Serial.begin(115200);
    pinMode(WSPEED, INPUT_PULLUP);				// input from wind meters windspeed sensor
    pinMode(RAIN, INPUT_PULLUP);				// input from wind meters rain gauge sensor
    seconds = 0;
    lastSecond = millis();
    // attach external interrupt pins to IRQ functions
    attachInterrupt(0, rainIRQ, FALLING);
    attachInterrupt(1, wspeedIRQ, FALLING);
    interrupts();								//turn on interrupts
}




//Calculates each of the variables that underground is expecting
// Esta seccion de funcion no se adultera, porque corresponde a la matematica aplicada a los valores que
// se capturan.
void calcWeather()
{
	//Calc winddir
	winddir = numDirWind[get_wind_direction()];	//get wind entrega el index para obtener el grado de la direccion
	//si se desea el cardinal de la direccion se utilizaría la funcion
	//nameDirWind[]
	//Calculo para windspeed en kph para avg2m
	float temp = 0;
	for (int i = 0; i < 120 ; i++)
	{
		temp += windspdavg[i];	//array se rellena en el loop()
	}
	temp /= 120.0;
	windspd_kph_avg2m = temp;

	//Calc winddir_avg2m, Wind Direction
	//You can't just take the average. Google "mean of circular quantities" for more info
	//We will use the Mitsuta method because it doesn't require trig functions
	//And because it sounds cool.
	//Based on: http://abelian.org/vlf/bearings.html
	//Based on: http://stackoverflow.com/questions/1813483/averaging-angles-again
	// FORMULA QUEDA INTACTA[!]
	long sum = winddiravg[0];
	int D = winddiravg[0];
	for(int i = 1 ; i < WIND_DIR_AVG_SIZE ; i++)
	{
		int delta = winddiravg[i] - D;

		if(delta < -180)
			D += delta + 360;
		else if(delta > 180)
			D += delta - 360;
		else
			D += delta;

		sum += D;
	}
	winddir_avg2m = sum / WIND_DIR_AVG_SIZE;
	if(winddir_avg2m >= 360) winddir_avg2m -= 360;
	if(winddir_avg2m < 0) winddir_avg2m += 360;

	//Find the largest windgust in the last 10 minutes
	windgust_kph_10m = 0;
	windgustdir_10m = 0;
	
	//Step through the 10 minutes in kph
	for (int i = 0; i < 10 ; i++)
	{
		if (windgust_10m[i] > windgust_kph_10m)
		{
			windgust_kph_10m = windgust_10m[i];
			windgustdir_10m = windgustdirection_10m[i];
		}
	}
	
	//Total rainfall for the day is calculated within the interrupt
	//Calculate amount of rainfall for the last 60 minutes
	rainin = 0;
	for(int i = 0 ; i < 60 ; i++)
	rainin += rainHour[i];
}

//Returns the instantaneous wind speed
//VMH: Se reemplaza unidad métrica de acumulación
float get_wind_speed()
{
	float deltaTime = millis() - lastWindCheck;		//se obtiene el tiempo en milisegundos entre la primera revision de la informacion
	deltaTime /= 1000.0;							//se lleva deltaTime a formato de unidad de segundos
	float windSpeed = (float)windClicks / deltaTime;	//se obtiene la cantidad de veces que se activó el interruptor magnético (1 interrupción es igual a 2.4kph)
	windClicks = 0;										//se vuelve a inicializar la variable volatil
	lastWindCheck = millis();							//se registra la actual medición de tiempo en milisegundos
	windSpeed *= 2.4;								//cantidad de veces interrumpidas por el factor 2.4, entrega la velocidad en kph
	return(windSpeed);								//retorna un float windSpeed
}

//Read the wind direction sensor, return heading in degrees
int get_wind_direction()
{
	unsigned int adc;
	adc = analogRead(WDIR_ADC); // get the current reading from the sensor
	
	// VMH: se realiza el cambio de parametro original que correspondía al valor en grados por
	// un valor que corresponde al indice de las matrices
	// nameDirWind y numDirWind
	
	if (adc < 68) return (5);
	if (adc < 89) return (3);
	if (adc < 98) return (4);
	if (adc < 129) return (7);
	if (adc < 189) return (6);
	if (adc < 249) return (9);
	if (adc < 299) return (8);
	if (adc < 419) return (1);
	if (adc < 469) return (2);
	if (adc < 609) return (11);
	if (adc < 639) return (10);
	if (adc < 709) return (15);
	if (adc < 795) return (0);
	if (adc < 829) return (13);
	if (adc < 889) return (14);
	if (adc < 949) return (12);
	return (-1); // error, disconnected?
}

void print_wind_dir_name(uint8_t x){
	if (x >= 0)	{
		Serial.print(nameDirWind[x]);
		}else{
		Serial.println("Error de lectura, posible pin desconectado");
	}
}

void print_wind_dir_grade(uint8_t x){
	if (x >= 0)	{
		Serial.print(numDirWind[x]);
		} else {
		Serial.println("Error de lectura, posible pin desconectado");
	}
}


//Prints the various variables directly to the port
//I don't like the way this function is written but Arduino doesn't support floats under sprintf
void printSensors()
{
	calcWeather(); //Go calc all the various sensors
	//Serial.println("inicio cadena");
	Serial.println(lumens());
	delay(1);
	Serial.println(uv());
	delay(1);
	Serial.println(winddir);					//lectura DIRECCION (Grados) instantánea
	delay(1);
	Serial.println(_nameWDir);					//lectura DIRECCION (Cardinal) instantánea
	delay(1);
	Serial.println(winddir_avg2m);				//lectura DIRECCION (Grados) prom 2min
	delay(1);
	Serial.println(windspd_kph_avg2m, 2);		//lectura VIENTO prom 2min, imprime con 1 decimal
	delay(1);
	Serial.println(windgust_kph, 2);			//lectura RAFAGA instantánea
	delay(1);
	Serial.println(windgust_kph_10m, 2);		//lectura RAFAGA prom 10min
	delay(1);
	Serial.println(windgustdir);				//lectura DIRECCION RAFAGA instantanea
	delay(1);
	Serial.println(windgustdir_10m);			//lectura DIRECCION RAFAGA prom 10min
	delay(1);
	Serial.println(rainin, 2);				//lectura acumulativa de la lluvia durante 1hr (tras 1hr se reinicia)
	delay(1);
	Serial.println(dailyrainin, 2);			//lectura instantanea de la lluvia acumulada (habría que considerar resetear el valor desde el acumulador)
	delay(1);
	//Serial.println("fin cadena");
}



void loop()
{
    //Keep track of which minute it is
	if(millis() - lastSecond >= 1000)
    {
    lastSecond += 1000;
        //Take a speed and direction reading every second for 2 minute average
        if(++seconds_2m > 119) seconds_2m = 0;

        //Calc the wind speed and direction every second for 120 second to get 2 minute average
        float currentSpeed = get_wind_speed();
        windspeed_kph = currentSpeed; //update global variable for windspeed when using the printWeather() function
        int current_index_Direction = get_wind_direction();
		_nameWDir = nameDirWind[current_index_Direction];
		windspdavg[seconds_2m] = (int)currentSpeed;
		winddiravg[seconds_2m] = numDirWind[current_index_Direction];

        //Check to see if this is a gust for the minute
        if(currentSpeed > windgust_10m[minutes_10m])
        {
            windgust_10m[minutes_10m] = currentSpeed;
            windgustdirection_10m[minutes_10m] = numDirWind[current_index_Direction];
        }

		//Check to see if this is a gust for the day in kph
		if (currentSpeed > windgust_kph)		//Si la velocidad actual es MAYOR que la velocidad de RAFAGA
		{
			windgust_kph = currentSpeed;
			windgustdir = numDirWind[current_index_Direction];
		}

        if(++seconds > 59)
        {
            seconds = 0;

            if(++minutes > 59) minutes = 0;
            if(++minutes_10m > 9) minutes_10m = 0;
			if(lastSecond > 0xFFFFFFF0) lastSecond = 0;	//evitar activar WD por desborde
			if(lastWindIRQ > 0xFFFFFFF0) lastWindIRQ = 0; //evitar activar WD por desborde
            rainHour[minutes] = 0; //Zero out this minute's rainfall amount
            windgust_10m[minutes_10m] = 0; //Zero out this minute's gust
        }

        //Originalmente la pregunta de los parámetros iba acá, pero como ya no se necesita
		//preguntar a cada segundo por lo parámetros, sino más bien, por cada consulta 
		//que viene desde la raspberry, se habilita el SerialEvent()
	}
	
}



//-----------------FRANCIS------------------------



float lumens()
{
//lectura lux
	const	long	A = 200;     //Resistencia en oscuridad en KΩ
	const	int	B = 1;        //Resistencia a la luz (10 Lux) en KΩ
	const	int	Rc = 10;       //Resistencia calibracion en KΩ
	lect = analogRead(LUMENS_ADC);
	lux = ((long)lect*A*10)/((long)B*Rc*(1024-lect));
	return(lux);
	
}

float uv()
{
//lectura uv
 /* 
 ML8511 UV Sensor Read Example
 Connect the following ML8511 breakout board to Arduino:
 3.3V = 3.3V
 OUT = A1
 GND = GND
 EN = 3.3V
 3.3V = A3
*/

//Hardware pin definitions
  int uvLevel = averageAnalogRead(UV_ADC);
	int refLevel = averageAnalogRead(REF_3V3_UV);
	//Use the 3.3V power pin as a reference to get a very accurate output value from sensor
	float outputVoltage = 3.3 / refLevel * uvLevel;
	float uvIntensity = mapfloat(outputVoltage, 0.99, 1.9, 0.0, 15.0); //Convert the voltage to a UV intensity level
	if(uvIntensity<0){
    uvIntensity=0;
	}
	return(uvIntensity);
}

//Takes an average of readings on a given pin
//Returns the average
int averageAnalogRead(int pinToRead)
{
  byte numberOfReadings = 8;
  unsigned int runningValue = 0; 

  for(int x = 0 ; x < numberOfReadings ; x++)
    runningValue += analogRead(pinToRead);
  runningValue /= numberOfReadings;

  return(runningValue);  
}

//The Arduino Map function but for floats
float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void serialEvent(){
	while(Serial.available()){
		char inChar = (char)Serial.read();
		if (inChar == 't')
		{
			printSensors();
		}else{
			Serial.println("Caracter equivocado");
		}
	}
}

