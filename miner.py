import time

from word_database import WordDatabase

from query import query_wiki
from tokenize import tokenize_text
from noun_sampler import NounSampler


DATABASE_FILE = "wikinouns.db"
NUM_NOUN_SAMPLES = 20
QUERY_WAIT_DURATION = 5


def article_is_valid(tokens):
    conditions = list()
    conditions.append(bool(2000 < len(tokens)))
    conditions.append(bool(10000 > len(tokens)))
    return all(conditions)


def main():
    db = WordDatabase(DATABASE_FILE)

    ns = NounSampler()
    ns.load_desiq()

    i = 0
    while i < NUM_NOUN_SAMPLES:
        noun = ns.sample()

        if not db.key_exists(noun):
            try:
                content = query_wiki(noun)
                time.wait(QUERY_WAIT_DURATION)
            except Exception as e:
                continue

            tokens = tokenize_text(content)
            if article_is_valid(tokens):
                str_tokens = ",".join(tokens)
                db.insert((noun, str_tokens))
                i += 1


if __name__ == '__main__':
    main()

