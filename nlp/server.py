from __future__ import print_function, unicode_literals, division

import logging
import pprint
import subprocess
from flask import Flask, request, json

from .music import create_music_database

app = Flask(__name__)


@app.route('/nlp/analysis', methods=['GET', 'POST'])
def analysis():
    request_json = request.get_json()

    if request_json is not None:
        text = request_json.get('text')
        lang = request_json.get('lang')

        ## TODO: do some fancy stuff...

        return json.jsonify({
            'similar_words': None,
            'text': text
            })

    return json.jsonify({'error': 'please provide a tweet as json'})


##############################################################################


class Analysis():

    def __init__(self,
                 music_database=None,
                 similarity_fn=None,
                 similarity_fn_kwargs=None):
        """The similarity_fn has to take the query keywords and a set
        of database keywords as two params."""
        if music_database is None:
            music_database = create_music_database()
        self.music_database = music_database

        self.similarity_fn = similarity_fn
        if similarity_fn_kwargs is None:
            similarity_fn_kwargs = dict()
        self.similarity_fn_kwargs = similarity_fn_kwargs

        # Getting rid of div by zero
        self._eps = 0.000000000001

    def process(self, text):
        tokens = self.tokenize(text)
        segments = self.segment(tokens)

        # Find keywords in segments.
        for s_start, s_end in segments:

            s_tokens = tokens[s_start:s_end]

            # Query music database for segment
            music_similarities = dict()
            for k in self.music_database:
                # Convert the music database keys, which are currently single keywords,
                # to word sets
                k_tokens = [k]
                s = self.query(s_tokens, k_tokens, **self.similarity_fn_kwargs)
                musics = self.music_database[k].keys()
                for m in musics:
                    music_similarities[m] = s

            # Create the segment entry.
            # segment_entry = {
            #     'start': s_start,
            #     ''
            # }
            print('Segment {0}: music similarities {1}'
                  ''.format(s_tokens, pprint.pformat(music_similarities)))

        return json.jsonify()

    def tokenize(self, text):
        return text.split()

    def segment(self, tokens):
        return [(0, len(tokens))]

    def query(self, q, k, **kwargs):
        """Given two sets keywords, queries the similarity service."""
        s = 0.0 + self._eps
        try:
            s = self.similarity_fn(q, k, **kwargs)
        except:
            pass
        return s


def query_word2vec_api(qs, ks, port=9001, host='127.0.0.1'):
    """Queries a running word2vec-api server on the given host/port."""
    _waste_output = 0.00001
    if len(qs) == 0:
        logging.warning('No query keywords!')
        return _waste_output
    if len(ks) == 0:
        logging.warning('No database keywords!')
        return _waste_output

    # construct URL
    ws1 = '&'.join(['ws1=' + q for q in qs])
    ws2 = '&'.join(['ws2=' + k for k in ks])

    url = 'http://' + host + ':' + str(port) + '/word2vec/n_similarity?' + ws1 + '&' + ws2
    print(url)
    proc = subprocess.Popen(['curl', url], stdout=subprocess.PIPE)

    # Getting some resistance to server problems
    similarities = []
    for line in proc.stdout:
        s = float(line.strip())
        similarities.append(s)

    return similarities[0]
