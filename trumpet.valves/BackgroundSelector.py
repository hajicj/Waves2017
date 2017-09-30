from typing import List

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample


def select_best_background(twitter_snippets: List[TwitterSnippet]) -> str:
    best_sample = None
    highest_similarity = 0
    for twitter_snippet in twitter_snippets:
        for background_sample in twitter_snippet.background_samples:
            if background_sample.similarity > highest_similarity:
                best_sample = background_sample.filename
                highest_similarity = background_sample.similarity

    return "/Users/phillip/web/waves/audiodata/" + best_sample


if __name__ == "__main__":
    twitter_snippet = TwitterSnippet(0, 3, "This is a tweet", 0.9, [Keyword("tweet", 0.6, [0.5, 0.1, 0.2])],
                                     [Voice("Susanne", 0.3), Voice("Hannes", 0.6)],
                                     [BackgroundSample("aggressive_mood.mp3", 0.3)])

    background_sample = select_best_background([twitter_snippet])
    print("Best background sample: {0}".format(background_sample))
