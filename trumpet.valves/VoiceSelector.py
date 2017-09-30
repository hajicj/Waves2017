from typing import List, Tuple

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample, VoiceSnippet


def select_best_voice(twitter_snippets: List[TwitterSnippet]) -> List[VoiceSnippet]:
    voice_snippets = []
    last_word_of_previous_snippet = -1
    for twitter_snippet in twitter_snippets:
        best_speaker = None
        best_speaker_similarity = 0
        for voices in twitter_snippet.voices:
            if voices.similarity > best_speaker_similarity:
                best_speaker = voices.speaker
                best_speaker_similarity = voices.similarity

        first_word = max(last_word_of_previous_snippet + 1, twitter_snippet.start)
        number_of_skipped_words = first_word - twitter_snippet.start
        last_word_of_previous_snippet = twitter_snippet.end

        words = twitter_snippet.text.split(" ")
        for i in range(number_of_skipped_words):
            words.pop(0)

        voice_snippets.append(VoiceSnippet(best_speaker, str.join(" ", words)))

    return voice_snippets


if __name__ == "__main__":
    twitter_snippet1 = TwitterSnippet(0, 3, "This is a tweet", 0.9, [Keyword("tweet", 0.6, [0.5, 0.1, 0.2])],
                                      [Voice("Susanne", 0.7), Voice("Hannes", 0.6)],
                                      [BackgroundSample("aggressive_mood.mp3", 0.3)])
    twitter_snippet2 = TwitterSnippet(3, 6, "tweet from a guy", 0.9, [Keyword("guy", 0.6, [0.5, 0.1, 0.2])],
                                      [Voice("Susanne", 0.2), Voice("Hannes", 0.8)],
                                      [BackgroundSample("aggressive_mood.mp3", 0.3)])

    voice_snippets = select_best_voice([twitter_snippet1, twitter_snippet2])

    for voice_snippet in voice_snippets:
        print("{0}: {1}".format(voice_snippet.speaker, voice_snippet.text))
