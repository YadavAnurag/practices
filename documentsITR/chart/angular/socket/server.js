const express = require('express'),
      app = express(),
      server = require('http').createServer(app);
      io = require('socket.io')(server);



app.use(express.static(__dirname + '/dist')); 



io.on('connection', (socket)=>{
    socket.on('disconnect', ()=>{
        console.log(`User ${socket.id} disconnected`);
    });

    socket.on('clientMessage', (clientData)=>{
        console.log(clientData);
    });

    socket.emit('serverMessage', {data: 'this is my data'});

});


server.listen(8888, '127.0.0.1', ()=>{
    console.log('Visit http://127.0.0.1:8888 in your browser');
});

