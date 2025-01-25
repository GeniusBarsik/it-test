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

    def is_product_in_db(self, sku):
        with self.conn:
            info = self.conn.execute("SELECT id FROM Products WHERE sku = ?", (sku,)).fetchall()
            print(info)
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

    def take_info_from_bd(self, table_name, widget, *args):
        params = ", ".join([el for el in args])
        with self.conn:
            print(params)
            info = self.conn.execute(f"SELECT {params} FROM {table_name}").fetchall()
            return info

    def take_column_names(self, table_name):
        names = self.conn.execute(f"PRAGMA table_info({table_name})").fetchall()
        names = [col[1] for col in names]
        return names

    def add_product_to_bd(self, category, name, price, sku, expiry_date, image_url, features):
        with self.conn:
            self.conn.execute("INSERT INTO Products (category, name, price, SKU, expiry_date, image_url, features) "
                              "VALUES (?, ?, ?, ?, ?, ?, ?)",
                              (category, name, price, sku, expiry_date, image_url, features))

            message.show_ok_info("Продукт добавлен")

    def delete_from_db(self, table_name, item):
        try:
            with self.conn:
                self.conn.execute(f"DELETE FROM {table_name} WHERE SKU = ?", (item,))
        except Exception as e:
            print(e)

    def edit_product(self, category, name, price, sku, expiry_date, image_url, features):
        try:
            with self.conn:
                print(category, sku, name)
                self.conn.execute("UPDATE Products "
                                  "SET category = ?, name = ?, price = ?, expiry_date = ?, image_url = ?, features = ? "
                                  "WHERE SKU = ? ",
                                  (category, name, price, expiry_date, image_url, features, sku))
                message.show_ok_info("Продукт изменен")
        except Exception as e:
            print(e)


'''
    def change_customer_in_db(self, name, lastname, phone, notes):
        with self.conn:
            self.conn.execute("UPDATE Customers "
                              "SET name = ?, lastname = ?, phone = ?, notes = ? "
                              "WHERE phone = ?", (name, lastname, phone, notes))
        message.show_ok_info(f"Данные клиента: {name} успешно изменены")
'''

db = DataBase("Shop_info")

if __name__ == '__main__':
    db.delete_from_db("Products", 1)
