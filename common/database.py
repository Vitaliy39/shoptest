from typing import List
import sqlite3

class Database:
    DATABASE = 'data.db'
    @staticmethod
    def create_table(name:str):
        connecton = sqlite3.connect(Database.DATABASE)
        cursor = connecton.cursor()
        query = 'CREATE TABLE IF NOT EXISTS goods (id integer PRIMARY KEY AUTOINCREMENT, goodname text, image text, price text)'
        cursor.execute(query)
        connecton.close()

    @staticmethod
    def find_by_name_and_job(name: str, usertype:str) -> List:
        connecton = sqlite3.connect(Database.DATABASE)
        cursor = connecton.cursor()
        query = "SELECT * FROM users WHERE username=? and usertype=?"
        result = cursor.execute(query, (name, usertype)).fetchone()
        connecton.close()
        return result

    @staticmethod
    def insert_value(table:str, data:dict):
        connection = sqlite3.connect(Database.DATABASE)
        cursor = connection.cursor()
        keys=str(tuple([i for i in data.keys()]))
        vals=(tuple([i for i in data.values()]))
        print(keys)
        print((vals))
        query = "INSERT INTO {} {} VALUES(?,?,?)".format(table, keys)
        cursor.execute(query, vals)
        connection.commit()
        connection.close()

    @staticmethod
    def get_all_data(table:str) -> List:
        connection = sqlite3.connect(Database.DATABASE)
        cursor = connection.cursor()
        query = "SELECT * FROM {}".format(table)
        query_result=cursor.execute(query).fetchall()
        column_names=[]
        result = []
        for row in cursor.description:
            column_names.append(row[0])
        for q in query_result:
            a = dict(zip(column_names, q))
            result.append(a)
        return result