import json
from argparse import Namespace
from json import JSONDecoder

import jsonpickle

from TwitterSnippet import TwitterSnippet, Keyword, Voice, BackgroundSample

json_path = "Test.json"
with open(json_path) as data_file:
    json_data = json.load(data_file)
    json_string = str(json_data).replace("'", '"')
    twitter_snippets = jsonpickle.decode(json_string)
print(twitter_snippets)


class Thing(object):
    def __init__(self, name):
        self.name = name

obj = Thing('Awesome')
frozen = jsonpickle.encode(obj)
thawed = jsonpickle.decode(frozen)

twitter_snippet = TwitterSnippet(0, 3, "This is a tweet", 0.9, [Keyword("tweet", 0.6, [0.5, 0.1, 0.2])], [Voice("Susanne", 0.3), Voice("Hannes", 0.6)], [BackgroundSample("aggressive_mood.mp3", 0.3)])
frozen = jsonpickle.encode(twitter_snippet)
thawed = jsonpickle.decode(frozen)
