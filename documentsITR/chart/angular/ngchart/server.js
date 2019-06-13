const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server);

const PORT = 8080;

let timerId = null
let sockets = new Set();

app.use(express.static(__dirname+'/dist/ngchart'));

io.on('connection', socket=>{
    sockets.add(socket, ()=>{
        console.log(`New Socket ${socket.id} added`);
    });
    
    if(!timerId){
        startTimer();
    }
    
    socket.on('clientdata', (data)=>{
        console.log(data);
    });

    socket.on('disconnect', ()=>{
        console.log(`Socket ${socket.id} disconnected`);
        sockets.delete(socket);
        console.log('Remaining sockets: ${sockets.size}');
    });

});


const interval = 1000;
function startTimer(){
    timerId = setInterval(()=>{
        if(!sockets.size){
            clearInterval(timerId);
            timerId = null;
            console.log(`Timer Stopped`);
        }

        let value = (0.5-Math.random());
        for(const socket of sockets){
            console.log(`Emitting value: ${value} to ${socket.id}`);
            socket.emit('data',{data: value});
        }

    }, interval);
}


app.listen(PORT, '10.4.1.126', ()=>{
    console.log(`Server is listening on https://10.4.1.126:${PORT}`);
});