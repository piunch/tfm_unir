$(document).ready(function(){
    // $.ajax({
    //     url: '/transactions',
    //     success: drawChart(),
    //     error: function() {
    //         console.log("No se ha podido obtener la información");
    //     }
    // });
	drawChart();
	$('#add-trx').click(function() {
		$('txdate')
		alert(JSON.stringify($('#form-trx').serializeArray()));
	});

});

function drawChart() {
	window.onload = function() {
        function randomScalingFactor() {
            return Math.round(Math.random() * 100 * (Math.random() > 0.5 ? -1 : 1));
        }
        function randomColorFactor() {
            return Math.round(Math.random() * 255);
        }
        function randomColor(opacity) {
            return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
        }
        function newDate(days) {
            return moment().add(days, 'd').toDate();
        }
        function newDateString(days) {
            return moment().add(days, 'd').format();
        }
        var config = {
            type: 'line',
            data: {
                datasets: [{
                    label: "Dataset with string point data",
                    data: [{
                        x: newDateString(0),
                        y: randomScalingFactor()
                    }, {
                        x: newDateString(2),
                        y: randomScalingFactor()
                    }, {
                        x: newDateString(4),
                        y: randomScalingFactor()
                    }, {
                        x: newDateString(5),
                        y: randomScalingFactor()
                    }],
                    fill: false
                }]
            },
            options: {
                responsive: true,
                title:{
                    display:true,
                    text:"Chart.js Time Point Data"
                },
                scales: {
                    xAxes: [{
                        type: "time",
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'Date'
                        }
                    }],
                    yAxes: [{
                        display: true,
                        scaleLabel: {
                            display: true,
                            labelString: 'value'
                        }
                    }]
                }
            }
		};
		var ctx = document.getElementById("canvas").getContext("2d");
        window.myLine = new Chart(ctx, config);
	};
}
