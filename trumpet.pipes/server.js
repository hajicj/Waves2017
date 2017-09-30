const tweets = require("../trumpet.input/cache/tweets_realdonaldtrump.json");
const api = require("./api");
const http = require("http");
const url = require("url");


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


http.createServer(function (req, res) {
    
  res.writeHead(200, {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
  });
  var parts = url.parse(req.url, true);
  var query = parts.query;
  
  // query.username  
  
  res.end(JSON.stringify(outputData));
  
}).listen(8000);

