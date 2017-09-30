;(function(app){
    
    app.data = {};
    app.username = null;
    
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
        $("#user").html("@" + app.username + " says:");
    };
    
    app.setUsername = function(username){
        this.username = username;
    };
    
    $("#user-input").keypress(function(e) {
        if(e.which == 13) {
            app.setUsername($("#user-input").val());
            $("#intro").fadeOut(1000);
            
            $.get("http://localhost:8000/?username=" + app.username, function(data){
                app.data = data;
                
                setTimeout(function(){
                    app.init();
                }, 1000);
            }); 
        }
    });
    
})(app);




