;(function(app){
    
    app.data = {};
    
    app.init = function(){
        
        var timeOffset = 0;
        
        app.data.tweets.forEach(function(tweet){
            setTimeout(function(){
                
                app.process(tweet);
                
            }, timeOffset * 1000);
            timeOffset += tweet.length;
        });
    };
    
    app.process = function(tweet){
        app.visualizer.loadAudio("mp3/" + tweet.audio);
        $("#text").html(tweet.text);
        $("#user").html("@" + tweet.user + " says:");
    };
    
    app.socket.onMessage(function(data){
        app.data = JSON.parse(data);
        
        app.init();
    });
    
    //app.visualizer.loadAudio("mp3/demo.mp3");
    
})(app);




