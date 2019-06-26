function handleHTTP(req,res) {
	if (req.method == "GET") {
		if (/^\/\d+(?=$|[\/?#])/.test(req.url)) {
			req.addListener("end",function(){
				req.url = req.url.replace(/^\/(\d+).*$/,"/$1.html");
				static_files.serve(req,res);
			});
			req.resume();
		}
		else {
			res.writeHead(403);
			res.end();
		}
	}
	else {
		res.writeHead(403);
		res.end();
	}
}

var path = require('path');
var fs = require('fs');
var file = fs.readFileSync('test_sim_ss_grh.dat').toString();
var lineByLine = require('n-readlines/readlines');

// var lineReader = require('readline').createInterface({
// 	input: require('fs').createReadStream('./test_sim_ss_grh.dat')
//   });
  
  


function connection(socket) {
	console.log('Client Connected');
	function disconnect() {
		console.log("Client disconnected!");
		clearInterval(timer);
	}

	socket.on("disconnect",disconnect);

	var row = file.split(" \n");
	
	totalx = [];
	totaly = [];
	for(i of row) {
		totalx.push(i.split(" ")[0]);
		totaly.push(Number(i.split(" ")[1]));
		
	}
	console.log(totalx.length, totaly.length);
	

	console.log(row.length);
	var timer = setTimeout(function(){
		socket.emit("nominalData",{totalx, totaly});
	},500);

	// socket.on("realTimeData", ()=>{

	// 	var timer = setInterval(function(){
	// 		lineReader.on('line', function (line) {
				
	// 		  });
	// 		socket.emit("serverRealTimeData",{x, y});
	// 	},1000);
	// });

	socket.on('getRealTimeData', () => {
		
		mypath = path.join(__dirname+'/test_sim_ss_grh.dat');
		//console.log(path.join(__dirname, 'src/assets/dataFile/newdata.txt'));
		sendRealTimeData(socket, mypath);
	  });


	var timer = setTimeout(function(){
		socket.emit("nominalData",{totalx, totaly});
	},500);
}




var
	http = require("http"),
	httpserv = http.createServer(handleHTTP),

	port = 8006,
	host = "127.0.0.1",

	ASQ = require("asynquence"),
	node_static = require("node-static"),
	static_files = new node_static.Server(__dirname),

	io = require("socket.io").listen(httpserv)
;

require("asynquence-contrib");

httpserv.listen(port, host);

io.on("connection",connection);
// configure socket.io
io.configure(function(){
	io.enable("browser client minification"); // send minified client
	io.enable("browser client etag"); // apply etag caching logic based on version number
	io.set("log level", 1); // reduce logging
	io.set("transports", [
		"websocket",
		"xhr-polling",
		"jsonp-polling"
	]);
});

serverData = {
	x:0,y:0
}

function sendRealTimeData(socket, pathToFile) {
	console.log(`Server: start to send real time data`);
	const liner = new lineByLine(pathToFile);
	i = 0
	id = setInterval(() => {
  
	  line = liner.next();
  
	  if (line) {
		lineString = line.toString('ascii');
		serverData.x = lineString.split(" ")[0];
		serverData.y = lineString.split(" ")[1];
  
		  socket.emit('serverRealTimeData', serverData);
		console.log(`server: ${i}th data sent from server x: ${serverData.x} y: ${serverData.y}`);
		i += 1;
  
	  } else {
		clearInterval(id);
		socket.emit('serverRealTimeDataCompleted', 'real time data has been sent');
	  }
  
	}, 1000);
	// i=0;
	// setInterval(()=>{
	//   i+=1;
	//   socket.emit('serverRealTimeData', i.toString());
	// },50);
  }