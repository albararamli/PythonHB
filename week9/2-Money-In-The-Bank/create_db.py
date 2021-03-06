import sqlite3


class bank_clients():

    def __init__(self):
        self.conn = sqlite3.connect("bank.db")
        self.cursor = self.conn.cursor()

    def generate_tables(self):

        sqlCreate = """CREATE TABLE clients(
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        balance REAL,
                        message TEXT,
                        mail TEXT)"""

        self.cursor.execute(sqlCreate)
        self.conn.commit()

    def insert_into_table(self, id, username, password, balance, message, mail):
        sqlInsert = "INSERT into clients (id, username, password, balance, message, mail) values (?, ?, ?, ?, ?, ?)"
        self.cursor.execute(
            sqlInsert, (id, username, password, balance, message, mail))
        self.conn.commit()

viBank = bank_clients()
viBank.generate_tables()
viBank.insert_into_table(1, "Ivan", "pw1", "300", "I am Ivan", "i@v.an")