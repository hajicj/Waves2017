import argparse

import AudioGenerator
import BackgroundSelector
import JsonReader
import VoiceGenerator
import VoiceSelector
from TwitterSnippet import TwitterSnippet, Voice, BackgroundSample, Keyword


def process_request(json: str, output_path: str) -> None:
    twitter_snippets = JsonReader.load_twitter_snippets_from_json(json)
    best_background_sample = BackgroundSelector.select_best_background(twitter_snippets)
    voice_snippets = VoiceSelector.select_best_voice(twitter_snippets)
    generated_voice = VoiceGenerator.call_say_command(voice_snippets)
    AudioGenerator.generate_audio(generated_voice, best_background_sample, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, default="Test.json",
                        help="The JSON content to be parsed that must contain a list of ")
    parser.add_argument("--output_path", type=str, default="Output.mp3",
                        help="Path to the mp3-file that will be generated")

    flags, unparsed = parser.parse_known_args()
    process_request(flags.json_path, flags.output_path)
