var tweets = require("../twitter/cache/tweets_realdonaldtrump.json");

tweets.forEach(function(tweet, index){
    console.log(tweet.text);
});