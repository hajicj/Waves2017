;(function(app){
    
    app.data = {};
    app.username = null;
    app.index = 0;
    
    app.init = function(){
        
        app.process(app.data.tweets[app.index]);
        
        /*
        var timeOffset = 0;
        
        app.data.tweets.forEach(function(tweet){
            
            setTimeout(function(){
                
                l = app.process(tweet);
                
            }, timeOffset * 1000);
            timeOffset += tweet.length;
        });*/
    };
    
    app.process = function(tweet){
        var l = app.visualizer.loadAudio("mp3/" + tweet.audio);
        $("#text").html(tweet.text);
        $("#user").html("@" + app.username + " says:");
        return l;
    };
    
    app.setUsername = function(username){
        this.username = username;
    };
    
    $(document).keypress(function(e){
        if( e.which == 32 ){
            app.index++;
            app.process(app.data.tweets[app.index]);
        }
    });
    
    $("#user-input").keypress(function(e) {
        if(e.which == 13) {
            app.setUsername($("#user-input").val());
            $("#intro").fadeOut(1000);
            $("#loader").fadeIn();
            
            $.get("http://localhost:8000/?username=" + app.username, function(data){
                app.data = data;
                $("#loader").fadeOut();
                app.init();
            }); 
        }
    });
    
})(app);




