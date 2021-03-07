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

    def load_wordnet(self):
        word_synsets = list(wn.all_synsets(wn.NOUN))

        def syn_to_str(x):
            return x.name().split('.')[0]

        if self.is_valid_word is not None:
            self.nouns.update([w for w in map(syn_to_str, word_synsets) if self.is_valid_word(w)])
        else:
            self.nouns.update([w for w in map(syn_to_str, word_synsets)])

    def load_desiq(self):
        desiq_url = 'http://www.desiquintans.com/downloads/nounlist/nounlist.txt'

        with urlopen(desiq_url) as response:
            content = response.read()
            words = content.decode("utf-8").split('\n')
            if self.is_valid_word is not None:
                self.nouns.update([w for w in words if self.is_valid_word(w)])
            else:
                self.nouns.update(words)

    def sample(self, num_words=1):
        if len(self.nouns) <= num_words:
            return self.nouns

        return random.sample(self.nouns, num_words)