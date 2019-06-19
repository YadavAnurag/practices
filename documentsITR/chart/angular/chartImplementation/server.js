const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);
const lineByLine = require('n-readlines/readlines');

app.use(express.static(__dirname + '/dist'));


app.get('/file', (req, res)=>{
  res.download(__dirname+ '/dataFile/mydata.txt');
  console.log(__dirname+ '/dataFile/mydata.txt');
});


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
    sendNominalData(socket, './test_sim_ss_grh.dat');
  });

  socket.on('getRealTimeData', clientData =>{
    console.log(`${clientData}`);
    sendRealTimeData(socket, './test_sim_ss_grh.dat');
  });


  
});



const port = 9898;
server.listen(port, () => {
  console.log(`Visit http://127.0.0.1:${port} in your browser`);
});




function sendNominalData(socket, pathToFile){
  console.log(`Server start to send nominal data`);
  const liner = new lineByLine(pathToFile);
  i=0
  id = setInterval(()=>{
    
    line = liner.next();

    if(line){
      lineString = line.toString('ascii');
      serverData.x = lineString.split(" ")[0];
      serverData.y = lineString.split(" ")[1];
      
      socket.emit('serverNominalData', serverData);
      console.log(`${i}th data sent from server x: ${serverData.x} y: ${serverData.y}`);
      i+=1;
      
    }else{
      clearInterval(id);
      socket.emit('serverNominalDataCompleted', 'nominal data has been sent');
    }

  }, 2);
}

function sendRealTimeData(socket, pathToFile){
  console.log(`Server: start to send real time data`);
  const liner = new lineByLine(pathToFile);
  i=0
  id = setInterval(()=>{
    
    line = liner.next();

    if(line){
      lineString = line.toString('ascii');
      serverData.x = lineString.split(" ")[0];
      serverData.y = lineString.split(" ")[1];
      
      socket.emit('serverRealTimeData', serverData);
      console.log(`server: ${i}th data sent from server x: ${serverData.x} y: ${serverData.y}`);
      i+=1;
      
    }else{
      clearInterval(id);
      socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
    }

  }, 50);
}