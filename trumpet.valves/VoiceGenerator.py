from typing import List

import os

from TwitterSnippet import VoiceSnippet


def call_say_command(voice_snippets: List[VoiceSnippet]) -> str:
    for i in range(len(voice_snippets)):
        voice_snippet = voice_snippets[i]
        say_command = 'say -v {0} -r 100 "{1}" -o '.format(voice_snippet.speaker,
                                                           voice_snippet.text) + os.path.abspath(
            "audiodata/{0}.aiff".format(i))
    print("Executing: " + say_command)
    os.system(say_command)

    files = []
    for i in range(len(voice_snippets)):
        files.append("-i " + os.path.abspath("audiodata/{0}.aiff".format(i)))
    output_path = os.path.abspath("audiodata/output.mp3")
    concatenate_command = "ffmpeg {0} -filter_complex '[0:0][1:0]concat=n=10:v=0:a=1[out]'  -map '[out]' -strict -2 -y ".format(
        str.join(" ", files) + " " + output_path)
    print("Executing: " + concatenate_command)

    return output_path


if __name__ == "__main__":
    call_say_command([VoiceSnippet("Anna", "Hallo, ich bin Anna und rede wunderbares Deutsch. Oder auch nicht..."),
                      VoiceSnippet("Hannes", "Nein")])
