const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

const lineByLine = require('n-readlines/readlines');
const liner = new lineByLine('./test_sim_ss_txyzvxvyvz.dat');




app.use(express.static(__dirname + '/dist'));





let sockets = new Set();


let id;
let i = 0;
let data = {
  first: Math.random(),
  second: i
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
    line = liner.next();
    if(line){

      lineString = line.toString('ascii');
      data.first = lineString.split(" ")[1];
      data.second = lineString.split(" ")[2];
      
      socket.emit('serverMessage', data);
      console.log('data sent from server', data);
      
    }else{
      clearInterval(id);
    }
  }, 5000);


});



const port = 9898;
server.listen(port, '127.0.0.1', () => {
  console.log(`Visit http://127.0.0.1:${port} in your browser`);
});
