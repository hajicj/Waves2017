"""This module is responsible for mapping music to words, so that we can use
word2vec.

The path to the directory that contains the actual music is in the env. var.
WAVES_MUSIC_ROOT.
"""
from __future__ import print_function, unicode_literals
import os
import re

__version__ = "0.0.1"
__author__ = "Jan Hajic jr."


if 'WAVES_MUSIC_ROOT' not in os.environ:
    os.environ['WAVES_MUSIC_ROOT'] = '~/Waves2017/soundfiles'


##############################################################################


def soundfile2words(soundfile):
    """The filename format is piano-singer-songwriter-power-pop_zj0qi44_.mp3"""
    basename = os.path.basename(soundfile)
    descriptor, key = basename.split('_', 1)
    descriptor_words = descriptor.split('-')
    return descriptor_words


def available_soundfiles():
    root = os.environ['WAVES_MUSIC_ROOT']
    return [os.path.join(root, f) for f in os.listdir(root)]