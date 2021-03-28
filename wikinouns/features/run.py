import pandas as pd
import nltk

from wikinouns.mining.word_database import WordDatabase
from wikinouns.features.noun_features import apply_on_parts
from wikinouns.features.noun_features import single_freqs, double_freqs, triple_freqs


DATABASE_FILE = "../wikinouns.db"
FEATURE_FILE = "../features.csv"


def main():
    word_db = WordDatabase(DATABASE_FILE)

    rows = []
    for noun, content, tag in word_db.pull():
        tokens = content.split(',')
        tagged_words = nltk.pos_tag(tokens)
        tags = [t[1].lower() for t in tagged_words]

        features = dict()
        features.update(apply_on_parts(tags, functions=[single_freqs, double_freqs, triple_freqs], splits=1))
        features.update(apply_on_parts(tags, functions=[single_freqs, double_freqs, triple_freqs], splits=2))
        features.update(apply_on_parts(tags, functions=[single_freqs, double_freqs, triple_freqs], splits=3))
        features.update(apply_on_parts(tags, functions=[single_freqs, double_freqs, triple_freqs], splits=4))
        features['noun'] = noun
        features['tag'] = tag
        rows.append(features)

    df = pd.DataFrame(rows).fillna(0)
    df.to_csv(FEATURE_FILE)


if __name__ == '__main__':
    main()

