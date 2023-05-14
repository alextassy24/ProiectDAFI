var ctx = document.getElementById("myChart").getContext("2d");

var graphData = {
	type: "line",
	data: {
		labels: ["jan", "feb", "mar", "apr", "may", "jun"],
		datasets: [
			{
				label: "Temperature",
				data: [12, 19, 3, 5, 2, 3],
				backgroundColor: ["rgba(73,198,230,0.5)"],
				borderWidth: 5,
			},
		],
	},
	options: {},
};

var myChart = new Chart(ctx, graphData);

var socket = new WebSocket("ws://localhost:8000/ws/base/");

socket.onmessage = function (e) {
	var djangoData = JSON.parse(e.data);
	console.log(djangoData);

	var newGraphData = graphData.data.datasets[0].data;
	newGraphData.shift();
	newGraphData.push(djangoData.value);
	graphData.data.datasets[0].data = newGraphData;
	myChart.update();

	document.querySelector("#app").innerText = djangoData.value;
};
