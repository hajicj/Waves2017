import os
from mutagen.mp3 import MP3


def generate_audio(generated_voice: str, best_background_sample: str, output_path: str,
                   audiodata_path: str) -> float:

    normalized_file_path = os.path.join(audiodata_path, "normalize.mp3")

    # Make the background sample quieter
    lower_volume = "ffmpeg -y -i " + best_background_sample + " -af volume=-6dB " + normalized_file_path
    print("Executing: " + lower_volume)
    os.system(lower_volume)

    # Alternatively we could normalize the background sample
    # normalize = "ffmpeg -y -i " + best_background_sample + " -filter:a loudnorm " + normalized_file_path
    # print("Executing: " + normalize)
    # os.system(normalize)

    overlay = "ffmpeg -y -i " + normalized_file_path + " -i " + generated_voice + " -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " + output_path
    print("Executing: " + overlay)
    os.system(overlay)

    audio_file_length_in_seconds = MP3(output_path).info.length
    return audio_file_length_in_seconds

if __name__ == "__main__":
    generate_audio("voice1.mp3", "background.mp3", "test.mp3", "../audiodata")
