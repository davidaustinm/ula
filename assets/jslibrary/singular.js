var bottommatrix = new Canvas("singular-sliders", [0,0, 2,2]);
var bottomleft = new Canvas("singular-left", [-4,-4,4,4]);
var bottomright = new Canvas("singular-right", [-4,-4,4,4]);

bottommatrix.margins = [20,5,20,5];
bottommatrix.setUpCoordinates();
bottomleft.margins = [5,5,5,5];
bottomleft.setUpCoordinates();
bottomright.margins = [5,5,5,5]
bottomright.setUpCoordinates();

var dx = 0.05;
var mkslider = function(xr, y, canvas, method, label) {
    var s = new Slider(xr, y, [-2,2], method);
    s.ticks = [-2,1,2]
    s.labels = [-2,1,2]
    s.point.style = "box";
    s.point.fillColor = "blue"
    s.point.size = 4;
    label = new Label(label, [xr[0], y])
    label.offset = [-8,5]
    label.alignment = "rb"
    canvas.addPlotable(label)
    canvas.addPlotable(s);
    canvas.addMoveable(s);
    return s;
}

var bottomupdate = function() {
    var ma = ba.coordinate();
    var mb = bb.coordinate();
    var mc = bc.coordinate();
    var md = bd.coordinate();
    x = v.head[0];
    y = v.head[1];
    w.head = [ma*x + mb*y, mc*x + md*y];
    h = Math.sqrt(w.head[0]*w.head[0] + w.head[1]*w.head[1])
    wn.head = [w.head[0]/h, w.head[1]/h]
    height.dims=[1,h]
    bottommatrix.draw();
    bottomleft.draw();
    bottomright.draw()
}

var ba = mkslider([dx, 1-2*dx], 1.5, bottommatrix, bottomupdate, "a");
var bb = mkslider([1+2*dx, 2-dx], 1.5, bottommatrix, bottomupdate, "b");
var bc = mkslider([dx, 1-2*dx], 0.5, bottommatrix, bottomupdate, "c");
var bd = mkslider([1+2*dx, 2-dx], 0.5, bottommatrix, bottomupdate,"d");
ba.init(1);
bb.init(0);
bc.init(0);
bd.init(1);

var blgrid = new Grid([-4,1,4], [-4,1,4]);
bottomleft.addPlotable(blgrid);

var blaxes = new Axes();
blaxes.labels = [[-4,1,4], [-4,1,4]]
blaxes.ticks = [[-4,1,4], [-4,1,4]]
bottomleft.addPlotable(blaxes);

var circle = new Circle([0,0], 1);
circle.strokeColor="gray";
circle.fillColor=null;
circle.lineWidth=3;
bottomleft.addPlotable(circle);

var v = new Vector([1,0]);
v.fillColor="red";
v.strokeColor="black";
v.move = function(p) {
    l = Math.sqrt(p[0]*p[0] + p[1]*p[1])
    if (l == 0) return;
    x = p[0]/l;
    y = p[1]/l;
    v.head = [x, y]
    ma = ba.coordinate();
    mb = bb.coordinate();
    mc = bc.coordinate();
    md = bd.coordinate();
    w.head = [ma*x + mb*y, mc*x + md*y];
    bottomupdate();
}
bottomleft.addPlotable(v);
bottomleft.addMoveable(v);

var brgrid = new Grid([-4,1,4], [-4,1,4]);
bottomright.addPlotable(brgrid);

var braxes = new Axes();
braxes.labels = [[-4,1,4], [-4,1,4]]
braxes.ticks = [[-4,1,4], [-4,1,4]]
bottomright.addPlotable(braxes)

var param = function(t) {
    a = ba.coordinate()
    b = bb.coordinate()
    c = bc.coordinate()
    d = bd.coordinate()
    cos = Math.cos(t)
    sin = Math.sin(t)
     p = [a*cos + b*sin, c*cos + d*sin]
     return p
}

var xf = function(t) {
    return param(t)[0]
}
var yf = function(t) {
    return param(t)[1];
}

var height = new Rectangle([3,0], [1,1])
height.fillColor="blue"
bottomright.addPlotable(height);

var ellipse = new ParametricCurve(xf, yf, [0, 2*Math.PI])
ellipse.fillColor=null;
ellipse.strokeColor='darkmagenta';
ellipse.lineWidth=3;
bottomright.addPlotable(ellipse);

var w = new Vector(1,0);
w.fillColor = "gray";
bottomright.addPlotable(w);

var wn = new Vector(1,0);
wn.fillColor="LightSkyBlue"; //"CornflowerBlue";
bottomright.addPlotable(wn);

bottomupdate();


