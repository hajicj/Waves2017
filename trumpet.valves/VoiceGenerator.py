from typing import List

from TwitterSnippet import VoiceSnippet


def call_say_command(voice_snippets: List[VoiceSnippet]) -> str:
    # TODO Call console: say -v Alex -r 100 "blablabla." -o audiodata/out-xxx.aiff
    return "speech.aiff"


if __name__ == "__main__":
    call_say_command([VoiceSnippet("Anna", "Hallo, ich bin Anna und rede wunderbares Deutsch. Oder auch nicht..."),
                      VoiceSnippet("Hannes", "Nein")])
