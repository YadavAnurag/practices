var express = require('express');
var app = express();
var expressServer = require('http').createServer(app);
var server = require('socket.io');
var client = require('socket.io-client');
var ip = require('os').networkInterfaces().eno1[0] .address;

app.use(express.static(__dirname, + '/public'));

var ioServer = server(expressServer);
var clientSocket = client('http://127.0.0.1:9898');


let serverSockets = new Set();
let localNominalData = null;


clientSocket.on('connect', () => {
    console.log(`TCP Client connnected with mainServer`);
    clientSocket.emit('getNominalData', {
        msg: 'TCP Client: please send nominal data'
    });
});
clientSocket.on('nominalData', (nominalData) => {
    localNominalData = nominalData;
    console.log(`TCP Client Got nominal-> X: ${nominalData.totalx.length} Y: ${nominalData.totaly.length} Z: ${nominalData.totalz.length} sq: ${nominalData.totalsq.length}`);
});




ioServer.on('connection', (socket) => {
    serverSockets.add(socket.id);
    console.log(`User ${socket.id} connected ${serverSockets.size} remaining`);
    socket.emit('nominalData', localNominalData);

    socket.on('getNominalData', (data) => {
        socket.emit('nominalData', localNominalData);
    });

    socket.on('disconnect', () => {
        serverSockets.delete(socket.id);
        if (!serverSockets.size) {
            stopRealTimeData();
        }
        console.log(`TCP Server: client ${socket.id} disconnected ${serverSockets.size} remaining`);
    });
});



clientSocket.on('disconnect', () => {
    console.log(`TCP Client socket disconnected retrying...`);
    stopRealTimeData();
});
clientSocket.on('error', (error) => {
    console.log(`Error occurred\n ${error}`);
});


clientSocket.on('serverRealTimeData', (realTimeData) => {
    console.log(realTimeData.x, realTimeData.y, realTimeData.z, realTimeData.sq,realTimeData.positionTime);
    ioServer.sockets.emit('serverRealTimeData', realTimeData);
});

//startRealTimeData();
// setTimeout(){
//     console.log(serverSockets.ioServer.emit(1,2,3));
// }


function startRealTimeData() {
    console.log('get called');
    setTimeout(function () {
        console.log('exact get called');
        clientSocket.emit('getRealTimeData', {
            msg: 'Please send realtime data'
        });
    }, 6000);
}

function stopRealTimeData() {
    if (localNominalData && !serverSockets.size) {
        stopMsg = {
            msg: 'Please stop sending realTimeData'
        };
        clientSocket.emit('stopRealTimeData', stopMsg);
        localNominalData = null;
        console.log(`TCP Client: stop event fired`);
    }
}





var port = 7777;
expressServer.listen(port,[ip], ()=>{
    console.log(`TCP Server: start listening on http://${ip}:${port}`);
});