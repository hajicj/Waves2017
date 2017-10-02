import argparse
import base64

import AudioGenerator
import BackgroundSelector
import JsonReader
import VoiceGenerator
import VoiceSelector


def select_samples_and_generate_final_audio(json: str, output_path: str, audiodata_path: str) -> None:
    twitter_snippets = JsonReader.load_twitter_snippets_from_json(json)
    best_background_sample = BackgroundSelector.select_best_background(twitter_snippets, audiodata_path)
    voice_snippets = VoiceSelector.select_best_voice(twitter_snippets)
    generated_voice = VoiceGenerator.call_say_command(voice_snippets, audiodata_path)
    AudioGenerator.generate_audio(generated_voice, best_background_sample, output_path, audiodata_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=str, default="Test.json",
                        help="The JSON content to be parsed that must contain a list of Twitter snippets")
    parser.add_argument("--output_path", type=str, default="Output.mp3",
                        help="Path to the mp3-file that will be generated")
    parser.add_argument("--audiodata_path", type=str, default="/Users/phillip/web/waves/audiodata",
                        help="Absolute path to the directory that contains the background music audio samples"
                             "that are referenced from the NLP-component.")

    flags, unparsed = parser.parse_known_args()
    select_samples_and_generate_final_audio(flags.json, flags.output_path, flags.audiodata_path)
