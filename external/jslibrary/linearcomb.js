var dx = 0.1;
var mkslider = function(xr, y, canvas, method) {
    var s = new Slider(xr, y, [-2,2], method);
    s.ticks = [-2,1,2]
    s.labels = [-2,1,2]
    s.point.style = "box";
    s.point.fillColor = "blue"
    s.point.size = 4;
    canvas.addPlotable(s);
    canvas.addMoveable(s);
    return s;
}

var topmatrix = new Canvas("linearcomb-sliders", [0,0, 2,2]);
var topcanvas = new Canvas("linearcomb-canvas", [-4,-4,4,4]);

topmatrix.margins = [20,5,20,5];
topmatrix.setUpCoordinates();
topcanvas.margins = [5,5,5,5];
topcanvas.setUpCoordinates();

var topupdate = function() {
    var ma = ta.coordinate();
    var mb = tb.coordinate();
    tv.head = [ma*2 + mb*1, ma*1 + mb*2];
    topmatrix.draw();
    topcanvas.draw();
}

var bottomupdate = function() {
    var ma = ba.coordinate();
    var mb = bb.coordinate();
    bv.head = [ma*1 + mb*(-2), ma*2 + mb*(-4)];
    bottommatrix.draw();
    bottomcanvas.draw();
}

var ta = mkslider([dx, 2-dx], 1.5, topmatrix, topupdate);
var tb = mkslider([dx, 2-dx], 0.5, topmatrix, topupdate);
ta.init(1);
tb.init(0);

var lta = new Label("c", [0,1.5]);
lta.offset = [-5,-3]
lta.font = "italic 16px arial";
topmatrix.addPlotable(lta);

var ltb = new Label("d", [0,0.5]);
ltb.offset = [-5,-3]
ltb.font = "italic 16px arial";
topmatrix.addPlotable(ltb);

var ltu = new Label("v", [2,1]);
ltu.offset = [10,-10];
ltu.font = "bold 16px arial";
topcanvas.addPlotable(ltu)

var ltv = new Label("w", [1,2]);
ltv.offset = [-10,5];
ltv.font = "bold 16px arial";
topcanvas.addPlotable(ltv);

var lba = new Label("a", [0,1.5]);
lba.offset = [-5,-3]
lba.font = "italic 16px arial";

var lbb = new Label("b", [0,0.5]);
lbb.offset = [-5,-3]
lbb.font = "italic 16px arial";

var lbu = new Label("u", [1,2]);
lbu.offset = [-10,5];
lbu.font = "bold 16px arial";

var lbv = new Label("v", [-2,-4]);
lbv.offset = [-10,5];
lbv.font = "bold 16px arial";

var tcgrid = new Grid([-4,1,4], [-4,1,4]);
topcanvas.addPlotable(tcgrid);

var trgrid = new TGrid([2,1],[1,2])
trgrid.strokeColor = "gray"
topcanvas.addPlotable(trgrid)

var tcaxes = new Axes();
tcaxes.labels = [[-4,1,4], [-4,1,4]]
tcaxes.ticks = [[-4,1,4], [-4,1,4]]
topcanvas.addPlotable(tcaxes);

var tu = new Vector([2,1]);
var tv = new Vector([1,2])
tu.fillColor = "white";
tv.fillColor = "white";
topcanvas.addPlotable(tu);
topcanvas.addPlotable(tv);

var bu = new Vector([1,2]);
var bv = new Vector([-2,-4])
bu.fillColor = "gray";
bv.fillColor = "gray";

var tv = new Vector([2,1]);
tv.fillColor = "red";

var bv = new Vector([1,2]);
bv.fillColor = "red";
topcanvas.addPlotable(tv);

topupdate();



