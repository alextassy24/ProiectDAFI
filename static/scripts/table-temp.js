function updateTempTable(data) {
	var tableBody = $("#temp-table tbody");
	tableBody.empty();

	for (var i = 0; i < data.length; i++) {
		var timestamp = new Date(data[i].timestamp).toLocaleString("en-US", {
			year: "numeric",
			month: "long",
			day: "numeric",
			hour: "numeric",
			minute: "numeric",
			second: "numeric",
		});

		var row =
			"<tr>" +
			"<td>" +
			data[i].id +
			"</td>" +
			"<td>" +
			timestamp +
			"</td>" +
			"<td>" +
			data[i].value +
			"</td>" +
			"</tr>";
		tableBody.append(row);
	}
}

function updateTempPaginationLinks(pageNumber, totalPages) {
	var previousPageLink = $("#temp-previous-page a");
	var nextPageLink = $("#temp-next-page a");

	previousPageLink.attr("onclick", "loadTempPage(" + (pageNumber - 1) + "); return false;");
	nextPageLink.attr("onclick", "loadTempPage(" + (pageNumber + 1) + "); return false;");

	if (pageNumber === 1) {
		previousPageLink.parent().addClass("disabled");
	} else {
		previousPageLink.parent().removeClass("disabled");
	}

	if (pageNumber === totalPages) {
		nextPageLink.parent().addClass("disabled");
	} else {
		nextPageLink.parent().removeClass("disabled");
	}
}

function loadTempPage(pageNumber) {
	$.ajax({
		url: "/pagination-temp/",
		type: "GET",
		data: { page: pageNumber },
		dataType: "json",
		success: function (response) {
			updateTempTable(response.data);
			updateTempPaginationLinks(pageNumber, response.total_pages);
		},
		error: function (xhr, status, error) {
			console.log(error);
		},
	});
}

loadTempPage(1);
