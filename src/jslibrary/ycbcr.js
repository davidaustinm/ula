var def = 0;
var ycbcrupdate = function() {
    var y = yValue.coordinate();
    var cb = cbValue.coordinate();
    var cr = crValue.coordinate();
    var values = ycbcr2rgb(y, 0, 0);
    yRect.fillColor = getColor(values[0], values[1], values[2]);
    values = ycbcr2rgb(128, cb, 0);
    cbRect.fillColor = getColor(values[0], values[1], values[2]);
    values = ycbcr2rgb(128, 0, cr);
    crRect.fillColor = getColor(values[0], values[1], values[2]);
    values = ycbcr2rgb(y,cb,cr);
    ycbcrRect.fillColor = getColor(values[0], values[1], values[2]);
    
    ycbcrsliders.draw();
}

var ycbcr2rgb = function(y,cb,cr) {
    var rs = y + 1.13983*cr;
    var gs = y - 0.39465*cb - 0.58060*cr;
    var bs = y + 2.03211*cb;
    return [rs,gs,bs];
}

var ycbcrsliders = new Canvas("ycbcr", [0,0,1.5,3]);

ycbcrsliders.margins = [20,5,10,5];
ycbcrsliders.setUpCoordinates();

var yl = new Label("Y", [0,2.5]);
var cbl = new Label("Cb", [0,1.5]);
var crl = new Label("Cr", [0,0.5]);
yl.offset = [-12,-5];
cbl.offset = [-12,-5];
crl.offset = [-12,-5];
ycbcrsliders.addPlotable([yl, cbl, crl]);

var yRect = new Rectangle([0,2], [1,1]);
yRect.fillColor = "black";
ycbcrsliders.addPlotable(yRect);
var cbRect = new Rectangle([0,1], [1,1]);
cbRect.fillColor = "black";
ycbcrsliders.addPlotable(cbRect);
var crRect = new Rectangle([0,0], [1,1]);
crRect.fillColor = "black";
ycbcrsliders.addPlotable(crRect);
var ycbcrRect = new Rectangle([1.1,0], [0.3,3]);
ycbcrRect.fillColor = "black";
ycbcrsliders.addPlotable(ycbcrRect);

var mkslider = function(range, y) {
    var s = new Slider([0,1], y, range, ycbcrupdate);
    s.point.style = "rect";
    s.point.fillColor = "lightgray";
    s.point.width = 5;
    s.point.height = 10;
    s.point.centerLine = true;
    ycbcrsliders.addPlotable(s);
    ycbcrsliders.addMoveable(s);
    return s;
}

var yValue = mkslider([0,255], 2.5);
var cbValue = mkslider([-128,128], 1.5);
var crValue = mkslider([-128,128], 0.5);
yValue.init(128);
cbValue.init(0);
crValue.init(0);

ycbcrupdate();


