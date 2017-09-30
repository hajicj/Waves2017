const tweets = require("../trumpet.input/cache/tweets_realdonaldtrump.json");
const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 7000 });
const api = require("./api");


/*

x Step 1:
    Get Twitter Feed from trumpet.input
x Step 2:
    Post each Tweet to trumpet.mouthpiece (NLP)
    and get sentiment as json
Step 3:
    Post sentiment json to trumpet.valve
    and get final mp3
x Step 5:
    Post tweets+paths to final mp3s to trumpet.output
    
    
*/


var outputData = {
    tweets: [
        {
            "text": "Arianna hoff is whatever.....",
            "audio": "first.mp3",
            "user": "realdonaldtrump",
            "length": 10
        },
        {
            "text": "Hello, I am Daniel",
            "audio": "second.mp3",
            "user": "realdonaldtrump",
            "length": 2
        }
    ]
};

/*api("/api/analysis", 5000, {text: tweets[0].text, lang: "en"}, function(res){
    console.log(res);
});*/

/*tweets.forEach(function(tweet, index){
    console.log(tweet.text);
});*/


wss.on('connection', function connection(ws) {
    /*ws.on('message', function incoming(message) {
        console.log('received: %s', message);
    });*/
    
    ws.send(JSON.stringify(outputData));
});


