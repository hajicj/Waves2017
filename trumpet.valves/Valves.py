import argparse

import BackgroundSelector
import JsonReader
import VoiceGenerator
import VoiceSelector
from TwitterSnippet import TwitterSnippet, Voice, BackgroundSample, Keyword


def process_request(json_path: str, output_path: str) -> None:
    twitter_snippets = JsonReader.load_twitter_snippets_from_json(json_path)
    best_background_sample = BackgroundSelector.select_best_background(twitter_snippets)
    voice_snippets = VoiceSelector.select_best_voice(twitter_snippets)
    generated_voice = VoiceGenerator.call_say_command(voice_snippets)
    # generated_sample = AudioGenerator.generate_audio(generated_voice, best_background_sample)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json_path", type=str, default="Test.json",
                        help="Path to the json-file that contains the description")
    parser.add_argument("--output_path", type=str, default="Output.mp3",
                        help="Path to the mp3-file that will be generated")

    flags, unparsed = parser.parse_known_args()
    process_request(flags.json_path, flags.output_path)
