var gulp = require('gulp');
var rename = require('gulp-rename');
var uglify = require( 'gulp-uglify' );
var concat = require( 'gulp-concat' );
var imagemin = require( 'gulp-imagemin' );
var cssmin = require('gulp-cssmin');
var gutil = require('gulp-util');
var $    = require('gulp-load-plugins')();

var sassPaths = [
  'bower_components/normalize.scss/sass',
  'bower_components/foundation-sites/scss',
  'bower_components/motion-ui/src'
];

var js = {
  fileList: [
    'bower_components/jquery/dist/jquery.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.core.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.mediaQuery.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.dropdownMenu.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.sticky.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.tabs.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.drilldown.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.equalizer.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.keyboard.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.triggers.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.accordion.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.timerAndImageLoader.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.box.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.motion.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.timer.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.imageLoader.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.touch.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.util.nest.js',
    'bower_components/foundation-sites/dist/js/plugins/foundation.orbit.js'
  ],
  styles: [
    'bower_components/Ionicons/css/ionicons.css'
  ]
};

/**
 * Dependencias JS
 */

gulp.task( 'build-js', function() {
  return gulp.src( js.fileList )
    .pipe( concat( 'dependencies.js' ) )
    .pipe( uglify().on('error', gutil.log) )
    .pipe( gulp.dest( 'js' ) );
});
/**
 * Minificar imagenes
 */
gulp.task('imgmin', function() {
    gulp.src('img/*')
        .pipe(imagemin())
        .pipe(gulp.dest('img'))
});
/**
 * Dependencias CSS
 */
  gulp.task( 'build-dependencies-css', function() {
    return gulp.src( js.styles )
      .pipe( concat( 'dependencies.css' ) )
      .pipe(cssmin())
      .pipe( gulp.dest( 'css' ) );
});
/*
* Compilador SASS
 */
gulp.task('sass', function() {
  return gulp.src('scss/app.scss')
    .pipe($.sass({
      includePaths: sassPaths,
      outputStyle: 'compressed' // if css compressed **file size**
    })
      .on('error', $.sass.logError))
    .pipe($.autoprefixer({
      browsers: ['last 2 versions', 'ie >= 9']
    }))
    .pipe(gulp.dest('css'));
});

gulp.task('default', ['sass','build-js','build-dependencies-css','imgmin'], function() {
  gulp.watch(['scss/**/*.scss'], ['sass']);
});
