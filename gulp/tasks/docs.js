'use strict';

var $ = require( 'gulp-load-plugins' )();
var configScripts = require( '../config' ).scripts;
var fsHelper = require( '../utils/fs-helper' );
var glob = require( 'glob' );
var gulp = require( 'gulp' );
var spawn = require( 'child_process' ).spawn;

/**
 * Generate scripts documentation.
 */
function docsScripts() {
  glob( configScripts.src, function( er, files ) {
    var options = [ 'build' ].concat( files ).concat(
                  [ '--github',
                    '--output=docs/scripts',
                    '--format=html' ] );
    spawn(
    fsHelper.getBinary( 'documentation', 'documentation.js' ),
      options, { stdio: 'inherit' }
    ).once( 'close', function() {
      $.util.log( 'Scripts documentation generated!' );
    } );
  } );
}

gulp.task( 'docs:scripts', docsScripts );

gulp.task( 'docs',
  [
    'docs:scripts'
  ]
);
