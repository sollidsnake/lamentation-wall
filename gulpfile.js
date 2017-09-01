var gulp = require('gulp');
var uglify = require('gulp-uglify');
var concat = require('gulp-concat');
var cleanCSS = require('gulp-clean-css');


gulp.task('js', function() {
    var files = ['./res/js/jquery-2.1.0.min.js',
                 './res/js/jquery.browser.min.js',
                 './res/bootstrap/js/bootstrap.min.js',
                 './res/js/parsley.min.js',
                 './res/me/generic.js',
                 './res/me/script.js',
                ];

    return gulp.src(files)
        .pipe(concat('script.js'))
        .pipe(uglify())
        .pipe(gulp.dest('static/'));
});

gulp.task('css', function() {
    var files = ['./res/bootstrap/css/bootstrap.css',
                 './res/me/style.css'
                ];

    return gulp.src(files)
        .pipe(concat('style.css'))
        .pipe(cleanCSS())
        .pipe(gulp.dest('static/'));
});

gulp.task('default', ['js']);
