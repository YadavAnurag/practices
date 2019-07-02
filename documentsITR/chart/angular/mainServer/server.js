const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const lineByLine = require('n-readlines/readlines');
const path = require('path');
var fs = require('fs');
var file = fs.readFileSync('dataFile/nominalData.txt').toString();



app.use(express.static(__dirname + '/dist'));



let sockets = new Set();
let id = null;
let i = 0;
let serverData = {
    x: 0,
    y: 0,
    position: 0
}




io.on('connection', (socket) => {


    sockets.add(socket);
    console.log(`user ${socket.id} connected`);

    socket.on('stopRealTimeData', () => {
        if (id) {
            clearInterval(id);
            console.log('Realtime Data sending stopped');
        }
    });

    socket.on('disconnect', () => {
        sockets.delete(socket);
        if (!sockets.size && id) {
            clearInterval(id);
        }
        console.log(`User ${socket.id} disconnected, remaining ${sockets.size}`);
    });

    socket.on('clientMessage', (clientData) => {
        console.log(clientData.msg);
    });

    socket.on('getNominalData', clientData => {
        console.log(`${clientData.msg}`);
        mypath = path.join(__dirname, '/dataFile/nominalData.txt');
        sendNominalData(socket, mypath);
    });

    socket.on('getRealTimeData', clientData => {
        console.log(`${clientData.msg}`);
        mypath = path.join(__dirname + '/dataFile/realtimeData.txt');
        console.log(id);
        if (!id) {
            sendRealTimeData(socket, mypath);
        }
    });

});



const port = 9898;
server.listen(port, () => {
    console.log(`Visit http://127.0.0.1:${port} in your browser`);
});




function sendNominalData(socket, pathToFile) {
    var str = file.split(/\r\n|\r|\n/g);

    var totalx = [];
    var totaly = [];

    for (i of str) {
        j = i.split(" ")[0];
        totalx.push(j);
        k = i.split(" ")[1];
        totaly.push(k)
    }
    var timer = setTimeout(function () {
        socket.emit("nominalData", {
            totalx,
            totaly
        });
        console.log("mainServer: nominalData sent");
    }, 2000);
}

function sendRealTimeData(socket, pathToFile) {
    console.log(`mainServer: start to send real time data`);
    const liner = new lineByLine(pathToFile);
    i = 0
    id = setInterval(() => {

        line = liner.next();

        if (line) {
            lineString = line.toString('ascii');
            serverData.x = lineString.split(" ")[0];
            serverData.y = lineString.split(" ")[1];
            serverData.position = i;
            for (const socket of sockets) {
                socket.emit('serverRealTimeData', serverData);
            }
            console.log(`server: ${i}th data sent from server x: ${serverData.x} y: ${serverData.position}`);
            i += 1;

        } else {
            clearInterval(id);
            socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
        }

    }, 100);

}