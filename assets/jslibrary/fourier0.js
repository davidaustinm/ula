var w0 = 5;
var w3 = 0;
var w7 = 0;

var update0 = function() {
    w0 = w0slider.coordinate();
    for (var i = 0; i < 8; i++) {
	points0[i].point = [i,f0(i)];
	lines0[i].p1 = [i, f0(i)];
    }
    fourier0.draw();
}

var fourier0 = new Canvas("fourier0", [0,-3,7,10]);

fourier0.margins = [10,10,10,10]
fourier0.setUpCoordinates();

dy = 0
y0 = -3
var w0l = new Label("F", [2,y0]);
w0l.offset = [-23,-3];
var w00 = new Label("0", [2,y0]);
w00.offset = [-14,-8];
fourier0.addPlotable([w0l, w00])

var w0slider = new Slider([2,6], y0, [5,8], update0);
w0slider.point.style = "box";
w0slider.point.fillColor = "blue";
w0slider.point.size = 4;
w0slider.init(w0);
fourier0.addPlotable(w0slider);
fourier0.addMoveable(w0slider);

var f0 = function(x) {
    return w0 + 0*Math.cos(3*Math.PI*(2*x+1)/16.0)
	+ 0*Math.cos(7*Math.PI*(2*x+1)/16.0);
}

var graph0 = new Graph(new Function(f0));
graph0.lineWidth = 2;
graph0.strokeColor = "gray"
fourier0.addPlotable(graph0);

var points0 = [];
var lines0 = [];
for (var i = 0; i < 8; i++) {
    var p = new Point([i, f0(i)]);
    p.fillColor = "blue"
    points0.push(p);

    var l = new Line([i,0], [i,f0(i)]);
    l.strokeColor = "lightgray";
    lines0.push(l);
}
fourier0.addPlotable(lines0);
fourier0.addPlotable(points0);
axes0 = new Axes()
fourier0.addPlotable(axes0);
axes0.ticks = [[0,1,7], null]
axes0.labels = [[0,1,7], null]

update0();


