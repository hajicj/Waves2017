
var audio = document.getElementById("audio");

audio.src = "demo.mp3";
audio.load();
var context = new AudioContext();
var src = context.createMediaElementSource(audio);
var analyser = context.createAnalyser();

src.connect(analyser);
analyser.connect(context.destination);

analyser.fftSize = 256;

var bufferLength = analyser.frequencyBinCount;

var dataArray = new Uint8Array(bufferLength);

// i => current, o => target
function map(value, istart, istop, ostart, ostop) {
      return ostart + (ostop - ostart) * ((value - istart) / (istop - istart));
}


var wavesurfer = WaveSurfer.create({
    container: '#waveform',
    waveColor: 'red',
    progressColor: 'purple',
    audioContext: context,
    cursorWidth: 0,
    height: 400
});
wavesurfer.load('demo.mp3');

wavesurfer.on("ready", function(){
    wavesurfer.play();
    audio.play();

    var $wave  = $("#waveform wave"),
        split = 32;

    function renderFrame() {
        requestAnimationFrame(renderFrame);
        analyser.getByteFrequencyData(dataArray);

        var lowSum = 0,
            highSum = 0;
     
        for (var i = 0; i < split; i++){
            lowSum += dataArray[i];
        }
        for (var i = split; i < bufferLength; i++){
            highSum += dataArray[i];
        }
    
        $wave.css("transform", "scale(1," + map(highSum, 0, 8192, 1, 3) + ")");
    }
    renderFrame();
    
});
