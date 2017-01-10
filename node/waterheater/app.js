var express = require("express");
var gpio = require("gpio");

var gpio21 = gpio.export(21, {
	direction: 'out',
	interval: 200,
});

var gpio20 = gpio.export(20, {
	direction: 'out',
	interval: 200,
});

var gpio19 = gpio.export(19, {
	direction: 'out',
	interval: 200,
});

var gpio13 = gpio.export(13, {
	direction: 'out',
	interval: 200,
});

var app = express();
var state;

app.post("/on", function(req, res) {
	gpio21.set(0);
	if (gpio21.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio21.value);
	res.send("The heater state is " + state);
});

app.post("/off", function(req, res) {
	gpio21.set(1);
	if (gpio21.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio21.value);
	res.send(state);
});

app.get("/status", function(req, res) {
	if (gpio21.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio21.value);
	res.send(state);
});

app.post("/light_on", function(req, res) {
	gpio19.set(0);
	if (gpio19.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio19.value);
	res.send(state);
});

app.post("/light_off", function(req, res) {
	gpio19.set(1);
	if (gpio19.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio19.value);
	res.send(state);
});

app.post("/valve_on", function(req, res) {
	gpio13.set(0);
	if (gpio13.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio13.value);
	res.send(state);
});

app.post("/valve_off", function(req, res) {
	gpio13.set(1);
	if (gpio13.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio13.value);
	res.send(state);
});

app.post("/other_on", function(req, res) {
	gpio20.set(0);
	if (gpio20.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio20.value);
	res.send(state);
});

app.post("/other_off", function(req, res) {
	gpio20.set(1);
	if (gpio20.value = 0) {
		state = "ON";
	} else {
		state = "OFF";
	}
	console.log("The heater state is ", state);
	console.log("The heater value is ", gpio20.value);
	res.send(state);
});

		
app.listen(3000, function() {
	console.log("App is listening on port 3000");
});

