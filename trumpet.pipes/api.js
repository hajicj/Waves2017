const http = require("http");

module.exports = function(path, port, data, callback){
    
    var headers = {
        'Content-Type' : 'application/json',
        'Content-Length' : Buffer.byteLength(JSON.stringify(data), 'utf8')
    };
    
    var options = {
        host: "localhost",
        port: port,
        path: path,
        method: 'POST',
        headers: headers
    };

    var req = http.request(options, function(res) {
        res.setEncoding('utf8');
        res.on('data', function (chunk) {
            callback(chunk);
        });
    });
    
    req.write(JSON.stringify(data));
    req.end();
};