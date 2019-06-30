function handleHTTP(req, res) {
    if (req.method === 'GET') {
        if (req.url === "/") {
            res.writeHead(200, {
                contentType: "text/plain"
            });
            res.write("Hello World");
            res.end(Math.random().toString());
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