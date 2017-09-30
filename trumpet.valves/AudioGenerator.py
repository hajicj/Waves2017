import os


def generate_audio(generated_voice, best_background_sample, output_path):


    lower_volume = "ffmpeg -i " + best_background_sample + " -af volume=-15dB " + output_path
    overlay = "ffmpeg -i " + output_path + " -i " + generated_voice + "-filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " + output_path

    os.system(lower_volume)
    os.system(overlay)




if __name__ == '__main__':
    generate_audio("audiodata/testpeaker.aiff", "audiodata/test_sample.mp3", "/out.mp3")
