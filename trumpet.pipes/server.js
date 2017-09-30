var tweets = require("../trumpet.input/cache/tweets_realdonaldtrump.json"),
    http = require("http");
    
/*

Step 1:
    Get Twitter Feed from trumpet.input
Step 2:
    Post each Tweet to trumpet.mouthpiece (NLP)
    and get sentiment as json
Step 3:
    Post sentiment json to trumpet.valve
    and get final mp3
Step 4:
    Post tweets+paths to mp3s to trumpet.output
    
    
*/

var api = function(path, port, data, callback){
    
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


api("/api/analysis", 5000, {text: tweets[0].text, lang: "en"}, function(res){
    console.log(res);
});

/*tweets.forEach(function(tweet, index){
    console.log(tweet.text);
});*/


