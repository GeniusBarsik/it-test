from qt_interfaces.forms.authorization_form import Ui_Authorization
from qt_interfaces.second_menu.orders_menu import Ui_OrdersMenu
from qt_interfaces.second_menu.products_menu import Ui_ProductMenu
from qt_interfaces.customer_information import Ui_CustomerInfo
from qt_interfaces.menu import Ui_Menu
from qt_interfaces.second_menu.create_order_menu import Ui_OrderCreate
from qt_interfaces.forms.phone_form import Ui_PhoneInput
from qt_interfaces.forms.customer_form import Ui_CustomerForm
from qt_interfaces.forms.product_form import Ui_ProductForm

from database.db_methods import db
from src.models.message_box import message
from models.help_methods import validation

from PyQt5 import QtCore, QtGui, QtWidgets

import sys


# Меню авторизации
class AuthWindow(QtWidgets.QMainWindow, Ui_Authorization):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu = None

        # signals
        self.ok_button.clicked.connect(self.check_admin)

    def check_admin(self):
        info_permissions = db.permissions_level(self.input_auth.text())
        if info_permissions:
            self.close()
            self.menu = MainMenu(info_permissions)
            self.menu.show()
        else:
            message.show_err_info("Неверный код администратора")


# Главное меню
class MainMenu(QtWidgets.QMainWindow, Ui_Menu):
    def __init__(self, permissions_lvl):
        super().__init__()
        self.setupUi(self)
        self.products_menu = ProductMenu()
        self.orders_menu = OrdersMenu()
        self.lvl = permissions_lvl
        self.phone = PhoneInput("customers")

        # signals
        self.products_button.clicked.connect(self.show_products_menu)
        self.orders_button.clicked.connect(self.show_orders_menu)
        self.customers_button.clicked.connect(self.show_customer_info)

    def show_products_menu(self):
        if int(self.lvl) < 2:
            message.show_err_info("У вас недостаточно прав")
        else:
            self.products_menu.show()

    def show_orders_menu(self):
        self.orders_menu.show()
        print("открыто")

    def show_customer_info(self):
        self.phone.show()


# Меню редактора продуктов
class ProductMenu(QtWidgets.QMainWindow, Ui_ProductMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.product_form = ProductForm()

        # signals
        self.add_new_product_button.clicked.connect(self.add_product)
        # self.remove_product_button.clicked.connect()
        # self.edit_product_button.clicked.connect()
        # self.search_by_name_button.clicked.connect()

    def add_product(self):
        self.product_form.show()


# Меню заказов
class OrdersMenu(QtWidgets.QMainWindow, Ui_OrdersMenu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.phone = PhoneInput("orders")

        # signals
        self.add_order_button.clicked.connect(self.add_order)

    def add_order(self):
        self.phone.show()


# Меню редактора информации о клиенте
class CustomerInfo(QtWidgets.QMainWindow, Ui_CustomerInfo):
    def __init__(self, name, lastname, phone, notes):
        super().__init__()
        self.setupUi(self)
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.notes = notes
        self.customer_name_label.setText(name)
        self.customer_phone_label.setText(phone)
        self.custome_lastname_label.setText(lastname)
        # signals


# Форма заполнения номера телефона клиента
class PhoneInput(QtWidgets.QMainWindow, Ui_PhoneInput):
    def __init__(self, info):
        super().__init__()
        self.setupUi(self)

        # сlasses
        self.customer_form = None
        self.customer_info = None
        self.create_order = None

        self.to_open = info

        # signals
        self.next_button.clicked.connect(self.check_phone)

    def check_phone(self):
        phone = self.phone_line_edit.text()
        phone = "".join(phone.split())
        print("ok")
        if not validation.validate_num(phone):
            self.phone_line_edit.clear()

        elif db.is_customer_in_db(phone):
            print("ok33")
            if self.to_open == "customers":
                self.phone_line_edit.clear()
                self.close()
                info = db.select_customer(phone)

                if info:
                    print(info)
                    self.customer_info = CustomerInfo(info[0], info[1], info[2], info[3])
                    self.close()
                    self.customer_info.show()

            elif self.to_open == "orders":
                self.create_order = CreateOrder(phone)
                self.create_order.show()
                self.phone_line_edit.clear()
                self.close()

        else:
            print("ok3")
            if self.to_open == "customers":
                message.show_err_info("Такого клиента не существует")
            elif self.to_open == "orders":
                self.customer_form = CustomerForm("orders", phone_number=phone)
                self.phone_line_edit.clear()
                self.close()
                self.customer_form.show()


# Форма заполнения информации о клиенте
class CustomerForm(QtWidgets.QMainWindow, Ui_CustomerForm):
    def __init__(self, step, phone_number="", name_customer="", lastname_customer="", notes_customer=""):
        super().__init__()
        self.setupUi(self)
        # classes
        self.create_order = None

        self.step = step
        self.phone = phone_number
        self.name = name_customer
        self.lastname = lastname_customer
        self.notes = notes_customer
        self.name_line_edit.setText(self.name)
        self.lastname_line_edit.setText(self.lastname)
        self.phone_line_edit.setText(self.phone)

        # signals
        self.add_or_change_button.clicked.connect(self.add_or_change_customer)

    def add_or_change_customer(self):
        name = self.name_line_edit.text()
        lastname = self.lastname_line_edit.text()
        phone = self.phone_line_edit.text()
        notes = self.notes_text_edit.toPlainText()


        if not validation.validate_name(name):
            self.name_line_edit.clear()
        elif not validation.validate_lastname(lastname):
            self.lastname_line_edit.clear()
        elif not validation.validate_num(phone):
            self.phone_line_edit.clear()
        else:
            if self.step == "orders":
                db.add_customer_to_db(name, lastname, phone, notes=notes)
                self.name_line_edit.clear()
                self.lastname_line_edit.clear()
                self.phone_line_edit.clear()
                self.notes_text_edit.clear()
                self.close()
                self.create_order = CreateOrder(phone)
                self.create_order.show()

# Меню составления заказа
class CreateOrder(QtWidgets.QMainWindow, Ui_OrderCreate):
    def __init__(self, phone):
        super().__init__()
        self.setupUi(self)
        self.phone = phone
        # signals

# Форма заполнения продукта
class ProductForm(QtWidgets.QMainWindow, Ui_ProductForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # signals


app = QtWidgets.QApplication(sys.argv)  # Создаем экземпляр QApplication
a = AuthWindow() # Создаем окно авторизации
a.show()  # Показываем окно
sys.exit(app.exec_())