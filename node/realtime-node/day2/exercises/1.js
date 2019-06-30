#!/usr/bin/env node

function printHelp() {
    console.log("1.js");
    console.log("usage: ");
    console.log("--help                 print this help");
    console.log("--file={NAME}          read the file of {NAME} and output it\n");
}



var args = require('minimist')(process.argv.slice(2));


if (args.help || !args.file) {
    printHelp();
    process.exit(1);
}

var hello = require('./helloworld2.js');
hello.say(args.file, (err, contents) => {
    console.log(contents.toString());
});