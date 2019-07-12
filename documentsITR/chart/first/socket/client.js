var PORT = 33333;
var HOST = '127.0.0.1';

var dgram = require('dgram');

i=0
var struct = {
    id : i
};

var message = Buffer.from('Message asdfasdfasdf');

var client = dgram.createSocket('udp4');




for(var i=0;i<6;i++){

    client.send(message, 0, message.length, PORT, HOST, function(err, bytes) {
        if (err) throw err;
        console.log('UDP message sent to ' + HOST +':'+ PORT);
    });
}

 