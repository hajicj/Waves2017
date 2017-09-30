;(function(app){
    
    app.utils = {
        map: function(value, istart, istop, ostart, ostop) {
            return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));
        }
    };

})(app);