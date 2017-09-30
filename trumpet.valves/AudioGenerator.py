import os
from mutagen.mp3 import MP3


def generate_audio(generated_voice, best_background_sample, output_path):
    # lower_volume = "ffmpeg -y -i " + best_background_sample + " -af volume=-15dB audiodata/lowervolume.mp3"
    # print(lower_volume)

    normalize = "ffmpeg -y -i " + best_background_sample + " -filter:a loudnorm audiodata/normalize.mp3"
    # print(normalize)
    overlay = "ffmpeg -y -i audiodata/normalize.mp3 -i " + generated_voice + " -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " + output_path

    os.system(normalize)
    os.system(overlay)

    audio = MP3("../audiodata/out.mp3")
    print(audio.info.length)


    # print(overlay)


