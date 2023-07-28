var w0 = 5;
var w3 = 0;
var w7 = 0;

var update = function() {
    w0 = w0slider.coordinate();
    w3 = w3slider.coordinate();
    w7 = w7slider.coordinate();
    for (var i = 0; i < 8; i++) {
	points[i].point = [i,f(i)];
	lines[i].p1 = [i, f(i)];
    }
    fourier.draw();
}

var fourier = new Canvas("fourier", [0,-3,7,10]);

fourier.margins = [10,10,10,10]
fourier.setUpCoordinates();

dy = 0.8
y0 = -1
y3 = y0 - dy
y7 = y3 - dy
var w0l = new Label("F", [2,y0]);
var w3l = new Label("F", [2, y3]);
var w7l = new Label("F", [2, y7]);
w0l.offset = [-23,-3];
w3l.offset = [-23,-3];
w7l.offset = [-23,-3];
var w00 = new Label("0", [2,y0]);
var w30 = new Label("3", [2,y3]);
var w70 = new Label("7", [2,y7]);
w00.offset = [-14,-8];
w30.offset = [-14,-8];
w70.offset = [-14,-8];
fourier.addPlotable([w0l, w3l, w7l, w00, w30, w70])

var w0slider = new Slider([2,6], y0, [5,8], update);
w0slider.point.style = "box";
w0slider.point.fillColor = "blue";
w0slider.point.size = 4;
w0slider.init(w0);
fourier.addPlotable(w0slider);
fourier.addMoveable(w0slider);

var w3slider = new Slider([2,6], y3, [-1.5,1.5], update);
w3slider.point.style = "box";
w3slider.point.fillColor = "blue";
w3slider.point.size = 4
w3slider.init(w3);
fourier.addPlotable(w3slider);
fourier.addMoveable(w3slider);

var w7slider = new Slider([2,6], y7, [-1.5,1.5], update);
w7slider.point.style = "box";
w7slider.point.fillColor = "blue";
w7slider.point.size = 4
w7slider.init(w7);
fourier.addPlotable(w7slider);
fourier.addMoveable(w7slider);

var f = function(x) {
    return w0 + w3*Math.cos(3*Math.PI*(2*x+1)/16.0)
	+ w7*Math.cos(7*Math.PI*(2*x+1)/16.0);
}

var graph = new Graph(new Function(f));
graph.lineWidth = 2;
graph.strokeColor = "gray"
fourier.addPlotable(graph);

var points = [];
var lines = [];
for (var i = 0; i < 8; i++) {
    var p = new Point([i, f(i)]);
    p.fillColor = "blue"
    points.push(p);

    var l = new Line([i,0], [i,f(i)]);
    l.strokeColor = "lightgray";
    lines.push(l);
}
fourier.addPlotable(lines);
fourier.addPlotable(points);
axes = new Axes()
fourier.addPlotable(axes);
axes.ticks = [[0,1,7], null]
axes.labels = [[0,1,7], null]



update();


