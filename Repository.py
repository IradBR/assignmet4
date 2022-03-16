import atexit
import sqlite3

from DAO import Hats, Suppliers, Orders


class Repository:
    def __init__(self, argv):
        self.conn = sqlite3.connect(argv[4])
        self.hats = Hats(self.conn)
        self.suppliers = Suppliers(self.conn)
        self.orders = Orders(self.conn)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.execute("""
        CREATE TABLE hats(
        id INT PRIMARY KEY, 
        topping TEXT NOT NULL, 
        supplier INT REFERENCES suppliers(id), 
        quantity INT NOT NULL) """)
        self.conn.execute("""
        CREATE TABLE suppliers(
        id INT PRIMARY KEY, 
        name TEXT NOT NULL) """)
        self.conn.execute("""
        CREATE TABLE orders(
        id INT PRIMARY KEY, location TEXT NOT NULL, 
        hat INT REFERENCES hats(id))""")



