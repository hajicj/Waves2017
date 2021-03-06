from __future__ import print_function, unicode_literals, division

import logging
import os
import pprint
import subprocess

import collections

import numpy
import textblob
from flask import Flask, request, json

from nltk.corpus import stopwords

from .music import create_music_database


##############################################################################


class Analysis:

    def __init__(self,
                 music_database=None,
                 similarity_fn=None,
                 similarity_fn_kwargs=None):
        """The similarity_fn has to take the query keywords and a set
        of database keywords as two params."""
        if music_database is None:
            music_database = create_music_database(sentiment=True)
        self.music_database = music_database

        self.similarity_fn = similarity_fn
        if similarity_fn_kwargs is None:
            similarity_fn_kwargs = dict()
        self.similarity_fn_kwargs = similarity_fn_kwargs

        # Getting rid of div by zero..?
        self._eps = 0.000000000001

    def process(self, text):
        return self.process_sentiment(text)

    def process_word2vec(self, text):
        # Unused.
        tokens = self.tokenize(text)
        segments = self.segment(tokens)

        # Find keywords in segments.
        for s_start, s_end in segments:

            s_tokens = tokens[s_start:s_end]

            # Query music database for segment
            music_similarities = collections.defaultdict(float)
            for k in self.music_database:
                # Convert the music database keys, which are currently single keywords,
                # to word sets
                k_tokens = [k]
                s = self.query(s_tokens, k_tokens, **self.similarity_fn_kwargs)
                musics = self.music_database[k].keys()
                for m in musics:
                    if s > music_similarities[m]:
                        print('SIM: input {0} for keyword {1} is new max: {2}'
                              ''.format(s_tokens, k, s))
                    music_similarities[m] = max(s, music_similarities[m])

            sorted_music_similarities = sorted(music_similarities.items(),
                                                 key=lambda kv: kv[1],
                                                 reverse=True)
            top_five_music_similarities = sorted_music_similarities[:5]
            # Create the segment entry.
            # segment_entry = {
            #     'start': s_start,
            #     ''
            # }
            print('Segment {0}: music similarities {1}'
                  ''.format(s_tokens, pprint.pformat(sorted_music_similarities)))

            print('Segment {0}: TOP5 music similarities {1}'
                  ''.format(s_tokens, pprint.pformat(top_five_music_similarities)))

        # return json.jsonify({})

    def process_sentiment(self, text):

        tokens = self.tokenize(text)
        clean_text = ' '.join(tokens)

        blob = textblob.TextBlob(clean_text)
        qp = blob.polarity
        qs = blob.subjectivity

        similarities = dict()
        for fname in self.music_database:
            ks, kp = self.music_database[fname]
            dist = numpy.sqrt((qs - ks) ** 2 + (qp - kp) ** 2)
            similarities[fname] = dist

        sorted_similarities = sorted(similarities.items(),
                                     key=lambda kv: kv[1],
                                     )
        print('Similarities:\n{0}'.format(pprint.pformat(sorted_similarities[:10])))

        # Just one segment
        output_total = {
            "py/object": "__main__.TwitterSnippet",
            "start": 0,
            "end": len(text.split()),
            "text": text,
            "relevance": 1.0,

            "keywords": [
                {"py/object": "__main__.Keyword",
                 "word": k,
                 "relevance": 1.0,
                 "word2vec": [0.1, 0.2, 0.3, 0.4, 0.5]}
            for k in tokens],

            "background_samples": [
                {"py/object": "__main__.BackgroundSample",
                 "filename": os.path.basename(sfname),
                 "similarity": snum
                 }
            for sfname, snum in sorted_similarities[:3]],

            "voices": [
                {"py/object": "__main__.Voice",
                 "speaker": "Stephanie",
                 "similarity": 1.0}
            ]
        }

        output = [output_total]
        return output

    def tokenize(self, text):
        tokens = text.split()
        filtered_tokens = [t for t in tokens
                           if t not in stopwords.words('english')]
        return filtered_tokens

    def segment(self, tokens):
        return [(0, len(tokens))]

    def query(self, q, k, **kwargs):
        """Given two sets keywords, queries the similarity service."""
        s = 0.0 + self._eps
        try:
            s = self.similarity_fn(q, k, **kwargs)
        except Exception as e:
            print(e)
            pass
        return s


##############################################################################

analysis_module = Analysis()

app = Flask(__name__)



@app.route('/nlp/analysis', methods=['GET', 'POST'])
def analysis():
    request_json = request.get_json()

    if request_json is not None:
        text = request_json.get('text')
        lang = request_json.get('lang')

        output = analysis_module.process(text)
        return json.jsonify(output)

    return json.jsonify({'error': 'please provide a tweet as json'})


if __name__ == '__main__':
    # Run the flask app
    pass
