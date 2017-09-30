"""This module is responsible for mapping music to words, so that we can use
word2vec.

The path to the directory that contains the actual music is in the env. var.
WAVES_MUSIC_ROOT.
"""
from __future__ import print_function, unicode_literals, division
import os
import re

import collections

import numpy
from nltk.corpus import stopwords
import textblob

from .word2vec import query_word2vec_maxn
from .tokenize import filter_stopwords

__version__ = "0.0.1"
__author__ = "Jan Hajic jr."


if 'WAVES_MUSIC_ROOT' not in os.environ:
    os.environ['WAVES_MUSIC_ROOT'] = '/Users/hajicj/Waves2017/soundfiles'



mood_words = []

##############################################################################


def soundfile2keywords(soundfile, filtering=True):
    """The filename format is piano-singer-songwriter-power-pop_zj0qi44_.mp3"""
    basename = os.path.basename(soundfile)
    descriptor, key = basename.split('_', 1)
    descriptor_words = descriptor.split('-')
    if filtering:
        descriptor_words = filter_stopwords(descriptor_words)
    return descriptor_words


def available_soundfiles():
    root = os.environ['WAVES_MUSIC_ROOT']
    return [os.path.join(root, f) for f in os.listdir(root)]


def create_music_database(sentiment=False):
    if sentiment:
        return create_music_database_sentiment()
    else:
        return create_music_database_keywords()


def create_music_database_keywords():
    """Creates the music database. Each piece of music is characterized
    by a list of keywords. These keywords can come from wherever: from
    the descriptor, from some mood dictionary, etc. Returns an inverse dict:
    for each keyword, a dict of the soundfiles for which it is relevant
    and the relevance of the keyword to that file."""
    keyword2soundfile = collections.defaultdict(dict)

    for f in available_soundfiles():
        keywords = soundfile2keywords(f)
        relevances = [1.0 for k in keywords]
        for keyword, relevance in zip(keywords, relevances):
            keyword2soundfile[keyword][f] = relevance

    return keyword2soundfile


def create_music_database_sentiment(expand=50):
    """Keys: subjectivity and valence vectors
    Values: music files
    """
    data = dict()
    for fname in available_soundfiles():
        keywords = soundfile2keywords(fname, filtering=True)
        print('Getting similarity for fname: {0}'
              ' tokens: {1}'.format(fname, keywords))

        try:
            subjectivity, polarity = get_expanded_sentiment_score(keywords,
                                                                  k=expand)
            data[fname] = (subjectivity, polarity)
        except Exception as e:
            print(e)
            print('File {0} will not be retrievable'.format(fname))
            continue

    return data


def get_expanded_sentiment_score(tokens, k=30):
    similar = query_word2vec_maxn(tokens, k=k)

    similar_words = [s[0] for s in similar]
    similarities = [s[1] for s in similar]
    subjectivities = []
    polarities = []
    for w in similar_words:
        blob = textblob.TextBlob(w)
        subjectivities.append(blob.subjectivity)
        polarities.append(blob.polarity)

    max_sim = numpy.sqrt(similarities[0] ** 2)

    subjectivity = 0.0
    polarity = 0.0
    n_subj_tokens = 1

    for idx in range(len(similar_words)):
        sim_ratio = similarities[idx] / max_sim
        if ((sim_ratio * subjectivities[idx]) ** 2) > (0.3 ** 2):
            # print('Subjective token for tokens {0}: {1} / {2}, {3}'
            #       ''.format(tokens, similar_words[idx],
            #                 subjectivities[idx], polarities[idx]))

            subjectivity += subjectivities[idx] * (sim_ratio ** 2)
            polarity += polarities[idx] * (sim_ratio ** 2)
            n_subj_tokens += 1.

    subjectivity /= n_subj_tokens
    polarity /= n_subj_tokens

    return (subjectivity, polarity)


def print_sentiment_database(d):
    for f in d:
        fname = os.path.basename(f)
        s = d[f][0]
        p = d[f][1]
        print('Filename: {0}\tS: {1:.3f}\tP: {2:.3f}'
              ''.format(fname, s, p))