$(document).ready(function(){
    $('#add-trx').click(function() {
        $('txdate')
        alert(JSON.stringify($('#form-trx').serializeArray()));
    });
    
    getBalance();
    getTransactions();
});

function getTransactions() {
    $.ajax({
        type: "GET",
        url: '/transactions/balace',
        success: setBalance,
    });
}

function getBalance() {
    $.ajax({
        type: "GET",
        url: '/transactions',
        success: drawChart,
    });
}

function setBalance(response, statusText, code) {
    console.log(response.current_balance);
}

function drawChart(transactions, statusText, code) {
    for (let i = 0; i < transactions.length; i++) {
        transactions[i].x = moment(transactions[i].x, 'YYYY-MM-DD').toDate();
    }
    function randomScalingFactor() {
        return Math.round(Math.random() * 100 * (Math.random() > 0.5 ? -1 : 1));
    }
    function randomColorFactor() {
        return Math.round(Math.random() * 255);
    }
    function randomColor(opacity) {
        return 'rgba(' + randomColorFactor() + ',' + randomColorFactor() + ',' + randomColorFactor() + ',' + (opacity || '.3') + ')';
    }
    var config = {
        type: 'line',
        data: {
            datasets: [{
                label: "Balance de la cuenta Nómina",
                pointRadius: 5,
                pointBackgroundColor: "#E8A87C",
                data: transactions,
                fill: false
            }]
        },
        options: {
            responsive: true,
            title:{
                display:true,
                text:"Balance de la cuenta"
            },
            scales: {
                xAxes: [{
                    type: "time",
                    time: {
                        displayFormat: 'es'
                    },
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Fecha'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Balance'
                    }
                }]
            },
            elements: {
                line: {
                    borderColor: "#E8A87C",
                    borderWidth: 4
                },
                point: {
                    
                }
            }
        }
    };
    var ctx = document.getElementById("canvas").getContext("2d");
    window.myLine = new Chart(ctx, config);
}
