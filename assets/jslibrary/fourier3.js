var w0 = 5;
var w3 = 0;

var update3 = function() {
    w3 = w3slider.coordinate();
    for (var i = 0; i < 8; i++) {
	points3[i].point = [i,f3(i)];
	lines3[i].p1 = [i, f3(i)];
    }
    fourier3.draw();
}

var fourier3 = new Canvas("fourier3", [0,-3,7,10]);

fourier3.margins = [10,10,10,10]
fourier3.setUpCoordinates();

dy = 0
y0 = -3
y3 = y0 - dy

var w3l = new Label("F", [2, y3]);
w3l.offset = [-23,-3];
var w30 = new Label("3", [2,y3]);
w30.offset = [-14,-8];
fourier3.addPlotable([w3l, w30])

var w3slider = new Slider([2,6], y3, [-1.5,1.5], update3);
w3slider.point.style = "box";
w3slider.point.fillColor = "blue";
w3slider.point.size = 4
w3slider.init(w3);
fourier3.addPlotable(w3slider);
fourier3.addMoveable(w3slider);

var f3 = function(x) {
    return 5 + w3*Math.cos(3*Math.PI*(2*x+1)/16.0)
	+ 0*Math.cos(7*Math.PI*(2*x+1)/16.0);
}

var f7 = function(x) {
    return 5 + 0*Math.cos(3*Math.PI*(2*x+1)/16.0)
	+ w7*Math.cos(7*Math.PI*(2*x+1)/16.0);
}

var graph3 = new Graph(new Function(f3));
graph3.lineWidth = 2;
graph3.strokeColor = "gray"
fourier3.addPlotable(graph3);

var points3 = [];
var lines3 = [];
for (var i = 0; i < 8; i++) {
    var p = new Point([i, f3(i)]);
    p.fillColor = "blue"
    points3.push(p);

    var l = new Line([i,0], [i,f3(i)]);
    l.strokeColor = "lightgray";
    lines3.push(l);
}
fourier3.addPlotable(lines3);
fourier3.addPlotable(points3);
axes3 = new Axes()
fourier3.addPlotable(axes3);
axes3.ticks = [[0,1,7], null]
axes3.labels = [[0,1,7], null]

update3();


