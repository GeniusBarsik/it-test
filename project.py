import sqlite3 as sl

from designs.authorization import Ui_authorization as auth
from designs.about_customer import Ui_about_customer as about
from designs.main import Ui_Menu as menu
from designs.insert_customer import Ui_insert_customer as insert_customer
from designs.phone import Ui_phone as phone
from designs.order_list import Ui_order_list as order_list
from designs.orders_button import Ui_orders as order_button
from designs.products_button import Ui_products as product_button
from designs.warehouse_info import Ui_warehouse_info as warehouse_info


class MainApp(auth, about, menu, insert_customer, phone, order_list, order_button, product_button, warehouse_info):
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
        #нужно добавить админы НЕУДАЛЯТЬ!

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
        pass

    def setup_phone(self):
        pass

    def setup_order_list(self):
        pass

    def setup_order_button(self):
        self.order_window = QtWidgets.QMainWindow()
        self.orders = order_button()
        self.orders.setupUi(self.order_window)

        #signals

        # Отображение
        self.order_window.show()

    def setup_product_button(self):
        self.product_button_window = QtWidgets.QMainWindow()
        self.products = product_button()
        self.products.setupUi(self.product_button_window)

        # signals

        # Отображение
        self.product_button_window.show()

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
