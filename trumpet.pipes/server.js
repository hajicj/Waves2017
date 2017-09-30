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
          var lengthSeconds = execSync('python3 ../trumpet.valves/Valves.py --json \' [   {     "py/object": "__main__.TwitterSnippet",     "start": 0,     "end": 3,     "text": "This is a tweet",     "relevance": 0.5,     "keywords": [       {         "py/object": "__main__.Keyword",         "word": "tweet",         "relevance": 0.9,         "word2vec": [           0.1,           0.2,           0.5,           0.6         ]       }     ],     "background_samples": [       {         "py/object": "__main__.BackgroundSample",         "filename": "business-freedom_gjrmyusd.mp3",         "similarity": 0.665       },       {         "py/object": "__main__.BackgroundSample",         "filename": "cheerful-morning-full_m1txke4_.mp3",         "similarity": 0.567       }     ],     "voices": [       {         "py/object": "__main__.Voice",         "speaker": "Stephanie",         "similarity": 0.876       },       {         "py/object": "__main__.Voice",         "speaker": "Horst",         "similarity": 0.967       }     ]   },   {     "py/object": "__main__.TwitterSnippet",     "start": 3,     "end": 5,     "text": "of some guy",     "relevance": 0.7,     "keywords": [       {         "py/object": "__main__.Keyword",         "word": "guy",         "relevance": 0.9,         "word2vec": [           0.1,           0.3,           0.5,           0.6         ]       }     ],     "background_samples": [       {         "py/object": "__main__.BackgroundSample",         "filename": "business-freedom_gjrmyusd.mp3",         "similarity": 0.665       },       {         "py/object": "__main__.BackgroundSample",         "filename": "cheerful-morning-full_m1txke4_.mp3",         "similarity": 0.567       }     ],     "voices": [       {         "py/object": "__main__.Voice",         "speaker": "Stephanie",         "similarity": 0.876       },       {         "py/object": "__main__.Voice",         "speaker": "Horst",         "similarity": 0.967       }     ]   } ]\' --output_path ../trumpet.output/mp3/' + tweet.id + ".mp3");
          
          outputData.tweets.push({
              "text": tweet.text,
              "audio": "first.mp3",
              "length": 10   
          });
          
      });
  
      res.end(JSON.stringify(outputData));
    
  });
  
}).listen(8000);

