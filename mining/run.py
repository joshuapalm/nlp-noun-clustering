from wiki_miner import WikiMiner
from word_database import WordDatabase
from noun_sampler import NounSampler

DATABASE_FILE = "wikinouns.db"


def main():
    db = WordDatabase(DATABASE_FILE)

    ns = NounSampler(with_replacement=False)
    ns.load_desiq()

    miner = WikiMiner(sampler=ns)
    miner.add(db)

    miner.start()


if __name__ == '__main__':
    main()
