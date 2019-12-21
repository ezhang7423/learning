var circles = {}
function print(thing){
	console.log(thing);
}
var width = view.size.width, height = view.size.height;




var path = new Path.Rectangle(view.center, new Size(100, 50));
path.style = {
	fillColor: 'white',
	strokeColor: 'black'
};

// Create a copy of the path and set its stroke color to red:
var copy = path.clone();
copy.fillColor = 'red';
copy.scale(5, .2)
var rotations = {}
for (var x = 0; x < 7; x++){
	rotations[x] = copy.clone()
	rotations[x].style.fillColor = {
		hue: x,
		saturation: 1,
		brightness: 1,
	}
	console.log(rotations[x].style.fillColor)
}

function onFrame(event) {
	copy.rotate(1)
	// Each frame, rotate the copy by 1 degree:
	for (var x = 0; x < 7; x++){
		rotations[x].rotate(x+2)
}

}
path.visible = false;
