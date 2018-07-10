var def = 0;
var update = function() {
    var rs = redValue.coordinate();
    var gs = greenValue.coordinate();
    var bs = blueValue.coordinate();
    redRect.fillColor = getColor(rs, def, def);
    greenRect.fillColor = getColor(def, gs, def);
    blueRect.fillColor = getColor(def, def, bs);
    rgbRect.fillColor = getColor(rs,gs,bs);
    
    sliders.draw();
}

var sliders = new Canvas("rgb", [0,0,1.5,3]);

sliders.margins = [20,5,10,5];
sliders.setUpCoordinates();

var rl = new Label("R", [0,2.5]);
var gl = new Label("G", [0,1.5]);
var bl = new Label("B", [0,0.5]);
rl.offset = [-10,-5];
gl.offset = [-10,-5];
bl.offset = [-10,-5];
sliders.addPlotable([rl, gl, bl]);

var redRect = new Rectangle([0,2], [1,1]);
redRect.fillColor = "black";
sliders.addPlotable(redRect);
var greenRect = new Rectangle([0,1], [1,1]);
greenRect.fillColor = "black";
sliders.addPlotable(greenRect);
var blueRect = new Rectangle([0,0], [1,1]);
blueRect.fillColor = "black";
sliders.addPlotable(blueRect);
var rgbRect = new Rectangle([1.1,0], [0.3,3]);
rgbRect.fillColor = "black";
sliders.addPlotable(rgbRect);

var mkslider = function(range, y) {
    var s = new Slider([0,1], y, range, update);
    s.point.style = "rect";
    s.point.fillColor = "lightgray";
    s.point.width = 5;
    s.point.height = 10; //10
    s.point.centerLine = true;
    sliders.addPlotable(s);
    sliders.addMoveable(s);
    return s;
}

var redValue = mkslider([0,255], 2.5);
var greenValue = mkslider([0,255], 1.5);
var blueValue = mkslider([0,255], 0.5);
redValue.init(128);
greenValue.init(128);
blueValue.init(128);

var getColor = function(r,g,b) {
    return 'rgb(' + Math.floor(r) + ',' +
        Math.floor(g) + ',' +
	Math.floor(b) + ')';
}

update();


