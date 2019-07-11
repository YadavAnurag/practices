const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const lineByLine = require('n-readlines/readlines');
const path = require('path');
var fs = require('fs');


app.use(express.static(__dirname + '/public'));








let sockets = [];
let id = null;
let i = 0,j = 0,k = 0;
let serverData = {
    positionTime: 0,
    x: 0,
    y: 0,
    z: 0,
    sq: 0,
}




io.on('connection', (socket) => {

    sockets.push(socket);
    console.log(`user ${socket.id} connected`);


    socket.on('disconnect', () => {
        sockets.pop(socket);
        console.log(`User ${socket.id} disconnected, remaining ${sockets.size}`);
    });


    // setTimeout(function () {
    //     if (!id) {
    //         myPath = path.join(__dirname + '/dataFile/test_sim_ss_txyzvxvyvz.dat');
    //         sendRealTimeData(socket, myPath);
    //     }
    // }, 6000);

});



const port = 9898;
server.listen(port, () => {
    console.log(`Visit http://127.0.0.1:${port} in your browser`);
});




function sendRealTimeData(socket, pathToFile) {
    console.log(`mainServer: start to send real time data`);
    const liner = new lineByLine(pathToFile);
    i = 0
    id = setInterval(() => {

        line = liner.next();

        if (line) {
            lineString = line.toString('ascii');

            serverData.positionTime = Number(lineString.split(" ")[0]);
            serverData.x = Number(lineString.split(" ")[1]);
            serverData.y = Number(lineString.split(" ")[2]);
            serverData.z = Number(lineString.split(" ")[3]);
            serverData.sq = Number(Math.sqrt(serverData.x*serverData.x+serverData.y*serverData.y));

            socket.emit('serverRealTimeData', serverData);
            console.log(`server: ${i}th data sent from server positionTime: ${serverData.positionTime} x: ${serverData.x} y: ${serverData.y} z: ${serverData.z} sq: ${serverData.sq}`);
            i += 1;

        } else {
            clearInterval(id);
            socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
        }

    }, 200);

}
// UDP socket
var PORT = 33333;
var HOST = '127.0.0.1';

var dgram = require('dgram');
var udpServer = dgram.createSocket('udp4');

udpServer.on('listening', function() {
    var address = udpServer.address();
    console.log('UDP Server listening on ' + address.address + ':' + address.port);
});

udpServer.on('message', function(message, remote) {

    sockets[0].emit("udpMessage", message);
    console.log(remote.address + ':' + remote.port +' - ' + message);
});

udpServer.bind(PORT, HOST);