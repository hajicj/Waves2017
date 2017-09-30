import base64
import json
from typing import List

import jsonpickle

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample


def load_twitter_snippets_from_json_path(json_path: str = "Test.json") -> List[TwitterSnippet]:
    with open(json_path) as data_file:
        json_data = json.load(data_file)
        json_string = str(json_data).replace("'", '"')
        twitter_snippets = jsonpickle.decode(json_string)
    return twitter_snippets


def load_twitter_snippets_from_json(json_string: str) -> List[TwitterSnippet]:
    twitter_snippets = jsonpickle.decode(json_string)
    json_string = str(json_string).replace("'", '"')

    for twitter_snippet in twitter_snippets:
        twitter_snippet.text = str(base64.b64decode(twitter_snippet.text))
    return twitter_snippets


if __name__ == "__main__":
    twitter_snippets = load_twitter_snippets_from_json_path()
    print("Loaded {0} snippets from json file Test.json".format(len(twitter_snippets)))
