from typing import List

import os

from TwitterSnippet import VoiceSnippet


def call_say_command(voice_snippets: List[VoiceSnippet]) -> str:
    print("SAY COMMAND")
    text = ""
    speaker = ""
    for i in range(len(voice_snippets)):
        voice_snippet = voice_snippets[i]
        text += voice_snippet.text + " "
        speaker = voice_snippet.speaker

    output_path = "/Users/phillip/web/waves/audiodata/say.aiff"
    say_command = 'say -v {0} "{1}" -o {2}'.format(speaker, str(text), output_path)
    print("SAY SAY SAY SAY SAYExecuting: " + say_command)
    os.system(say_command)

    return output_path

    #files = []
    #for i in range(len(voice_snippets)):
    #    files.append("-i /Users/phillip/web/waves/audiodata/{0}.aiff".format(i))
    #output_path = "/Users/phillip/web/waves/audiodata/output.mp3"
    #concatenate_command = "ffmpeg {0} -filter_complex '[0:0][1:0]concat=n=10:v=0:a=1[out]'  -map '[out]' -strict -2 -y ".format(
    #    str.join(" ", files) + " " + output_path)
    #print("Executing: " + concatenate_command)
    #
    #return output_path


if __name__ == "__main__":
    call_say_command([VoiceSnippet("Alex", "Hallo, ich bin Anna und rede wunderbares Deutsch. Oder auch nicht..."),
                      VoiceSnippet("Alex", "Nein")])
