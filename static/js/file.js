function readFiles(path) {
    var fs = require("fs");
    fs.readdir(path, function(err, files) {
        if (err) {
            return console.error(err);
        }
        files.forEach(function(file) {
            console.log(file);
        });
    });
}

moudule.exports = readFiles