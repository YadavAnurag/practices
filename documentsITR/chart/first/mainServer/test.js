var fs = require('fs');
var path = require('path');

var file = fs.readFileSync('dataFile/newdata.txt').toString();

var str = file.split(/\r\n|\r|\n/g);

var totalx = [];
var totaly = [];

for(i of str){
	j = i.split(" ")[0];
	totalx.push(j);
	k = i.split(" ")[1];
	totaly.push(j)
}
console.log(totalx);

console.log(totaly.length, totalx.length);
