var gulp = require('gulp'),
    django = require('gulp-django-utils'),
    rename = require('gulp-rename'),
    autoprefixer = require('gulp-autoprefixer'),
    sass = require('gulp-sass'),
    csso = require('gulp-csso'),
    babel = require('gulp-babel'),
    browserSync = require('browser-sync').create('my_server'),
    concat = require('gulp-concat'),
    uglify = require('gulp-uglify'),
    watch = require('gulp-watch');


var projectName = '';
var jsPath = projectName+'frontend/js/';
var cssPath = projectName+'frontend/scss/';
jsFiles = [
    jsPath+'libs/device.min.js',
    jsPath+'libs/jquery-3.1.1.min.js',
    jsPath+'libs/TweenMax.min.js',
    jsPath+'libs/ScrollMagic.min.js',
    jsPath+'libs/animation.gsap.min.js',
    jsPath+'libs/jquery.waypoints.min.js',
    jsPath+'libs/*.js',
    jsPath+'apps/*.js',
    jsPath+'*.js',
];
cssFiles = [
        cssPath+'common/vars.scss',
        cssPath+'common/reset-css.scss',
        cssPath+'common/fonts.scss',
        cssPath+'common/main.scss',
        cssPath+'blocks/*.scss',
        cssPath+'*.scss',
];
// Initialize application list for processing.
var apps = [''];

// Initialize project with apps in current directory.
var project = new django.Project(apps);

project.discoverApps();

// Create a task which depends on the same tasks in apps.

project.task('default', ['css','js']);

project.task('void',function(){});

//WATCH TASK, for some return
project.task('watch', ['css','js', 'watch-css','watch-js','watch-html', 'babel'] ,function() {
    return  browserSync.init({
                proxy: "http://127.0.0.1:8000/",
            });
});


project.task("watch-css", function() {
    return project.watch([
        projectName+'frontend/scss/**/*.scss',
    ],['css']);
});

project.task("watch-js", function() {
    return project.watch(projectName+'frontend/js/**/*.js', ["js"]);
});
project.task("watch-html", function() {
    return project.watch(projectName+'templates/'+projectName+'*.html', ["html_change"]);
});
project.task('html_change',function(){
    browserSync.reload();
})

// END WATCH TASK


project.task('babel', () =>
    gulp.src('static/build/production.js')
        .pipe(babel({
            presets: ["es2015", 'env']
        }))
        .pipe(gulp.dest(projectName+'static/build'))
);

project.task('css', function () {
    return project.src(cssFiles)
            .pipe(concat('production.scss'))
            .pipe(sass().on('error', sass.logError))
            .pipe(autoprefixer({
                browsers: ['last 10 versions'],
                cascade: false
            }))
            .pipe(rename("production.css"))
            .pipe(project.dest(projectName+'static/build'))
            .pipe(browserSync.stream());
});
project.task('css_compress',function(){
    return project.src(projectName+'static/build/production.css')
            .pipe(csso())
            .pipe(project.dest(projectName+'static/build/'));
});
project.task('js', function(){
    return  project.src(jsFiles)
            .pipe(concat('production.js'))
            .pipe(project.dest(projectName+'static/build'))
            .pipe(browserSync.stream());
});
project.task('js_compress',function(){
    return project.src(projectName+'static/build/production.js')
            .pipe(uglify())
            .pipe(project.dest(projectName+'static/build/'));
});
