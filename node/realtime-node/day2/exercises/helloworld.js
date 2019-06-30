function say(filename, cb) {
    return contents = fs.readFile(filename, function (err, contents) {
        if (err) {
            cb(err);
        } else {
            setTimeout(() => {
                cb(null, contents);
            }, 1000);
        }
    });
}

var fs = require('fs');


module.exports.say = say;