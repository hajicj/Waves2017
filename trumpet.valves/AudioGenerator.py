import os
from mutagen.mp3 import MP3


def generate_audio(generated_voice, best_background_sample, output_path):
    lower_volume = "ffmpeg -y -i " + best_background_sample + " -af volume=-6dB /Users/phillip/web/waves/audiodata/normalize.mp3"
    # print(lower_volume)

    # normalize = "ffmpeg -y -i " + best_background_sample + " -filter:a loudnorm /Users/phillip/web/waves/audiodata/normalize.mp3"

    overlay = "ffmpeg -y -i /Users/phillip/web/waves/audiodata/normalize.mp3" + " -i " + generated_voice + " -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " + output_path

    os.system(lower_volume)
    os.system(overlay)


    audio = MP3(output_path)
    print(audio.info.length)


if __name__ == "__main__":
    generate_audio("voice1.mp3", "background.mp3", "test.mp3")
