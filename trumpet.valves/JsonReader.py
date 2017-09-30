import json
from typing import List

import jsonpickle

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample


def load_twitter_snippets_from_json(json_path: str = "Test.json") -> List[TwitterSnippet]:
    with open(json_path) as data_file:
        json_data = json.load(data_file)
        json_string = str(json_data).replace("'", '"')
        twitter_snippets = jsonpickle.decode(json_string)
    return twitter_snippets


if __name__ == "__main__":
    twitter_snippet = TwitterSnippet(0, 3, "This is a tweet", 0.9, [Keyword("tweet", 0.6, [0.5, 0.1, 0.2])],
                                     [Voice("Susanne", 0.3), Voice("Hannes", 0.6)],
                                     [BackgroundSample("aggressive_mood.mp3", 0.3)])

    twitter_snippets = load_twitter_snippets_from_json()
    print("Loaded {0} snippets from json file Test.json".format(len(twitter_snippets)))
