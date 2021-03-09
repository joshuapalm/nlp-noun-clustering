import sqlite3
from sqlite3 import Error


class WordDatabase:
    def __init__(self, db_file):

        sql_nouns_table = """ CREATE TABLE IF NOT EXISTS nouns (
                          noun text PRIMARY KEY,
                          words text NOT NULL ); """

        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        if self.conn is not None:
            c = self.conn.cursor()
            c.execute(sql_nouns_table)
        else:
            print("Error! cannot create the database connection.")

    def push(self, datum):
        self.insert(datum)

    def insert(self, row):
        sql = ''' INSERT INTO nouns(noun, words)
              VALUES(?,?) '''
        cur = self.conn.cursor()
        cur.execute(sql, row)
        self.conn.commit()
        return cur.lastrowid

    def key_exists(self, noun):
        sql = ''' SELECT 1 FROM "nouns" WHERE "noun"="{}" LIMIT 1; '''.format(noun)
        cur = self.conn.cursor()
        cur.execute(sql)
        a = cur.fetchall()
        return len(a) > 0

