"""This module steals tokenization from the sent2vec repo."""
from __future__ import print_function, unicode_literals
import os
import re
from nltk import TweetTokenizer
import codecs

__version__ = "0.0.1"
__author__ = "Jan Hajic jr."


##############################################################################


def preprocess_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+)|(http?://[^\s]+))','<url>',tweet)
    tweet = re.sub('(\@[^\s]+)','<user>',tweet)
    try:
        tweet = tweet.decode('unicode_escape').encode('ascii', 'ignore')
    except:
        pass
    return tweet


def tokenize_tweets(filename, dest_folder):
    basename = os.path.basename(filename)
    dest = os.path.join(dest_folder, basename + '.tok')
    print("processing %s" % basename)
    tknzr = TweetTokenizer()
    with codecs.open(dest, 'w', "utf-8") as out_fs:
        with open(filename, 'r', encoding="utf-8") as in_fs:
            for line in in_fs:
                try:
                    language, id, timestamp, username, tweet = line.strip().split('\t')
                except:
                    print("could not parse line.")
                    continue
                if language != 'en':
                    continue
                tweet = tknzr.tokenize(tweet)
                if not 6 < len(tweet) < 110:
                    continue
                tweet = preprocess_tweet(' '.join(tweet))
                filter(lambda word: ' ' not in word, tweet)
                out_fs.write(id+'\t'+timestamp+'\t'+username+'\t'+tweet+'\n')

