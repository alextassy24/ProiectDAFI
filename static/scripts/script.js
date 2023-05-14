var ctx = document.getElementById("myChart1").getContext("2d");
var ctx2 = document.getElementById("myChart2").getContext("2d");

var tempGraphData = {
	type: "line",
	data: {
		labels: [],
		datasets: [
			{
				label: "Temperature(°C)",
				data: [],
				backgroundColor: ["rgba(73,198,230,1)"],
				borderWidth: 5,
			},
		],
	},
	options: {},
};

var presGraphData = {
	type: "line",
	data: {
		labels: [],
		datasets: [
			{
				label: "Presure(bar)",
				data: [],
				backgroundColor: ["rgba(0,0,0,1)"],
				borderWidth: 5,
			},
		],
	},
	options: {},
};

var myTempChart = new Chart(ctx, tempGraphData);
var myPresChart = new Chart(ctx2, presGraphData);

var socket = new WebSocket("ws://localhost:8000/ws/base/");

socket.onmessage = function (e) {
	var djangoData = JSON.parse(e.data);

	var newTempGraphData = tempGraphData.data.datasets[0].data;
	var newTempGraphLabels = tempGraphData.data.labels;
	newTempGraphData.push(djangoData.value_temp);
	newTempGraphLabels.push(djangoData.i);
	tempGraphData.data.datasets[0].data = newTempGraphData;
	myTempChart.update();

	var newPresGraphData = presGraphData.data.datasets[0].data;
	var newPresGraphLabels = presGraphData.data.labels;
	newPresGraphData.push(djangoData.value_press);
	newPresGraphLabels.push(djangoData.i);
	presGraphData.data.datasets[0].data = newPresGraphData;
	myPresChart.update();

	document.querySelector("#temperature").innerText = djangoData.value_temp;
	document.querySelector("#pressure").innerText = djangoData.value_press;
	document.querySelector("#systemStatus").innerText = djangoData.status;
};

let form = document.getElementById("form");

form.addEventListener("submit", (e) => {
	e.preventDefault();
	let tempMinVal = e.target.tempMinValue.value;
	let tempMaxVal = e.target.tempMaxValue.value;
	let pressMinVal = e.target.pressMinValue.value;
	let pressMaxVal = e.target.pressMaxValue.value;

	socket.send(
		JSON.stringify({
			action: "set",
			tempMinVal: tempMinVal,
			tempMaxVal: tempMaxVal,
			pressMinVal: pressMinVal,
			pressMaxVal: pressMaxVal,
		})
	);
});

var coolingButton = document.getElementById("coolingBtn");
var heatingButton = document.getElementById("heatingBtn");
var stopButton = document.getElementById("stopBtn");

coolingButton.addEventListener("click", function () {
	socket.send(JSON.stringify({ action: "cooling" }));
});

heatingButton.addEventListener("click", function () {
	socket.send(JSON.stringify({ action: "heating" }));
});

stopButton.addEventListener("click", function () {
	socket.send(JSON.stringify({ action: "stop" }));
});
