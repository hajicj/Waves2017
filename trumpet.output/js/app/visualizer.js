;(function(app){
    
    
    app.visualizer = {
        audio: document.getElementById("audio"),
        ctx: null,
        src: null,
        analyser: null,
        bufferLength: null,
        dataArray: null,
        wavesurfer: null,
        $wave: null,
        frequencySplit: 32,
        loadAudio: function(file){
            
            this.audio.src = file;
            this.audio.load();
            
            if( ! this.ctx ){
                this.ctx = new AudioContext();
                this.src = this.ctx.createMediaElementSource(this.audio);
            
                this.analyser = this.ctx.createAnalyser();

                this.src.connect(this.analyser);
                this.analyser.connect(this.ctx.destination);

                this.analyser.fftSize = 256;

                this.bufferLength = this.analyser.frequencyBinCount;

                this.dataArray = new Uint8Array(this.bufferLength);
            }
            
            this.initWavesurfer();
        },
        initWavesurfer: function(){
            if( ! this.wavesurfer ){
                this.wavesurfer = WaveSurfer.create({
                    container: '#waveform',
                    waveColor: 'rgba(255,255,255,.4)',
                    progressColor: 'rgba(255,255,255,.8)',
                    audioContext: this.ctx,
                    cursorWidth: 0,
                    height: 400
                });
            }
            this.wavesurfer.load(this.audio.src);

            this.wavesurfer.on("ready", function(){
                this.wavesurfer.play();
                this.audio.play();

                this.$wave  = $("#waveform wave");
                this.renderFrame();
    
            }.bind(this));
        },
        renderFrame: function(){
            requestAnimationFrame(this.renderFrame.bind(this));
            this.analyser.getByteFrequencyData(this.dataArray);

            var lowSum = 0,
                highSum = 0;

            for (var i = 0; i < this.frequencySplit; i++){
                lowSum += this.dataArray[i];
            }
            for (var i = this.frequencySplit; i < this.bufferLength; i++){
                highSum += this.dataArray[i];
            }

            this.$wave.css("transform", "scale(1," + app.utils.map(highSum, 0, 8192, 1, 3) + ")");
        }
    };
    
})(app);