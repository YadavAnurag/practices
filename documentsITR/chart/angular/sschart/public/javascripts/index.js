var x = document.getElementById('x');
var y = document.getElementById("y");
var rowNumberTime = document.getElementById('rowNumberTime');
var time = document.getElementById('time');
var now = null;


var ctx = document.getElementById('myChart').getContext('2d');

var chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(231,233,237)'
};

var xmax = 2207000;
var xmin = 0;

var ymax = 985700;
var ymin = -100;

var nominalLabels = [];
var nominalData = [];
var realTimeData = [];


var nominalDataset = {
    type: 'line',
    label: 'Nominal Data',
    borderColor: chartColors.red,
    borderWidth: 0,
    pointRadius: 0.05,
    lineTension: 0,
    fill: false,
    data: nominalData,
};

var realTimeDataset = {
    type: 'line',
    label: 'RealTime Data',
    borderColor: chartColors.blue,
    borderWidth: 0,
    pointRadius: 3,
    lineTension: 0,
    fill: false,
    xAxisID: 'x-axis-2',
    data: realTimeData
};

var myDatasets = [realTimeDataset, nominalDataset];

var chartOptions = {
    responsive: true,
    title: {
        display: true,
        text: 'RealTime Data with Nominal Data'
    },
    // tooltips: {
    //   mode: 'nearest',
    //   intersect: true,
    // },
    scales: {

        xAxes: [{
                gridLines: {
                    offsetGridLines: false
                }
            },
            {
                id: 'x-axis-2',
                type: 'linear',
                position: 'bottom',
                display: true,
                ticks: {
                    min: xmin,
                    max: xmax,
                    beginAtZero: true,
                    // stepSize: 10
                }
            }
        ],
        yAxes: [{
            ticks: {
                beginAtZero: true,
                min: ymin,
                max: ymax,
                // stepSize: 10
            }
        }]
    }
};


var config = {
    type: 'line',
    data: {
        labels: nominalLabels,
        datasets: myDatasets,
    },
    options: chartOptions
};

var myChart = new Chart(ctx, config);




var socket = io.connect("127.0.0.1:7777");
socket.on('connect', function () {
    console.log('Client got connected');
    //callGetNominalData();
});
socket.on('serverMessage', function (data) {
    console.log(data.msg);
});

socket.on("nominalData", function (data) {
    config.data.datasets[1].data = data.totaly;
    config.data.labels = data.totalx;
    myChart.update();
    console.log(config.data.datasets[1].data.length, config.data.labels.length, data);
});


socket.on("serverRealTimeData", function (data) {
    config.data.datasets[0].data.push({
        x: data.x,
        y: data.y
    });


    var now = new Date();

    x.innerHTML = data.x;
    y.innerHTML = data.y;
    rowNumberTime.innerHTML = Number(data.position) / 10;

    time.innerHTML = now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds() + ':' + now.getMilliseconds();

    myChart.update();
    console.log(typeof (data.i));
});

function callGetNominalData() {
    setTimeout(function () {
        socket.emit("getNominalData", {
            msg: "webclient: Please send nominal data"
        });
        console.log('webClient: event getNominalData fired');
    }, 2000);
}

function callGetRealTimeData() {
    setTimeout(function () {
        if (config.data.labels.length) {
            socket.emit("getRealTimeData", "Please send realtime data");
            console.log('getrealTimeData fired');
        } else {
            console.log('No nominal data..check tcp server running or not');
        }
    }, 8000);
}