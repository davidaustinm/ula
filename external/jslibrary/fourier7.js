var w7 = 0;

var update7 = function() {
    w7 = w7slider.coordinate();
    for (var i = 0; i < 8; i++) {
	points7[i].point = [i,f7(i)];
	lines7[i].p1 = [i, f7(i)];
    }
    fourier7.draw();
}

var fourier7 = new Canvas("fourier7", [0,-3,7,10]);

fourier7.margins = [10,10,10,10]
fourier7.setUpCoordinates();

dy = 0
y0 = -3
y3 = y0 - dy
y7 = y3 - dy
var w7l = new Label("F", [2, y7]);
w7l.offset = [-23,-3];
var w70 = new Label("7", [2,y7]);
w70.offset = [-14,-8];
fourier7.addPlotable([w7l, w70])

var w7slider = new Slider([2,6], y7, [-1.5,1.5], update7);
w7slider.point.style = "box";
w7slider.point.fillColor = "blue";
w7slider.point.size = 4
w7slider.init(w7);
fourier7.addPlotable(w7slider);
fourier7.addMoveable(w7slider);

var f7 = function(x) {
    return 5 + 0*Math.cos(3*Math.PI*(2*x+1)/16.0)
	+ w7*Math.cos(7*Math.PI*(2*x+1)/16.0);
}

var graph7 = new Graph(new Function(f7));
graph7.lineWidth = 2;
graph7.strokeColor = "gray"
fourier7.addPlotable(graph7);

var points7 = [];
var lines7 = [];
for (var i = 0; i < 8; i++) {
    var p = new Point([i, f7(i)]);
    p.fillColor = "blue"
    points7.push(p);

    var l = new Line([i,0], [i,f7(i)]);
    l.strokeColor = "lightgray";
    lines7.push(l);
}
fourier7.addPlotable(lines7);
fourier7.addPlotable(points7);
axes7 = new Axes()
fourier7.addPlotable(axes7);
axes7.ticks = [[0,1,7], null]
axes7.labels = [[0,1,7], null]

update7();


