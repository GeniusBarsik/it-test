import sqlite3 as sl


# Подключение / создание базы данных
con = sl.connect('shop_db')

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            category VARCHAR(100) NOT NULL,
            features TEXT,
            SKU VARCHAR(50) NOT NULL,
            expiry_date DATE,
            image_url VARCHAR(255)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Customers (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            firs_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            phone VARCHAR(50) NOT NULL,
            notes TEXT
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Admins (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            user_code VARCHAR(20) NOT NULL,
            permissions_level INTEGER NOT NULL
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Warehouses (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            address VARCHAR(100) NOT NULL,
            name VARCHAR(50) NOT NULL,
            named_geo VARCHAR(50),
            coord_geo VARCHAR(30)
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Storage (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            FOREIGN KEY (warehouse_id) REFERENCES Warehouses(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
        );
    """)

    con.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            order_date DATE,
            FOREIGN KEY (customer_id) REFERENCES Customers(id) ON DELETE CASCADE,
            FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE
        );
    """)


