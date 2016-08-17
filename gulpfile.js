var gulp = require('gulp')
var sass = require('gulp-sass')
var concatCss = require('gulp-concat-css')

gulp.task('default', function() {
    console.log('Gulp is great!')
})

gulp.task('watch', function(){
  gulp.watch('catalog/static/catalog/**/*.scss', ['sass'])
})

gulp.task('sass', function(){
  return gulp.src('catalog/static/catalog/**/*.scss')
    .pipe(sass())
    .pipe(concatCss("bundle.css"))
    .pipe(gulp.dest('catalog/static/catalog/dist/'))
})

