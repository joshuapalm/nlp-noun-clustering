import time

import nltk
import wikipedia


class WikiMiner:
    def __init__(self, sampler, query_wait_duration=15):
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
        c_tokens = [x for x in c_tokens if x]
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
        while self.running and ((time.time() - start_time) < duration):
            noun = self.sampler.sample()[0]
            print((time.time() - start_time))

            try:
                content = self.query(noun)
                time.sleep(self.query_wait_duration)
                tokens = self.tokenize_text(content)
                if self.article_is_valid(tokens):
                    str_tokens = ",".join(tokens)
                    self.forward((noun, str_tokens))
            except Exception as e:
                print('Wikipedia page for "{}" not found. '.format(noun))

    def stop(self):
        self.running = False


