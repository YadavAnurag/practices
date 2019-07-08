const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const lineByLine = require('n-readlines/readlines');
const path = require('path');
var fs = require('fs');




app.use(express.static(__dirname + '/public'));



let sockets = new Set();
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
        myPath = path.join(__dirname, '/dataFile/test_sim_ss_txyzvxvyvz.dat');
        sendNominalData(socket, myPath);
    });

    socket.on('getRealTimeData', clientData => {
        console.log(`${clientData.msg}`);
        console.log(id);
    });

    setTimeout(function () {
        if (!id) {
            myPath = path.join(__dirname + '/dataFile/test_sim_ss_txyzvxvyvz.dat');
            sendRealTimeData(socket, myPath);
        }
    }, 6000);

});



const port = 9898;
server.listen(port, () => {
    console.log(`Visit http://127.0.0.1:${port} in your browser`);
});




function sendNominalData(socket, pathToFile) {
    var file = fs.readFileSync(pathToFile).toString();
    var allRows = file.split(/\r\n|\r|\n/g);
    

    var totalx = [],totaly = [],totalz = [],totalsq = [];

    for (i of allRows) {
        j = i.split(" ")[1];
        totalx.push(j);
        k = i.split(" ")[2];
        totaly.push(Number(k));
        l = i.split(" ")[3];
        totalz.push(Number(l));

        totalsq.push((Math.sqrt(j*j+k*k)).toString());
    }
    var timer = setTimeout(function () {
        socket.emit("nominalData", {
            totalx,
            totaly,
            totalz,
            totalsq
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

            serverData.positionTime = lineString.split(" ")[0];
            serverData.x = lineString.split(" ")[1];
            serverData.y = lineString.split(" ")[2];
            serverData.z = lineString.split(" ")[3];
            serverData.sq = Math.sqrt(serverData.x*serverData.x+serverData.y*serverData.y);

            socket.emit('serverRealTimeData', serverData);
            console.log(`server: ${i}th data sent from server positionTime: ${serverData.positionTime} x: ${serverData.x} y: ${serverData.y} z: ${serverData.z} sq: ${serverData.sq}`);
            i += 1;

        } else {
            clearInterval(id);
            socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
        }

    }, 200);

}