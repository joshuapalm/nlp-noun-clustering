from wiki_miner import WikiMiner
from word_database import WordDatabase
from noun_sampler import NounSampler

DATABASE_FILE = "wikinouns.db"


def main():
    db = WordDatabase(DATABASE_FILE)

    ns = NounSampler()
    ns.load_desiq()

    miner = WikiMiner(ns)
    miner.add(db)

    miner.start(duration=60)


if __name__ == '__main__':
    main()
