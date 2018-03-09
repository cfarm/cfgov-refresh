const BASE_JS_PATH = '../../../../cfgov/unprocessed/js/';
const chai = require( 'chai' );
const expect = chai.expect;
const sinon = require( 'sinon' );
let BreakpointHandler;
let args;
const standardType = require( BASE_JS_PATH + 'modules/util/standard-type' );

/**
 * Change the viewport to width x height. Mocks window.resizeTo( w, h ).
 * @param  {number} width - width in pixels.
 * @param  {number} height - height in pixels.
 */
function windowResizeTo( width, height ) {
  // Change the viewport to width x height. Mocks window.resizeTo( w, h ).
  global.innerWidth = width;
  global.innerHeight = height;

  // Trigger the window resize event.
  global.dispatchEvent( new Event( 'resize' ) );
}

describe( 'BreakpointHandler', () => {
  beforeEach( () => {
    args = {
      enter:      standardType.noopFunct,
      leave:      standardType.noopFunct,
      breakpoint: 600
    };

    BreakpointHandler = require( BASE_JS_PATH + 'modules/BreakpointHandler' );
  } );

  it( 'should throw an error if passed incomplete arguments', () => {
    const errorTxt = 'BreakpointHandler constructor requires arguments!';
    function createBreakpointInstance() {
      return new BreakpointHandler();
    }

    expect( createBreakpointInstance ).to.throw( errorTxt );
  } );

  it( 'should correctly create BreakpointHandler instances', () => {
    const breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.watchWindowResize )
      .to.be.an.instanceof( Function );
    expect( breakpointHandler.handleViewportChange )
      .to.be.an.instanceof( Function );
    expect( breakpointHandler.testBreakpoint )
      .to.be.an.instanceof( Function );

    expect( breakpointHandler.match ).to.be.false;
    expect( breakpointHandler.type === 'max' ).to.be.true;
  } );

  it( 'should allow responsive breakpoints as arguments', () => {
    args.breakpoint = 'bpXS';
    let breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.breakpoint ).to.equal( 600 );
    expect( breakpointHandler.type === 'max' ).to.be.true;
    expect( breakpointHandler.testBreakpoint( 300 ) ).to.be.true;

    args.breakpoint = 'bpSM';
    args.type = 'min';
    breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.breakpoint ).to.equal( 601 );
    expect( breakpointHandler.type === 'min' ).to.be.true;
    expect( breakpointHandler.testBreakpoint( 601 ) ).to.be.true;
  } );

  it( 'should test a breakpoint', () => {
    let breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.testBreakpoint( 601 ) ).to.be.false;

    args.type = 'min';
    breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.testBreakpoint( 601 ) ).to.be.true;

    args.type = 'range';
    args.breakpoint = [ 0, 600 ];
    breakpointHandler = new BreakpointHandler( args );
    expect( breakpointHandler.testBreakpoint( 300 ) ).to.be.true;
    expect( breakpointHandler.testBreakpoint( 601 ) ).to.be.false;
  } );

  it( 'should handle viewport changes', () => {
    let breakpointHandler = new BreakpointHandler( args );
    let enterSpy = sinon.spy( breakpointHandler, 'enter' );
    let leaveSpy = sinon.spy( breakpointHandler, 'leave' );

    windowResizeTo( 598, 800 );
    expect( enterSpy.calledOnce ).to.be.true;
    expect( enterSpy.calledWithMatch( sinon.match.has( 'isBpXS', true ) ) )
      .to.be.true;

    windowResizeTo( 601, 800 );
    expect( leaveSpy.calledOnce ).to.be.true;
    expect( leaveSpy.calledWithMatch( sinon.match.has( 'isBpSM', true ) ) )
      .to.be.true;

    args.type = 'min';
    args.breakpoint = 901;
    breakpointHandler = new BreakpointHandler( args );
    enterSpy = sinon.spy( breakpointHandler, 'enter' );
    windowResizeTo( 1000, 800 );
    expect( enterSpy.calledOnce ).to.be.true;
    expect( enterSpy.calledWithMatch( sinon.match.has( 'isBpMED', true ) ) )
      .to.be.true;

    args.type = 'max';
    args.breakpoint = 1020;
    breakpointHandler = new BreakpointHandler( args );
    leaveSpy = sinon.spy( breakpointHandler, 'leave' );
    windowResizeTo( 1021, 800 );
    expect( leaveSpy.calledOnce ).to.be.true;
    expect( leaveSpy.calledWithMatch( sinon.match.has( 'isBpLG', true ) ) )
      .to.be.true;
  } );

  it( 'should watch for window resize events', () => {
    const breakpointHandler = new BreakpointHandler( args );
    const handleViewportChangeSpy = sinon.spy(
      breakpointHandler, 'handleViewportChange'
    );

    expect( handleViewportChangeSpy.called ).to.be.false;
    windowResizeTo( 1200, 800 );
    expect( handleViewportChangeSpy.called ).to.be.true;
  } );
} );