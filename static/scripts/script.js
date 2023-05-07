var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
	type: "line",
	data: {
		labels: [],
		datasets: [
			{
				label: "Generated Data",
				data: [],
				borderColor: "rgba(255, 99, 132, 1)",
				backgroundColor: "rgba(255, 99, 132, 0.2)",
			},
		],
	},
	options: {
		scales: {
			yAxes: [
				{
					ticks: {
						beginAtZero: true,
					},
				},
			],
		},
	},
});

var source = new EventSource("{% url 'view_data' %}");
source.onmessage = function (event) {
	var data = JSON.parse(event.data);
	myChart.data.labels.push("");
	myChart.data.datasets[0].data.push(data.value);
	myChart.update();
};
