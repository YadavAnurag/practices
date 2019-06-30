function handleHTTP(req, res) {
    if (req.method === 'GET') {
        if (/^\/\d+(?=$|[\/?#])/.test(req.url)) {
            req.addListener("end", function () {
                req.url = req.url.replace(/^\/(\d+).*$/, "/$1.html");
                static_files.serve(req, res);
            });
            req.resume();
        } else {
            res.writeHead(403);
            res.end("GTFO");

        }
    } else {
        res.writeHead(403);
        res.end("GTFO");
    }
}


function handleIO(socket) {


    console.log('client connected');

    var i = 0
    setInterval(() => {
        i += 1;
        socket.emit('serverMsg', "serverMsg" + i);
        console.log('serverMsg' + i);
    }, 50);

    function disconnect() {
        console.log('client disconnected');
    }

    socket.on('disconnect', disconnect);


}




var host = "localhost";
var port = 9007;

var http = require('http');
var httpServer = http.createServer(handleHTTP).listen(port);

var ASQ = require('asynquence');
var node_static = require('node-static');
var static_files = new node_static.Server(__dirname);
var io = require('socket.io').listen(httpServer);

io.on('connection', handleIO);
io.configure(function () {
    io.enable("browser client minification"); // send minified client
    io.enable("browser client etag"); // apply etag caching logic based on version number
    io.set("log level", 1); // reduce logging
    io.set("transports", [
        "websocket",
        "xhr-polling",
        "jsonp-polling"
    ]);
});