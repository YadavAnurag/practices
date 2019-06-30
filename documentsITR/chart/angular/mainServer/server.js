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
let id;
let i = 0;
let serverData = {
    x: 0,
    y: 0
}




io.on('connection', (socket) => {


    sockets.add(socket);
    console.log(`user ${socket.id} connected`);
    socket.on('disconnect', () => {
        sockets.delete(socket);
        console.log(`User ${socket.id} disconnected, remaining ${sockets.size}`);
    });

    socket.on('clientMessage', (clientData) => {
        console.log(clientData);
    });

    socket.on('getNominalData', clientData => {
        console.log(`${clientData}`);
        mypath = path.join(__dirname, '/dataFile/nominalData.txt');
        // sendNominalData(socket, './test_sim_ss_grh.dat');
        sendNominalData(socket, mypath);
    });

    socket.on('getRealTimeData', clientData => {
        console.log(`${clientData}`);
        mypath = path.join(__dirname + '/dataFile/realtimeData.txt');
        //console.log(path.join(__dirname, 'src/assets/dataFile/newdata.txt'));
        sendRealTimeData(socket, mypath);
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

	for(i of str){
		j = i.split(" ")[0];
		totalx.push(j);
		k = i.split(" ")[1];
		totaly.push(k)
	}
	var timer = setTimeout(function(){
		socket.emit("nominalData",{totalx, totaly});
		console.log("nominalData sent");
	},500);
}

function sendRealTimeData(socket, pathToFile) {
    console.log(`Server: start to send real time data`);
    const liner = new lineByLine(pathToFile);
    i = 0
    id = setInterval(() => {

        line = liner.next();

        if (line) {
            lineString = line.toString('ascii');
            serverData.x = lineString.split(" ")[0];
            serverData.y = lineString.split(" ")[1];

            for (const socket of sockets) {
                socket.emit('serverRealTimeData', serverData);
            }
            console.log(`server: ${i}th data sent from server x: ${serverData.x} y: ${serverData.y}`);
            i += 1;

        } else {
            clearInterval(id);
            socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
        }

    }, 50);
    i = 0;
    setInterval(() => {
        i += 1;
        socket.emit('serverRealTimeData', i.toString());
    }, 50);
}