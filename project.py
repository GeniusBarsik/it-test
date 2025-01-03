import sqlite3 as sl
import re

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
from PyQt5.QtWidgets import QMessageBox


class MainApp(auth, about, menu, insert_customer, phone, order_list, order_button, product_button, warehouse_info, product_editor):
    def __init__(self):
        super().__init__()
        self.con = sl.connect('shop_db')
        self.setup_auth()
        self.lvl_admin = None
        self.what_to_open = None
        self.customer_info = {}

    # ________________________________________НАСТРОЙКА ВИДЖЕТОВ И ИХ СИГНАЛЫ_________________________________
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
        # нужно добавить админы НЕ УДАЛЯТЬ!

        # Отображение
        self.menu_window.show()

    def setup_about(self):
        self.about_window = QtWidgets.QMainWindow()
        self.about_customer = about()
        self.about_customer.setupUi(self.about_window)

        # signals

        # Отображение
        self.about_window.show()

    def setup_insert_customer(self):
        # Открытие окна insert_customer
        self.insert_customer_window = QtWidgets.QMainWindow()
        self.insert_customer = insert_customer()
        self.insert_customer.setupUi(self.insert_customer_window)

        # Signals
        self.insert_customer.to_order_button.clicked.connect(self.add_customer)
        # Отображение
        self.insert_customer_window.show()

    def setup_order_list(self):
        # Открытие окна insert_customer
        self.order_list_window = QtWidgets.QMainWindow()
        self.order_list = order_list()
        self.order_list.setupUi(self.order_list_window)

        # Signals
        self.order_list_window.show()

    # изменил
    def setup_order_button(self):
        self.order_window = QtWidgets.QMainWindow()
        self.orders = order_button()
        self.orders.setupUi(self.order_window)
        self.what_to_open = 'orders'
        # signals
        self.orders.add_order.clicked.connect(self.setup_phone)
        # Отображение
        self.order_window.show()

    def setup_phone(self):
        # Открытие окна phone
        self.phone_window = QtWidgets.QMainWindow()
        self.phone = phone()
        self.phone.setupUi(self.phone_window)

        # Привязка сигнала к методу открытия окна insert_customer
        self.phone.next_button.clicked.connect(self.phone_validate)

        # Отображение
        self.phone_window.show()

    # подгрузка бд из таблицы Customers
    def setup_product_button(self):
        self.product_button_window = QtWidgets.QMainWindow()
        self.products = product_button()
        self.products.setupUi(self.product_button_window)

        # Загрузка данных из базы
        self.load_products_to_widget()

        # Отображение окна
        self.product_button_window.show()

    def setup_warehouse_info(self):
        self.warehouse_info_window = QtWidgets.QMainWindow()
        self.warehouses = warehouse_info()
        self.warehouses.setupUi(self.warehouse_info_window)

        # signals

        # Отображение
        self.warehouse_info_window.show()

    # ________________________________ ФУНКЦИИ СИГНАЛОВ ______________________________________
    # Авторизация

    # Проверка пароля
    def check_pass(self):
        inline_text = self.authorization.lineEdit.text()
        self.lvl_admin = self.validate_code(inline_text)
        if self.lvl_admin:
            self.authorization_window.close()
            self.setup_menu()
        else:
            self.authorization.lineEdit.clear()
            self.msg_box('number_error')

    # Проверка на наличие USER CODE в DB
    def validate_code(self, code):
        with self.con:
            info = self.con.execute('SELECT * FROM Admins WHERE user_code = ?', (code,))
            result = info.fetchall()
            if result:
                return result[0][2]
            else:
                return False

    # _________________________________________________________________________________________
    # Валидация номера телефона (правильный или неправильный ввод)
    def phone_validate(self):
        try:
            number = self.phone.number_edit.text()
            pattern = r'^(25|29|33|44|45|46)\d{7}$'
            if re.match(pattern, number):
                if self.is_number_in_database(number):  # Проверяем есть ли номер  в базе и далее проверяем, какое окно открывать
                    if self.what_to_open == 'orders':
                        self.phone_window.close()
                        self.setup_order_list()
                    elif self.what_to_open == 'customers':
                        self.setup_about()
                else:
                    if self.what_to_open == 'orders':
                        self.customer_info['number'] = number
                        self.setup_insert_customer()
                        print(self.customer_info)
                    elif self.what_to_open == 'customers':
                        pass
            else:
                self.phone.number_edit.clear()
                self.msg_box("not_correct_phone")
        except Exception as e:
            print(e)

    # Есть ли номер в базе данных
    def is_number_in_database(self, number):
        try:
            with self.con:
                info = self.con.execute('SELECT * FROM Customers WHERE phone = ?', (number,))
                info = info.fetchall()
                return info
        except Exception as e:
            print(e)

    # _________________________________________________________________________________________________
    # Добавление клиента
    def add_customer(self):
        try:
            name = self.insert_customer.name_edit.text()
            lastname = self.insert_customer.lastname_edit.text()
            note = self.insert_customer.notes_edit.toPlainText()
            phone = self.customer_info['number']
            if not name or not lastname:
                self.msg_box("critical")
            else:
                self.customer_info['name'] = name
                self.customer_info['lastname'] = lastname
                if not note:
                    self.customer_info['notes'] = ''
                else:
                    self.customer_info['notes'] = note

                with self.con:
                    self.con.execute('INSERT INTO Customers (first_name, last_name, phone, notes) VALUES (?, ?, ?, ?)',
                                     (name, lastname, phone, note))
                    self.msg_box("ok")
        except Exception as e:
            print(e)


    # Msg box
    def msg_box(self, type_):
        msg = QMessageBox()
        if type_ == "critical":
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Заполните обязательные поля!")
            msg.setWindowTitle("Ошибка")
            msg.setInformativeText("Пожалуйста, проверьте ваши данные.")
        elif type_ == "ok":
            msg.setWindowTitle("Действие")
            msg.setIcon(QMessageBox.Information)
            msg.setText("Данные успешно добавлены")
        elif type_ == "number_error":
            msg.setWindowTitle("Действие")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Такого кода администратора не существует")
        elif type_ == "not_correct_phone":
            msg.setWindowTitle("Неверный формат")
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Введенный номер телефона не соответствует формату")

        msg.setStandardButtons(QMessageBox.Ok)

        # Отображаем окно и ждем, пока пользователь его закроет
        msg.exec_()


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


if __name__ == "__main__":
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    sys.exit(app.exec_())
