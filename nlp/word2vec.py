"""This module implements a class that..."""
from __future__ import print_function, unicode_literals
import logging
import subprocess
import json

__version__ = "0.0.1"
__author__ = "Jan Hajic jr."


def query_word2vec_api(qs, ks, port=9001, host='127.0.0.1'):
    """Queries a running word2vec-api server on the given host/port."""
    _waste_output = 0.00001
    if len(qs) == 0:
        logging.warning('No query keywords!')
        return _waste_output
    if len(ks) == 0:
        logging.warning('No database keywords!')
        return _waste_output

    # construct group URL
    ws1 = '&'.join(['ws1=' + q for q in qs])
    ws2 = '&'.join(['ws2=' + k for k in ks])

    max_sim = -1.1
    max_wq = None
    max_wk = None
    for w1 in qs:
        for w2 in ks:
            url = 'http://' + host + ':' + str(port) + \
                  '/word2vec/similarity?w1={0}&w2={1}'.format(w1, w2)
            proc = subprocess.Popen(['curl', url],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)

            # Getting some resistance to server problems
            similarities = []
            for line in proc.stdout:
                s = float(line.strip())
                similarities.append(s)

            s = similarities[0]
            if s > max_sim:
                max_sim = s
                max_wq = w1
                max_wk = w2

    print('Max. similarity between {0} and {1}: {2} ({3} - {4})'
          ''.format(qs, ks, max_sim, max_wq, max_wk))
    return max_sim


def query_word2vec_maxn(q, k=100, port=9001, host='127.0.0.1'):
        url = 'http://' + host + ':' + str(port) + \
              '/word2vec/most_similar?positive={0}&topn={1}'.format(
                  '&positive='.join(q),
                  k)
        proc = subprocess.Popen(['curl', url],
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        lines = [str(l.strip()) for l in proc.stdout]
        line = lines[0]
        if line.startswith('b'):
            line = line[2:-1]

        line = line[1:-1]
        items = line.split('], ')
        output = []
        for item in items:
            try:
                ws, ns = item.split(', ')
                word = ws[1:-1]
                num = float(ns[:-1])
                output.append([word, num])
            except Exception as e:
                print('Could not parse item {0}!'
                      ''.format(item))
                raise e
        return output
