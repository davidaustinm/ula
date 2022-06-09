var def = 0;
var hsvupdate = function() {
    var h = hValue.coordinate();
    var s = sValue.coordinate();
    var v = vValue.coordinate();
    var values = hsv2rgb(h, 1, 1);
    hRect.fillColor = getColor(values[0], values[1], values[2]);
    values = hsv2rgb(180, s, 1);
    sRect.fillColor = getColor(values[0], values[1], values[2]);
    values = hsv2rgb(180, 1, v);
    vRect.fillColor = getColor(values[0], values[1], values[2]);
    values = hsv2rgb(h,s,v);
    hsvRect.fillColor = getColor(values[0], values[1], values[2]);
    
    hsvsliders.draw();
}

var hsv2rgb = function(h, s, v) {
    if (s <= 0) return [255*v,255*v,255*v];
    if (h >= 360) h = 0;
    h /= 60;
    var i = Math.floor(h);
    var f = h - i;
    var p = v * (1-s);
    var q = v * (1 - (s*f));
    var t = v * (1 - (s * ( 1 -f)));
    switch(i) {
    case 0: return [255*v,255*t,255*p];
    case 1: return [255*q,255*v,255*p];
    case 2: return [255*p,255*v,255*t];
    case 3: return [255*p,255*q,255*v];
    case 4: return [255*t,255*p,255*v];
    case 5:
    default: return [255*v,255*p,255*q];
    }
}

var hsvsliders = new Canvas("hsv", [0,0,1.5,3]);

hsvsliders.margins = [20,5,10,5];
hsvsliders.setUpCoordinates();

var hl = new Label("H", [0,2.5]);
var sl = new Label("S", [0,1.5]);
var vl = new Label("V", [0,0.5]);
hl.offset = [-12,-5];
sl.offset = [-12,-5];
vl.offset = [-12,-5];
hsvsliders.addPlotable([hl, sl, vl]);

var hRect = new Rectangle([0,2], [1,1]);
hRect.fillColor = "black";
hsvsliders.addPlotable(hRect);
var sRect = new Rectangle([0,1], [1,1]);
sRect.fillColor = "black";
hsvsliders.addPlotable(sRect);
var vRect = new Rectangle([0,0], [1,1]);
vRect.fillColor = "black";
hsvsliders.addPlotable(vRect);
var hsvRect = new Rectangle([1.1,0], [0.3,3]);
hsvRect.fillColor = "black";
hsvsliders.addPlotable(hsvRect);

var mkslider = function(range, y) {
    var s = new Slider([0,1], y, range, hsvupdate);
    s.point.style = "rect";
    s.point.fillColor = "lightgray";
    s.point.width = 5;
    s.point.height = 10;
    s.point.centerLine = true;
    hsvsliders.addPlotable(s);
    hsvsliders.addMoveable(s);
    return s;
}

var hValue = mkslider([0,360], 2.5);
var sValue = mkslider([0,1], 1.5);
var vValue = mkslider([0,1], 0.5);
hValue.init(180);
sValue.init(0.5);
vValue.init(0.5);

var getColor = function(r,g,b) {
    return 'rgb(' + Math.floor(r) + ',' +
        Math.floor(g) + ',' +
	Math.floor(b) + ')';
}

hsvupdate();


