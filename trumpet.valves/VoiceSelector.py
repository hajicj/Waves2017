from typing import List, Tuple

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample, VoiceSnippet


def select_best_voice(twitter_snippets: List[TwitterSnippet]) -> List[VoiceSnippet]:
    pass


if __name__ == "__main__":
    twitter_snippet1 = TwitterSnippet(0, 3, "This is a tweet", 0.9, [Keyword("tweet", 0.6, [0.5, 0.1, 0.2])],
                                     [Voice("Susanne", 0.7), Voice("Hannes", 0.6)],
                                     [BackgroundSample("aggressive_mood.mp3", 0.3)])
    twitter_snippet2 = TwitterSnippet(3, 6, "tweet from a guy", 0.9, [Keyword("guy", 0.6, [0.5, 0.1, 0.2])],
                                     [Voice("Susanne", 0.2), Voice("Hannes", 0.8)],
                                     [BackgroundSample("aggressive_mood.mp3", 0.3)])

    voices = select_best_voice([twitter_snippet1, twitter_snippet2])

    print("Best background sample: {0}".format(voices))
