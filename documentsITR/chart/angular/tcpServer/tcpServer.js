var http = require('http');
var server = require('socket.io');
var client = require('socket.io-client');

let serverSockets = new Set();
let localNominalData = null;

var httpServer = http.createServer((err, req, res) => {
    if (err) {
        console.log(`Server error: \n${err}`);
    }
    res.writeHead(200, {
        "Content-Type": "text/plain"
    });
    res.end("Hello TCP Server");
});


var ioServer = server(httpServer, {});
var clientSocket = client('http://127.0.0.1:9898');




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


clientSocket.on('connect', () => {
    console.log(`TCP Client connnected with mainServer`);
    clientSocket.emit('getNominalData', {
        msg: 'TCP Client: please send nominal data'
    });
});
clientSocket.on('disconnect', () => {
    console.log(`TCP Client socket disconnected retrying...`);
    stopRealTimeData();
});
clientSocket.on('error', (error) => {
    console.log(`Error occurred\n ${error}`);
});

clientSocket.on('nominalData', (nominalData) => {
    localNominalData = nominalData;
    console.log(`TCP Client Got nominal-> X: ${nominalData.totalx.length} Y: ${nominalData.totaly.length}`);
});
clientSocket.on('serverRealTimeData', (realTimeData) => {
    console.log(realTimeData.x, realTimeData.y);
    ioServer.sockets.emit('serverRealTimeData', realTimeData);
});

startRealTimeData();



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





var PORT = 7777;
httpServer.listen(PORT);