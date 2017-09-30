;(function(app){
    
    app.socket = {
        connection: new WebSocket('ws://localhost:7000'),
        onMessage: function(callback){
            this.connection.addEventListener('message', function (event) {
                callback(event.data);
            });
        }
    };
    
})(app);