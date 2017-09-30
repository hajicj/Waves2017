from typing import List


def call_say_command(voice_snippets: List[VoiceSnippet]) -> str:
    # TODO Call console: say -v Alex -r 100 "blablabla." -o audiodata/out-xxx.aiff

    for i in range(len(voice_snippets)):
        voice_snippet = voice_snippets[i]

        saycommand = 'say -v {0} -r 100 "{1}" -o audiodata/{2}.aiff'.format(voice_snippet)


if __name__ == "__main__":
    call_say_command([VoiceSnippet("Anna", "Hallo, ich bin Anna und rede wunderbares Deutsch. Oder auch nicht..."),
                      VoiceSnippet("Hannes", "Nein")])




    # ffmpeg -i 1.mp4 -i 2.mp4 -i 3.mp4 -i 4.mp4 -i 5.mp4 -i 6.mp4 -i 7.mp4 -i 8.mp4 -i 9.mp4 -i 10.mp4  -filter_complex '[0:0][1:0]concat=n=10:v=0:a=1[out]'  -map '[out]' -strict -2 -y 10_final.mp4
