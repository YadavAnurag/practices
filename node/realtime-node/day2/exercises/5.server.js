var ASQ = require('asynquence');


function handleHTTP(req, res) {
    if (req.method === 'GET') {
        if (req.url === "/") {
            res.writeHead(200, {
                contentType: "text/plain"
            });

            ASQ((done) => {
                    setTimeout(() => {
                        done(Math.random());
                    }, 1000);
                })
                .then((done, num) => {
                    setTimeout(() => {
                        done('Hello World' + num);
                    },1000);
                })
                .val((msg) => {
                    res.end(msg);
                });

            // setTimeout(() => {
            //     var num = Math.random();
            //     setTimeout(() => {
            //         res.end('Hello World' + num);
            //     });
            // }, 1000);

            // res.write("Hello World");
            // res.end(Math.random().toString());
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