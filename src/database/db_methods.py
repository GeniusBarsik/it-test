import sqlite3 as sl
from src.models.message_box import message


class DataBase:
    def __init__(self, name):
        try:
            self.conn = sl.connect(name)
            self.__create_table()
        except Exception as e:
            message.show_err_info(e)

        # Создание базы данных
    def __create_table(self):
        with self.conn:
            self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS Customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(20) NOT NULL,
                        lastname VARCHAR(20) NOT NULL,
                        phone VARCHAR(20) NOT NULL,
                        notes TEXT
                    )
                """)
            self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        category VARCHAR(100) NOT NULL,
                        name VARCHAR(50) NOT NULL,
                        price NUMERIC NOT NULL,
                        SKU VARCHAR(50) NOT NULL,
                        expiry_date VARCHAR(20),
                        image_url VARCHAR(255),
                        features TEXT
                    )
                    """)
            self.conn.execute("""
                    CREATE TABLE IF NOT EXISTS Orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        product_id INTEGER,
                        FOREIGN KEY (customer_id) REFERENCES Customers (id) ON DELETE CASCADE,
                        FOREIGN KEY (product_id) REFERENCES Products (id) ON DELETE CASCADE
                    )
                    """)
            self.conn.execute("""
                   CREATE TABLE IF NOT EXISTS Warehouses (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name VARCHAR(25) NOT NULL
                   )
                   """)
            self.conn.execute("""
                   CREATE TABLE IF NOT EXISTS Storage (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       warehouse_id INTEGER,
                       product_id INTEGER,
                       quantity INTEGER NOT NULL,
                       FOREIGN KEY (product_id) REFERENCES Products (id) ON DELETE CASCADE,
                       FOREIGN KEY (warehouse_id) REFERENCES Warehouses (id) ON DELETE CASCADE
                   )
                   """)
            self.conn.execute("""
                   CREATE TABLE IF NOT EXISTS Admins (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_code VARCHAR(20),
                       permissions_level VARCHAR(1)
                   )
                   """)

    def permissions_level(self, user_code):
        with self.conn:
            try:
                info = self.conn.execute("SELECT permissions_level FROM Admins "
                                         "WHERE user_code = ?", (user_code,)).fetchall()
                if info:
                    return info[0][0]
                return False
            except Exception as e:
                print(e)

    def add_admin(self, code, level):
        with self.conn:
            self.conn.execute("INSERT INTO Admins (user_code, permissions_level) VALUES (?, ?)", (code, level))

    def is_customer_in_db(self, phone):
        with self.conn:
            info = self.conn.execute("SELECT id FROM Customers WHERE phone = ?", (phone,)).fetchall()
            if info:
                return True
            return False

    def add_customer_to_db(self, name, lastname, phone, notes=""):
        with self.conn:
            try:
                self.conn.execute("INSERT INTO Customers (name, lastname, phone, notes) "
                                  "VALUES (?, ?, ?, ?)", (name, lastname, phone, notes))
                message.show_ok_info("Клиент успешно добавлен")
            except Exception as e:
                message.show_err_info(e)

    def select_customer(self, phone):
        with self.conn:
            info = self.conn.execute("SELECT name, lastname, phone, notes FROM Customers "
                                     "WHERE phone = ?", (phone,)).fetchall()
        if info:
            return info[0][0], info[0][1], info[0][2], info[0][3]
        message.show_err_info("Клиента с данным номером телефона нет в базе данных")
        return False
'''
    def change_customer_in_db(self, name, lastname, phone, notes):
        with self.conn:
            self.conn.execute("UPDATE Customers "
                              "SET name = ?, lastname = ?, phone = ?, notes = ? "
                              "WHERE phone = ?", (name, lastname, phone, notes))
        message.show_ok_info(f"Данные клиента: {name} успешно изменены")

    def add_product_to_bd(self, category, name, price, sku, expiry_date, image_url, features):
        with self.conn:
            self.conn.execute("INSERT INTO Products (category, name, price, SKU, expiry_date, image_url, features) "
                              "VALUES (?, ?, ?, ?, ?, ?, ?)", (category, name, price, sku, expiry_date, image_url, features))
'''
db = DataBase("Shop_info")


if __name__ == '__main__':
    print(db.select_customer("+375336193565"))