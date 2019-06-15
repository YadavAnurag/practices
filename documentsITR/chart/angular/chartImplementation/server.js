const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

app.use(express.static(__dirname + '/dist'));


let sockets = new Set();
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

  let i = 0;
  setInterval(() => {
    console.log(`server trying to send data to client`);

    data = {
      msg: 'server data sent to client',
      position: i
    }

    socket.emit('serverMessage', data);
    i += 1;
  }, 2000);
});



const port = 9898;
server.listen(port, '127.0.0.1', () => {
  console.log(`Visit http://127.0.0.1:${port} in your browser`);
});
