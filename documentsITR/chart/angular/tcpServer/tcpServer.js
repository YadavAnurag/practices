var http = require('http');
var socket = require('socket.io');


var server = http.createServer((err, req, res)=>{
    if(err){
        console.log(`Server error: \n${err}`);
    }
    res.writeHead(200, {"Content-Type": "text/plain"});
    res.end("Hello TCP Server");
});



var PORT = 7777;

var io1 = socket.listen(server);
var io2 = socket.listen(server);

io1.attach(6000);
io2.attach(7000);












io1.on('connection', (socket)=>{
    console.log(`User ${socket.id} connected with io1`);
    socket.emit("serverMsg", "this is server");
    socket.on('myevent', (data)=>{
        console.log(data);
    });
});
io1.on('msg', (data)=>{
    console.log(data);
});



io2.on('connection', (socket)=>{
    console.log(`User ${socket.id} connected with io2`);
});

io2.on('msg', (data)=>{
    console.log(data);
});

server.listen(PORT);