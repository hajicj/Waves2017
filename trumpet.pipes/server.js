const api = require("./api");
const http = require("http");
const url = require("url");
const { exec, execSync } = require('child_process');


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


/*api("/api/analysis", 5000, {text: tweets[0].text, lang: "en"}, function(res){
    console.log(res);
});*/



http.createServer(function (req, res) {
    
  res.writeHead(200, {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*'
  });
  var parts = url.parse(req.url, true);
  var query = parts.query;
  
  /*if( ! /[^a-zA-Z0-9]/.test(query.username) ){
      console.log("invalid username");
      return;
  }*/
  
  exec('php ../trumpet.input/auth.php ' + query.username, {maxBuffer: 1024 * 50000}, (err, stdout, stderr) => {
      if (err) {
          console.log("err", err);
          return;
      }
      
      tweets = JSON.parse(stdout);
      
      var outputData = {
          tweets: []
      };
      
      tweets.forEach(function(tweet, index){
          
          // push each tweet to nlp
          
          // send response to trumpet.valves
          
          // prepare response to format:
          // console.log(tweet.id);
          // var length = execSync("python ../trumpet.valves/Valves.py --json '{}' --output ");
          
          outputData.tweets.push({
              "text": tweet.text,
              "audio": "first.mp3",
              "length": 10   
          });
          
      });
  
      res.end(JSON.stringify(outputData));
    
  });
  
}).listen(8000);

