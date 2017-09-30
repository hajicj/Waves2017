from typing import List


class TwitterSnippet:
    def __init__(self, start: int, end: int, text: str, relevance: float, keywords: List[Keyword], voices: List[Voice],
                 background_samples: List[BackgroundSample]) -> None:
        self.voices = voices
        self.background_samples = background_samples
        self.keywords = keywords
        self.start = start
        self.end = end
        self.text = text
        self.relevance = relevance


class Voice:
    def __init__(self, speaker: str, similarity: float) -> None:
        self.similarity = similarity
        self.speaker = speaker


class BackgroundSample:
    def __init__(self, filename: str, similarity: float) -> None:
        self.similarity = similarity
        self.filename = filename


class Keyword:
    def __init__(self, word: str, relevance: float, word2vec: List[float]) -> None:
        self.word2vec = word2vec
        self.relevance = relevance
        self.word = word
