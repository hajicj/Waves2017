import os
from mutagen.mp3 import MP3


def generate_audio(generated_voice, best_background_sample, output_path):
    # lower_volume = "ffmpeg -y -i " + best_background_sample + " -af volume=-15dB audiodata/lowervolume.mp3"
    # print(lower_volume)

    normalize = "ffmpeg -y -i " + os.path.abspath(best_background_sample) + " -filter:a loudnorm " + os.path.abspath(
        "audiodata/normalize.mp3")

    overlay = "ffmpeg -y -i " + os.path.abspath(
        "audiodata/normalize.mp3") + " -i " + os.path.abspath(
        generated_voice) + " -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " + \
              os.path.abspath(output_path)

    print("Executing: " + normalize)
    os.system(normalize)
    print("Executing: " + overlay)
    os.system(overlay)

    audio = MP3("../audiodata/out.mp3")
    print(audio.info.length)


if __name__ == "__main__":
    generate_audio("voice1.mp3", "background.mp3", "test.mp3")
