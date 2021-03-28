import csv
import random
from urllib.request import urlopen

import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')


def custom_filter_fcn(word):
    conditions = list()
    conditions.append(bool(len(word) > 2))
    conditions.append(bool(len(word) < 20))
    conditions.append(bool(word.isalpha()))
    return all(conditions)


class NounSampler:
    def __init__(self, filter_fcn=custom_filter_fcn):
        self.is_valid_word = filter_fcn
        self.nouns = set()

    def add_word(self, word, tag='unknown'):
        if isinstance(word, str):
            word = [(word, tag)]
        elif isinstance(word, list):
            word = [(w, tag) for w in word]
        else:
            raise Exception
        self.nouns.update(set(word))

    def load_from_csv(self, filepath):
        data = []
        with open(filepath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count > 0:
                    data.append(tuple(row))
                line_count += 1
        self.nouns.update(set(data))

    def load_wordnet(self, tag='unknown'):
        def syn_to_str(x):
            return x.name().split('.')[0]
        word_synsets = list(wn.all_synsets(wn.NOUN))
        if self.is_valid_word is not None:
            self.nouns.update([(w, tag) for w in map(syn_to_str, word_synsets) if self.is_valid_word(w)])
        else:
            self.nouns.update([(w, tag) for w in map(syn_to_str, word_synsets)])

    def load_desiq(self, tag='unknown'):
        desiq_url = 'http://www.desiquintans.com/downloads/nounlist/nounlist.txt'
        with urlopen(desiq_url) as response:
            content = response.read()
            words = content.decode("utf-8").split('\n')
            if self.is_valid_word is not None:
                self.nouns.update([(w, tag) for w in words if self.is_valid_word(w)])
            else:
                self.nouns.update([(w, tag) for w in words])

    def is_empty(self):
        return len(self.nouns) == 0

    def sample(self):
        if self.is_empty():
            return None
        noun = random.choice(tuple(self.nouns))
        self.nouns.remove(noun)
        return noun

