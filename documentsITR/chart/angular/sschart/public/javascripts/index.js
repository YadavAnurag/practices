var range = document.getElementById("range");
var altitude = document.getElementById("altitude");
var azimuth = document.getElementById("azimuth");
var positionTime = document.getElementById('positionTime');
var time = document.getElementById('time');
var now = null;


var firstCtx = document.getElementById('firstChart').getContext('2d');
var secondCtx = document.getElementById('secondChart').getContext('2d');


var chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(231,233,237)',
    white: 'rgb(255,255,255)'
};

var fxmax = 1690660;
var fxmin = 0;
var fymax = 955600;
var fymin = 0;

var sxmax = 0;
var sxmin = -1690660;
var symax = 0;
var symin = -1418632;

var firstNominalLabels = [],secondNominalLabels = [];
var firstNominalData = [],secondNominalData = [];
var firstRealTimeData = [],secondRealTimeData = [];


var firstNominalDataset = {
    type: 'line',
    label: 'first Nominal Data',
    borderColor: chartColors.white,
    borderWidth: 0,
    pointRadius: 1,
    pointBackgroundColor: 'white',
    lineTension: 0,
    fill: false,
    data: firstNominalData,
};
var secondNominalDataset = {
    type: 'line',
    label: 'second Nominal Data',
    borderColor: chartColors.white,
    borderWidth: 0,
    pointRadius: 1,
    pointBackgroundColor: 'white',
    lineTension: 0,
    fill: false,
    data: secondNominalData,
};

var firstRealTimeDataset = {
    type: 'line',
    label: 'first RealTime Data',
    //borderColor: chartColors.yellow,
    borderWidth: 0,
    pointRadius: 2,
    pointBackgroundColor: "yellow",
    lineTension: 0,
    fill: false,
    xAxisID: 'firstChart-x-axis-2',
    data: firstRealTimeData
};
var secondRealTimeDataset = {
    type: 'line',
    label: 'second RealTime Data',
    //borderColor: chartColors.yellow,
    borderWidth: 0,
    pointRadius: 2,
    pointBackgroundColor: "yellow",
    lineTension: 0,
    fill: false,
    xAxisID: 'secondChart-x-axis-2',
    data: secondRealTimeData
};

var firstDatasets = [firstRealTimeDataset, firstNominalDataset];
var secondDatasets = [secondRealTimeDataset, secondNominalDataset];

var firstChartOptions = {
    layout: {
        padding: {
            left: 5,
            right: 10,
            top: 5,
            bottom: 5
        }
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        xAxes: [{
                gridLines: {
                    offsetGridLines: false
                }
            },
            {
                id: 'firstChart-x-axis-2',
                type: 'linear',
                position: 'bottom',
                display: true,
                scaleLabel: {
                    display: true,
                    labelString: 'Down Range (km)',
                    fontSize: 20

                },
                ticks: {
                    min: fxmin,
                    max: fxmax,
                    // beginAtZero: true,
                }
            }
        ],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Altitude (km)',
                fontSize: 20
            },


            ticks: {
                //beginAtZero: true,
                min: fymin,
                max: fymax,
            }
        }]
    }
};

var secondChartOptions = {
    layout: {
        padding: {
            left: 5,
            right: 10,
            top: 5,
            bottom: 5
        }
    },
    responsive: true,
    maintainAspectRatio: false,
    scales: {
        xAxes: [{
                gridLines: {
                    offsetGridLines: false
                }
            },
            {
                id: 'secondChart-x-axis-2',
                type: 'linear',
                position: 'bottom',
                display: false,
                scaleLabel: {
                    display: true,
                    labelString: 'Down Range (km)',
                    fontSize: 10

                },
                ticks: {
                    max: sxmax,
                    min: sxmin,
                    //beginAtZero: true,
                }
            }
        ],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Altitude (km)',
                fontSize: 10
            },


            ticks: {
                //beginAtZero: true,
                min: symin,
                max: symax,
            }
        }]
    }
};




var firstConfig = {
    type: 'line',
    data: {
        labels: firstNominalLabels,
        datasets: firstDatasets,
    },
    options: firstChartOptions
};

var secondConfig = {
    type: 'line',
    data: {
        labels: secondNominalLabels,
        datasets: secondDatasets,
    },
    options: secondChartOptions
};

Chart.defaults.global.defaultFontColor = 'white';

var firstChart = new Chart(firstCtx, firstConfig);
var secondChart = new Chart(secondCtx, secondConfig);



var socket = io.connect("127.0.0.1:7777");
socket.on('connect', function () {
    console.log('Client got connected');

});
socket.on('serverMessage', function (data) {
    console.log(data.msg);
});

socket.on("nominalData", function (data) {
    firstConfig.data.labels = data.totalsq;
    firstConfig.data.datasets[1].data = data.totalz;
    
    secondConfig.data.labels = data.totalx;
    secondConfig.data.datasets[1].data = data.totaly;
    
    
    firstChart.update();
    firstChart.update();


    //firstChartOptions.scales.xAxes[1].display = false;

    console.log(firstConfig.data.datasets[1].data.length, firstConfig.data.labels.length, data);
});


socket.on("serverRealTimeData", function (data) {
    console.log(data);

    firstConfig.data.datasets[0].data.push({
        x: data.sq,
        y: data.z
    });

    secondConfig.data.datasets[0].data.push({
        x: data.x,
        y: data.y
    });


    var now = new Date();

    range.innerHTML = data.sq;
    altitude.innerHTML = data.z;
    azimuth.innerHTML = 0;
    positionTime.innerHTML = Number(data.positionTime).toFixed(1) + ' seconds ';

    time.innerHTML = now.getHours() + ':' + now.getMinutes() + ':' + now.getSeconds() + ':' + now.getMilliseconds();

    firstChart.update();
    secondChart.update();

    
});
