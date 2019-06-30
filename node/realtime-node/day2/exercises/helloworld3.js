function readFile(filename) {
    return ASQ((done) => {
        var stream = fs.createReadStream(filename);
        var contents = "";

        stream.pipe(fs.createWriteStream(filename + ".backup").on("end", () => {
            //do something
        }))

        stream.on('data', (chunk) => {
            console.log('data');
            contents += chunk;
        });
        stream.on('end', () => {
            done(contents);
        });
    });
}

function delayMsg(done, contents) {
    setTimeout(() => {
        done(contents);
    }, 1000);
}

function say(filename) {
    return readFile(filename)
        .then(delayMsg);
}



var fs = require('fs');
var ASQ = require('asynquence');
require('asynquence-contrib');


module.exports.say = say;