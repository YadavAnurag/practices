const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

const lineByLine = require('n-readlines/readlines');
//const liner = new lineByLine('./test_sim_ss_txyzvxvyvz.dat');
const liner = new lineByLine('./cdp.txt');




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

  id = setInterval(()=>{
    i=0
    line = liner.next();
    if(line){

      lineString = line.toString('ascii');
      serverData.x = lineString.split(" ")[2];
      serverData.y = lineString.split(" ")[1];
      
      socket.emit('serverMessage', serverData);
      console.log('data sent from server', serverData);
      i+=1;
      
    }else{
      clearInterval(id);
    }
  }, 2000);
});



const port = 9898;
server.listen(port, '127.0.0.1', () => {
  console.log(`Visit http://127.0.0.1:${port} in your browser`);
});
