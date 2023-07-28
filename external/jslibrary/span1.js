var bottommatrix = new Canvas("span1-sliders", [0,0, 2,2]);
var bottomcanvas = new Canvas("span1-canvas", [-4,-4,4,4]);

bottommatrix.margins = [20,5,20,5];
bottommatrix.setUpCoordinates();
bottomcanvas.margins = [5,5,5,5];
bottomcanvas.setUpCoordinates();

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

var bottomupdate = function() {
    var ma = ba.coordinate();
    var mb = bb.coordinate();
    bv.head = [ma*1 + mb*(-2), ma*2 + mb*(-4)];
    bottommatrix.draw();
    bottomcanvas.draw();
}

var lba = new Label("c", [0,1.5]);
lba.offset = [-5,-3]
lba.font = "italic 16px arial";
bottommatrix.addPlotable(lba);

var lbb = new Label("d", [0,0.5]);
lbb.offset = [-5,-3]
lbb.font = "italic 16px arial";
bottommatrix.addPlotable(lbb);

var lbu = new Label("v", [1,2]);
lbu.offset = [-10,5];
lbu.font = "bold 16px arial";
bottomcanvas.addPlotable(lbu)

var lbv = new Label("w", [-2,-4]);
lbv.offset = [-10,5];
lbv.font = "bold 16px arial";
bottomcanvas.addPlotable(lbv);

var ba = mkslider([dx, 2-dx], 1.5, bottommatrix, bottomupdate);
var bb = mkslider([dx, 2-dx], 0.5, bottommatrix, bottomupdate);
ba.init(1);
bb.init(0);

var bcgrid = new Grid([-4,1,4], [-4,1,4]);
bottomcanvas.addPlotable(bcgrid);

var bcaxes = new Axes();
bcaxes.labels = [[-4,1,4], [-4,1,4]]
bcaxes.ticks = [[-4,1,4], [-4,1,4]]
bottomcanvas.addPlotable(bcaxes);

var line = new Line([-2,-4],[2,4])
line.strokeColor = "gray"
bottomcanvas.addPlotable(line)

var bu = new Vector([1,2]);
var bv = new Vector([-2,-4])
bu.fillColor = "white";
bv.fillColor = "white";
bottomcanvas.addPlotable(bu);
bottomcanvas.addPlotable(bv);

var bv = new Vector([1,2]);
bv.fillColor = "red";
bottomcanvas.addPlotable(bv);

bottomupdate();


