import sqlite3 as sl

from designs.authorization import Ui_authorization as auth
from designs.about_customer import Ui_about_customer as about
from designs.main import Ui_Menu as menu
from designs.insert_customer import Ui_insert_customer as insert_customer
from designs.phone import Ui_phone as phone
from designs.order_list import Ui_order_list as order_list
from designs.products_button import Ui_products as product_button
from designs.warehouse_info import Ui_warehouse_info as warehouse_info
from designs.orders_button import Ui_orders as order_button
from designs.add_products import Ui_ProductEditor as product_editor

class MainApp(auth, about, menu, insert_customer, phone, order_list, order_button, product_button, warehouse_info, product_editor):
    def __init__(self):
        super().__init__()
        self.con = sl.connect('shop_db')
        self.setup_auth()

    # Настройка виджетов

    def setup_auth(self):
        self.authorization_window = QtWidgets.QMainWindow()
        self.authorization = auth()
        self.authorization.setupUi(self.authorization_window)

        # signals
        self.authorization.ok_button.clicked.connect(self.check_pass)

        # Отображение
        self.authorization_window.show()

    def setup_menu(self):
        self.menu_window = QtWidgets.QMainWindow()
        self.main_menu = menu()
        self.main_menu.setupUi(self.menu_window)

        # signals
        self.main_menu.product.clicked.connect(self.setup_product_button)
        self.main_menu.available.clicked.connect(self.setup_warehouse_info)
        self.main_menu.customer.clicked.connect(self.setup_about)
        self.main_menu.order.clicked.connect(self.setup_order_button)
        #нужно добавить админы НЕ УДАЛЯТЬ!

        # Отображение
        self.menu_window.show()

    def setup_about(self):
        self.about_window = QtWidgets.QMainWindow()
        self.about_customer = about()
        self.about_customer.setupUi(self.about_window)

        # signals

        # Отображение
        self.about_window.show()

    def setup_insert_custsomer(self):
        # Открытие окна insert_customer
        self.insert_customer_window = QtWidgets.QMainWindow()
        self.insert_customer = insert_customer()
        self.insert_customer.setupUi(self.insert_customer_window)

        # Отображение
        self.insert_customer_window.show()

    # изменил
    def setup_phone(self):
        # Открытие окна phone
        self.phone_window = QtWidgets.QMainWindow()
        self.phone = phone()
        self.phone.setupUi(self.phone_window, self.con)

        # Привязка сигнала к методу открытия окна insert_customer
        self.phone.open_insert_customer = self.setup_insert_custsomer

        # Отображение
        self.phone_window.show()

    def setup_order_list(self):
        pass

    #изменил
    def setup_order_button(self):
        self.order_window = QtWidgets.QMainWindow()
        self.orders = order_button()
        self.orders.setupUi(self.order_window)

        # signals
        # Привязал signal кнопки с именем add_order
        self.orders.add_order.clicked.connect(self.setup_phone)

        self.order_window.show()

#подгрузка бд из таблицы Customers
    def setup_product_button(self):
        self.product_button_window = QtWidgets.QMainWindow()
        self.products = product_button()
        self.products.setupUi(self.product_button_window)

        # Загрузка данных из базы
        self.load_products_to_widget()


        # Отображение окна
        self.product_button_window.show()

    def load_products_to_widget(self):
        cursor = self.con.cursor()

        cursor.execute("SELECT * FROM Products")
        data = cursor.fetchall()

        table = self.products.tableWidget

        table.setColumnCount(len(cursor.description))
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels([description[0] for description in cursor.description])

        # Заполнение таблицы данными
        for row_index, row_data in enumerate(data):
            for column_index, value in enumerate(row_data):
                table.setItem(row_index, column_index, QtWidgets.QTableWidgetItem(str(value)))


    def setup_warehouse_info(self):
        self.warehouse_info_window = QtWidgets.QMainWindow()
        self.warehouses = warehouse_info()
        self.warehouses.setupUi(self.warehouse_info_window)

        # signals

        # Отображение
        self.warehouse_info_window.show()

    # Обработка сигналов (их ф-ции)

        # Проверка пароля
    def check_pass(self):
        inline_text = self.authorization.lineEdit.text()
        if self.validate_code(inline_text):
            self.authorization_window.close()
            self.setup_menu()
        else:
            print('Мимо')

    def validate_code(self, code):
        info = self.con.execute('SELECT * FROM Admins WHERE user_code = ?', (code,))
        result = info.fetchall()
        if result:
            return True
        else:
            return False


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
