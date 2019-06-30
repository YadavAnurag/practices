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


var host = "localhost";
var port = 9007;

var http = require('http');
var httpServer = http.createServer(handleHTTP).listen(port);

var ASQ = require('asynquence');
var node_static = require('node-static');
var static_files = new node_static.Server(__dirname);
var io = require('socket.io');
io.listen(httpServer);