import time

import nltk
from nltk.corpus import wordnet
import wikipedia


class WikiMiner:
    def __init__(self, sampler, query_wait_duration=5):
        self.sampler = sampler
        self.query_wait_duration = query_wait_duration
        self.destinations = list()
        self.running = False

    def add(self, dest):
        self.destinations.append(dest)

    def forward(self, datum):
        for dest in self.destinations:
            dest.push(datum)

    @staticmethod
    def query(word):
        page = wikipedia.page(word)
        return page.content

    @staticmethod
    def tokenize_text(text):
        text = text.lower()
        tokens = nltk.word_tokenize(text)
        c_tokens = [''.join(e for e in string if e.isalpha()) for string in tokens]
        c_tokens = [x for x in c_tokens if x and wordnet.synsets(x)]
        return c_tokens

    @staticmethod
    def article_is_valid(tokens):
        conditions = list()
        conditions.append(bool(2000 < len(tokens)))
        conditions.append(bool(10000 > len(tokens)))
        return all(conditions)

    def start(self, duration=60):
        self.running = True
        start_time = time.time()
        while not self.sampler.is_empty() and ((time.time() - start_time) < duration):
            try:
                noun, label = self.sampler.sample()
                search = wikipedia.search(noun)
                search = [s.lower() for s in search]
                if noun in search:
                    content = self.query(noun)
                    time.sleep(self.query_wait_duration)
                    tokens = self.tokenize_text(content)
                    if self.article_is_valid(tokens) and noun in tokens:
                        str_tokens = ",".join(tokens)
                        self.forward((noun, str_tokens, label))
            except Exception as e:
                pass

    def stop(self):
        self.running = False

