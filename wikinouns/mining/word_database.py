import os

import sqlite3
from sqlite3 import Error


class WordDatabase:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)

    def __iter__(self):
        return self.pull()

    def pull(self):
        sql_select = "SELECT * FROM nouns"
        if self.conn is not None:
            test = self.conn.cursor().execute(sql_select)
            for row in test:
                yield row

    def push(self, row):
        if self.conn is not None:
            self.__create_table(self.conn.cursor())

        self.__insert(self.conn.cursor(), row)
        self.conn.commit()

    def __create_table(self, cursor):
        sql_create = """ CREATE TABLE IF NOT EXISTS nouns (
                        noun text PRIMARY KEY,
                        words text NOT NULL ); """
        cursor.execute(sql_create)

    def __insert(self, cursor, datum):
        sql_insert = """ INSERT INTO nouns(noun, words)
                        VALUES(?,?) """
        cursor.execute(sql_insert, datum)
