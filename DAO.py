from DTO import *


class Hats:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, hatDTO):
        self.conn.execute(""" INSERT INTO hats (id, topping, supplier, quantity) VALUES (?, ?, ?, ?)""",
                          [hatDTO.id, hatDTO.topping, hatDTO.supplier, hatDTO.quantity])

    def find(self, topping):
        c = self.conn.cursor()
        c.execute("""SELECT id, topping, supplier, quantity FROM hats WHERE topping = ? ORDER BY supplier""", [topping, ])
        return Hat(*c.fetchone())

    def update(self, id):
        self.conn.execute("""UPDATE hats SET quantity = quantity-1  WHERE id = ?""", [id, ])
        c = self.conn.cursor()
        c.execute("""SELECT quantity FROM hats WHERE id = ?""", [id, ])
        if c.fetchone()[0] == 0:
            self.delete(id)

    def delete(self, id):
        self.conn.execute("""DELETE From hats WHERE id = ?""", [id, ])


class Suppliers:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, supplierDTO):
        self.conn.execute(""" INSERT INTO suppliers (id, name) VALUES (?, ?)""",
                          [supplierDTO.id, supplierDTO.name])

    def find(self, id):
        c = self.conn.cursor()
        c.execute("""SELECT * FROM suppliers WHERE id = ?""", [id, ])
        return Supplier(*c.fetchone())


class Orders:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, orderDTO):
        self.conn.execute(""" INSERT INTO orders(id, location, hat) VALUES (?, ?, ?)""",
                          [orderDTO.id, orderDTO.location, orderDTO.hat.id])
