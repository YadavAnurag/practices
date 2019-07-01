var io = require('socket.io-client');

var socket1 = io('http://127.0.0.1:6000');

socket1.on('err', (err)=>{
    if(err){
        console.log(err);
    }
});


socket1.on('connect', ()=>{
    console.log();
    console.log('im connected with 1st');
});



var socket2 = io('http://127.0.0.1:7000');


socket2.on('err', (err)=>{
    if(err){
        console.log(err);
    }
});


socket2.on('connect', ()=>{
    console.log('im connected with 2nd');
});


setTimeout(()=>{
    console.log('fired');
    socket1.emit('myevent', 'first');
}, 3000);

// socket2.emit('msg', 'second');

socket1.on('serverMsg', (data)=>{
    console.log(data);
});