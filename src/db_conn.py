#! /Users/audrius/Documents/VCSPython/py_projmngpg/bin/python3

import os
import psycopg2.extras
from dotenv import load_dotenv


load_dotenv()


class DBEngine:
    def __init__(self):
        self.connection = self.connect()
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

    @staticmethod
    def connect():
        try:
            connection = psycopg2.connect(
                dbname=os.getenv('DATABASE_NAME'),
                user=os.getenv('DB_USERNAME'),
                password=os.getenv('PASSWORD'),
                host=os.getenv('HOST'),
                port=os.getenv('PORT')
            )
            print("\nConnected to PostgresSQL database. Congratulations!")
        except (Exception, psycopg2.Error) as error:
            raise Exception("Error while connecting to PostgresSQL", error)

        return connection

    def __del__(self):
        if self.connection:
            self.cursor.close()
            self.connection.close()
            print('That is it. Connection closed!')
