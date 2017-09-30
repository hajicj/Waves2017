import json

with open("Test.json") as data_file:
    twitter_snippets = json.load(data_file)
print(twitter_snippets)
