var WebSocketServer = require('websocket').server;
var http = require('http');

var server = http.createServer((req, res) => {
    console.log(`${new Date()} received request for ${req.url} `);
    res.writeHead(202);
    res.end('How are you');
});

var port = 8888;
server.listen(port, '127.0.0.1', () => {
    console.log(`Server is listening on http://localhost:${port}`);
    console.log(server.address().address);
});

wsServer = new WebSocketServer({
    httpServer: server,
    autoAcceptConnections: true
});

function originIsAllowed(origin) {
    return true;
}

wsServer.on('request', (request) => {
    if (!originIsAllowed(req.origin)) {
        request.reject();
        console.log(`${new Date()} Connection from origin ${request.origin}`);
    }

    var connection = request.accept('echo-protocol', request.origin);
    console.log(`${new Date()} connection accepted`);

    connection.on('message', (message) => {
        if (message.type === 'utf8') {
            console.log(`Received Message ${message.utf8Data}`);
            connection.sendUTF(`Server Response\n ${message.utf8Data}`);
        } else if (message.type === 'binary') {
            console.log(`Received Binary Message of ${message.binaryData.length} length`);
            connection.sendBytes(`Server Response\n ${message.binaryData}`);
        }
    });

    connection.on('close', (reasonCode, description) => {
        console.log(`${new Data()} peer ${connection.remoteAddress} disconnected`);
    });

});