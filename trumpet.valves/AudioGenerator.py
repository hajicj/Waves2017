import os


def generate_audio(voice_path, background_path):

    output_path = ""

    lower_volume = "ffmpeg -i " + background_path + " -af volume=-15dB " + output_path
    overlay = "ffmpeg -i " + output_path + " -i " + voice_path + "-filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 output.mp3"

    os.system(lower_volume)
    os.system(overlay)


    return output_path




if __name__ == '__main__':
    output = generate_audio("audiodata/testpeaker.aiff", "audiodata/test_sample.mp3")

    print("Output: " + output)