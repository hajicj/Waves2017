import json
from argparse import Namespace
from json import JSONDecoder

import jsonpickle

with open("Test.json") as data_file:
    json_data = json.load(data_file)
    twitter_snippets = jsonpickle.decode(data_file)
print(twitter_snippets)
