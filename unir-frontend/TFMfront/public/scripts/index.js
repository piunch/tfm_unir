$(document).ready(function(){
    $.ajax({
        url: '/transactions',
        success: drawChart(respuesta),
        error: function() {
            console.log("No se ha podido obtener la información");
        }
    });
});

function drawChart(respuesta) {
    var ctx = document.getElementById("myChart");
    var myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                fill: false,
                label: 'Balance mensual',
                data: [12, 19, 3, 5, 2, 3],
                borderColor: [
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 3
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'time',
                    time: {
                        displayFormats: {
                            quarter: 'MMM D'
                        }
                    }
                }]
            }
        }
    });
}
