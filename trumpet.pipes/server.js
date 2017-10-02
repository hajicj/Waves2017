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
          var t = tweet.text,
              x = tweet.id;
          
          var ttext = new Buffer(t).toString('base64');
          
          var files = [
            "dramatic-action-score_g1rgqeno.mp3",
              "bizets-habanera_fylc2hsd.mp3",
              "happy-groovy-power-pop_mjvh9neo.mp3"
          ];
          
          var file = files[Math.floor(Math.random()*files.length)];
          
          var fixedJson = '[{"py/object": "__main__.TwitterSnippet","start": 0,"end": 3,"text": "' + ttext + '","relevance": 0.5,"keywords": [{"py/object": "__main__.Keyword","word": "tweet","relevance": 0.9,"word2vec": [0.1,0.2,0.5,0.6]}],"background_samples": [{"py/object": "__main__.BackgroundSample","filename": "' + file + '","similarity": 0.665}],"voices": [{"py/object": "__main__.Voice","speaker": "Daniel","similarity": 0.876}]}]';
          
          var cmd = '/usr/local/bin/python3 ../trumpet.valves/Valves.py --json \'' + fixedJson + '\' --output_path /Users/phillip/web/waves/trumpet.output/mp3/' + x + ".mp3" + " --audiodata_path /Users/phillip/web/waves/audiodata";
          
          console.log(cmd);
          execSync(cmd);
          
          outputData.tweets.push({
              "text": t,
              "audio": x + ".mp3"
          });
          
      });
  
      res.end(JSON.stringify(outputData));
    
  });
  
}).listen(8000);

