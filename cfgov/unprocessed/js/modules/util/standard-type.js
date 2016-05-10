'use strict';

// Constant for the name of the JS hook used
// for attaching JS behavior to HTML DOM elements.
var JS_HOOK = 'data-js-hook';

// Constant for the name of the JS hook used
// for flagging the dom as having already been initialized.
// Typically meaning an instance had an init() method called,
// such as after this action:
// var expandable = new Expandable( 'm-expandable' ).init();
var STATE_INIT = 'data-state-initialized';

/**
 * Empty function that will do nothing.
 * A usecase is when an object has empty functions used for callbacks,
 * which are meant to be overridden with functionality, but if not,
 * noopFunct will fire and do nothing instead.
 *
 * e.g.
 * callback.onComplete = standardType.noopFunct;
 */
function noopFunct() {
  // Placeholder function meant to be overridden.
}

var UNDEFINED;

module.exports = {
  JS_HOOK:    JS_HOOK,
  noopFunct:  noopFunct,
  STATE_INIT: STATE_INIT,
  UNDEFINED:  UNDEFINED
};
