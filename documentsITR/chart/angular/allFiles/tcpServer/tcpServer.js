var express = require('express');
var app = express();
var expressServer = require('http').createServer(app);
var server = require('socket.io');
var client = require('socket.io-client');
var ip = require('os').networkInterfaces().eno1[0] .address;
const lineByLine = require('n-readlines/readlines');
const path = require('path');
var fs = require('fs');


app.use(express.static(__dirname, + '/public'));


var ioServer = server(expressServer);
var clientSocket = client('http://127.0.0.1:9898');


let serverSockets = new Set();
let localNominalData = {};

myPath = path.join(__dirname, '/dataFile/test_sim_ss_txyzvxvyvz.dat');
readNominalData(myPath);


clientSocket.on('connect', () => {
    console.log(`TCP Client connnected with mainServer`);
});




ioServer.on('connection', (socket) => {
    serverSockets.add(socket.id);
    console.log(`User ${socket.id} connected ${serverSockets.size} remaining`);

    socket.emit('nominalData', localNominalData);
    console.log('Nominal Data sent to end client');

    socket.on('getNominalData', (data) => {
        socket.emit('nominalData', localNominalData);
    });

    socket.on('disconnect', () => {
        serverSockets.delete(socket.id);
        console.log(`TCP Server: client ${socket.id} disconnected ${serverSockets.size} remaining`);
    });
});



clientSocket.on('disconnect', () => {
    console.log(`TCP Client socket disconnected retrying...`);
});
clientSocket.on('error', (error) => {
    console.log(`Error occurred\n ${error}`);
});

clientSocket.on('udpMessage', (data) => {
    console.log(`Data received from udp server ${data}`);
    ioServer.sockets.emit('tcpServerUdpData', data);
});

clientSocket.on('serverRealTimeData', (realTimeData) => {
    console.log(realTimeData.positionTime,realTimeData.x, realTimeData.y, realTimeData.z, realTimeData.sq);
    ioServer.sockets.emit('serverRealTimeData', realTimeData);
});




function readNominalData(pathToFile) {
    var file = fs.readFileSync(pathToFile).toString();
    var allRows = file.split(/\r\n|\r|\n/g);
    

    var totalx = [],totaly = [],totalz = [],totalsq = [];

    for (i of allRows) {
        j = i.split(" ")[1];
        totalx.push(Number(j));
        k = i.split(" ")[2];
        totaly.push(Number(k));
        l = i.split(" ")[3];
        totalz.push(Number(l));

        totalsq.push((Math.sqrt(j*j+k*k)));
    }

    localNominalData.totalx = totalx;
    localNominalData.totaly = totaly;
    localNominalData.totalz = totalz;
    localNominalData.totalsq = totalsq;
    console.log('Nominal read done');
}


var port = 7777;
expressServer.listen(port,[ip], ()=>{
    console.log(`TCP Server: start listening on http://${ip}:${port}`);
});