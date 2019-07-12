var range = document.getElementById("range");
var altitude = document.getElementById("altitude");
var azimuth = document.getElementById("azimuth");
var positionTime = document.getElementById('positionTime');
var time = document.getElementById('time');
var now = null;
var localNominalData = null;

var firstCtx = document.getElementById('firstChart').getContext('2d');
var secondCtx = document.getElementById('secondChart').getContext('2d');

var firstChart,secondChart;

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

var fxmax = 0;
var fxmin = 0;
var fymax = 0;
var fymin = 0;

var sxmax = 0;
var sxmin = 0;
var symax = 0;
var symin = 0;

var firstNominalLabels = [],secondNominalLabels = [];
var firstNominalData = [],secondNominalData = [];
var firstRealTimeData = [],secondRealTimeData = [];


var firstNominalDataset = {
    type: 'scatter',
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
    type: 'scatter',
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
    type: 'scatter',
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
    type: 'scatter',
    label: 'second RealTime Data',
    // borderColor: chartColors.yellow,
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
                    beginAtZero: true,
                }
            }
        ],
        yAxes: [{
            position: 'right',
            scaleLabel: {
                display: true,
                labelString: 'Altitude (km)',
                fontSize: 10
            },


            ticks: {
                beginAtZero: true,
                min: symin,
                max: symax,
            }
        }]
    }
};




var firstConfig = {
    type: 'scatter',
    data: {
        labels: firstNominalLabels,
        datasets: firstDatasets,
    },
    options: firstChartOptions
};
var firstConfig1 = {
    type: 'scatter',
    data: {
        labels: firstNominalLabels,
        datasets: firstDatasets,
    },
    options: firstChartOptions
};

var secondConfig = {
    type: 'scatter',
    data: {
        labels: secondNominalLabels,
        datasets: secondDatasets,
    },
    options: secondChartOptions
};
var secondConfig1 = {
    type: 'scatter',
    data: {
        labels: secondNominalLabels,
        datasets: secondDatasets,
    },
    options: secondChartOptions
};


Chart.defaults.global.defaultFontColor = 'white';





var socket = io.connect("127.0.0.1:7777");
socket.on('connect', function () {
    console.log('Client got connected');

});
socket.on('serverMessage', function (data) {
    console.log(data.msg);
});





socket.on("nominalData", function (data) {
    
    fxmin = Math.min(...data.totalsq);
    sxmin = Math.min(...data.totalx);   

    fxmax = Math.max(...data.totalsq);
    sxmax = Math.max(...data.totalx);



    fymin = Math.min(...data.totalz);
    symin = Math.min(...data.totaly);   

    fymax = Math.max(...data.totalz);
    symax = Math.max(...data.totaly);

    console.log(fxmax,fxmin,fymax, fymin);
    console.log(fxmax,fxmin,fymax, fymin);

    localNominalData = data;

    updateChart();
});






function updateChart(){

    firstChartOptions.scales.xAxes[1].ticks.max = fxmax;
    firstChartOptions.scales.xAxes[1].ticks.min = fxmin;
    firstChartOptions.scales.yAxes[0].ticks.max = fymax;
    firstChartOptions.scales.yAxes[0].ticks.min = fymin;

    secondChartOptions.scales.xAxes[1].ticks.max = sxmax;
    secondChartOptions.scales.xAxes[1].ticks.min = sxmin;
    secondChartOptions.scales.yAxes[0].ticks.max = symax;
    secondChartOptions.scales.yAxes[0].ticks.min = symin;


    for(i =0; i<localNominalData.totalx.length; i++){

        firstConfig.data.datasets[1].data.push({
            x: localNominalData.totalsq[i],
            y: localNominalData.totalz[i]
        });
        
        secondConfig.data.datasets[1].data.push({
            x: localNominalData.totalx[i],
            y: localNominalData.totaly[i]
        });
    }

    firstChart1 = new Chart.Scatter(firstCtx, firstConfig1);
    secondChart1 = new Chart.Scatter(secondCtx, secondConfig1);

    rsFxmax = firstChart1.scales["x-axis-1"].max;
    rsFxmin = firstChart1.scales["x-axis-1"].min;

    rsSxmax = secondChart1.scales["x-axis-1"].max;
    rsSxmin = secondChart1.scales["x-axis-1"].min;

    

    firstChartOptions.scales.xAxes[1].ticks.max = rsFxmax;
    firstChartOptions.scales.xAxes[1].ticks.min = rsFxmin;
    secondChartOptions.scales.xAxes[1].ticks.max = rsSxmax;
    secondChartOptions.scales.xAxes[1].ticks.min = rsSxmin;
    

    firstChart = new Chart.Scatter(firstCtx, firstConfig);
    secondChart = new Chart.Scatter(secondCtx, secondConfig);

    firstChart.update();
    secondChart.update();

    console.log(firstChart);

}


socket.on("serverRealTimeData", function (data) {

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

socket.on("tcpServerUdpData", function(data){
    console.log(data);
});