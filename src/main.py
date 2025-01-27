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
from models.help_methods import widget_operation

from models.dialog_window import WhatWindow, SearchWindow

from PyQt5 import QtWidgets  # QtCore, QtGui

import sys


class AuthWindow(QtWidgets.QMainWindow, Ui_Authorization):
    """
    Меню авторизации.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Поле экземпляра класса меню
        self.menu = None

        # Подключение сигналов
        self.ok_button.clicked.connect(self.check_admin)

    def check_admin(self):
        """
        Проверяет код администратора.

        Если введенный код корректен, закрывает окно авторизации и
        открывает главное меню. В противном случае отображает сообщение об ошибке.
        """
        info_permissions = db.permissions_level(self.input_auth.text())
        if info_permissions:
            self.close()
            self.menu = MainMenu(info_permissions)
            self.menu.show()
        else:
            message.show_err_info("Неверный код администратора")


class MainMenu(QtWidgets.QMainWindow, Ui_Menu):
    """
    Главное меню приложения.

    Этот класс представляет собой главное меню, в котором пользователи
    могут управлять продуктами, заказами, информацией о клиентах, складами в зависимости
    от их уровня доступа.
    """
    def __init__(self, permissions_lvl: str):
        super().__init__()
        self.setupUi(self)

        # Флаг для информации, что открывать далее
        self.to_open = "customers"

        # Создание экземпляров класса для дальнейшей проходки
        self.products_menu = ProductMenu()
        self.orders_menu = OrdersMenu()
        self.phone = PhoneInput(self.to_open)

        # Уровень доступа пользователя
        self.lvl = permissions_lvl

        # Подключение сигналов
        self.products_button.clicked.connect(self.show_products_menu)
        self.orders_button.clicked.connect(self.show_orders_menu)
        self.customers_button.clicked.connect(self.show_customer_info)
        # self.warehouses_button
        # self.admins_button

    def show_products_menu(self):
        """
        Отображает меню продуктов, если у пользователя достаточно прав.

        Если уровень доступа пользователя ниже 2, выводит сообщение об ошибке.
        """
        if int(self.lvl) < 2:
            message.show_err_info("У вас недостаточно прав")
        else:
            self.products_menu.show()

    def show_orders_menu(self):
        """
        Отображает меню заказов.
        """
        self.orders_menu.show()
        print("открыто")

    def show_customer_info(self):
        """
        Отображает информацию о клиенте.
        """
        self.phone.show()


class ProductMenu(QtWidgets.QMainWindow, Ui_ProductMenu):
    """
    Меню редактора продуктов.

    Этот класс представляет собой интерфейс для управления продуктами,
    включая добавление новых продуктов, редактирование и удаление существующих.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.info = db.take_info_from_bd("Products", self.products_table_widget, "*")
        widget_operation.load_info_to_table_widget(self.info, self.products_table_widget)
        self.products_table_widget.setHorizontalHeaderLabels(db.take_column_names("Products"))

        # Создание экземпляра класса для отображения формы заполнения информации о продукте
        self.product_form = None

        # Подключение сигналов
        self.add_new_product_button.clicked.connect(self.manage_product)
        self.remove_product_button.clicked.connect(self.remove_product)
        self.edit_product_button.clicked.connect(self.edit_product)
        self.search_by_name_button.clicked.connect(self.search_product)
        # self.products_table_widget
        self.sort_combo_box.currentIndexChanged.connect(self.to_sort_combo)
        self.refresh_button.clicked.connect(self.reload_widget)

    def manage_product(self):
        """
        Открывает форму для добавления, редактирования или удаления продукта.
        """
        self.product_form = ProductForm("add_product")
        self.product_form.show()

    def remove_product(self):
        """
        Удаляет продукт из базы данных и обновляет TableWidget
        """
        if not self.products_table_widget.selectedItems():
            message.show_ok_info("Выберите продукт для удаления")
        else:
            self.info = db.take_info_from_bd("Products", self.products_table_widget, "*")
            row = self.products_table_widget.currentRow()
            name = (self.info[row])[2]
            to_del = (self.info[row])[4]
            what = WhatWindow("product", name)
            if what.exec_():
                db.delete_from_db("Products", to_del)
                self.products_table_widget.clearSelection()
                self.reload_widget()
                message.show_ok_info(f"Продукт {name} удален")
            else:
                self.products_table_widget.clearSelection()

    def edit_product(self):
        """
        Изменяет продукт в базе данных и обновляет TableWidget
        """
        if not self.products_table_widget.selectedItems():
            message.show_ok_info("Выберите продукт для изменения")
        else:
            self.info = db.take_info_from_bd("Products", self.products_table_widget, "*")
            row = self.products_table_widget.currentRow()
            _, category, name, price, sku, expiry_date, image_url, features = self.info[row]
            price = str(price)
            try:
                self.product_form = ProductForm("edit_product", name, price, sku, category, image_url, expiry_date, features)
            except Exception as e:
                print(e)
            self.product_form.show()

    def reload_widget(self):
        """
        Обновляет виджет
        """
        self.info = db.take_info_from_bd("Products", self.products_table_widget, "*")
        widget_operation.load_info_to_table_widget(self.info, self.products_table_widget)
        self.products_table_widget.setHorizontalHeaderLabels(db.take_column_names("Products"))

    def search_product(self):
        """
        Выгружает продукты по SKU с совпавшей подстрокой указанной в QDialog LineEdit
        """
        search = SearchWindow()
        search.exec_()
        try:
            to_search = search.search_line_edit.text()
            self.info = db.take_info_from_db_by_param("Products", to_search)
            widget_operation.load_info_to_table_widget(self.info, self.products_table_widget)
            self.products_table_widget.setHorizontalHeaderLabels(db.take_column_names("Products"))
        except Exception as e:
            print(e)

    def to_sort_combo(self):
        text = self.sort_combo_box.currentText()
        d = {"Название":"name", "Номер товара":"SKU", "Цена":"price", "Категория":"category"}
        if not self.checkBox.isChecked():
            info = db.sort_info("Products", d[text])
        else:
            info = db.sort_info("Products", d[text], reverse=True)
        try:
            widget_operation.load_info_to_table_widget(info, self.products_table_widget)
            self.products_table_widget.setHorizontalHeaderLabels(db.take_column_names("Products"))
        except Exception as e:
            print(e)

class OrdersMenu(QtWidgets.QMainWindow, Ui_OrdersMenu):
    """
    Меню заказов.

    Этот класс предоставляет интерфейс для управления заказами,
    включая добавление и удаление.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Параметр, передающий программе информацию, что открывать далее
        self.to_open = "orders"

        # Создание экзмемпляра класса с переданным параметром to_open
        self.phone = PhoneInput(self.to_open)

        # Подключение сигналов
        self.add_order_button.clicked.connect(self.add_order)

    def add_order(self):
        """
        Открывает окно ввода номера телефона для дальнейшей проходки
        "orders"
        """
        self.phone.show()


class CustomerInfo(QtWidgets.QMainWindow, Ui_CustomerInfo):
    """
    Меню редактора информации о клиенте.

    Этот класс предоставляет интерфейс для отображения и редактирования
    информации о клиенте, включая имя, фамилию, телефон и заметки.
    """
    def __init__(self, name, lastname, phone, notes):
        super().__init__()
        self.setupUi(self)

        # Информация о клиенте
        self.name = name
        self.lastname = lastname
        self.phone = phone
        self.notes = notes

        # Заполнение полей формы
        self.customer_name_label.setText(name)
        self.customer_phone_label.setText(phone)
        self.custome_lastname_label.setText(lastname)

        # Подключение сигналов


class PhoneInput(QtWidgets.QMainWindow, Ui_PhoneInput):
    """
    Форма заполнения номера телефона клиента.

    Данный класс представляет собой окно ввода номера телефона,
    с возможностью проверки номера и открытия соответствующих форм
    для существующих или новых (после создания) клиентов.

    :Attributes:
        customer_form (CustomerForm): Форма для создания нового клиента (если требуется).
        customer_info (CustomerInfo): Информация о существующем клиенте и ее изменение.
        create_order (CreateOrder): Меню создания заказа.
        to_open (str): Определяет, какую форму открыть ('customers' или 'orders').
    """
    def __init__(self, info):
        super().__init__()
        self.setupUi(self)

        # Поля создания экзмепляров классов на основании введенных данных
        self.customer_form = None
        self.customer_info = None
        self.create_order = None

        # Задает необходимый параметр для определения следующей формы на открытие
        self.to_open = info

        # Подключение сигналов
        self.next_button.clicked.connect(self.check_phone)

    def check_phone(self):
        """
        Проверяет введенный номер телефона.

        Если номер валиден и существует в базе данных, открывает
        соответствующую форму. В противном случае выводит сообщение об ошибке
        или очищает поле ввода.
        """
        phone = self.phone_line_edit.text()
        phone = "".join(phone.split())
        if not validation.validate_num(phone):
            self.phone_line_edit.clear()

        elif db.is_customer_in_db(phone):
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
            if self.to_open == "customers":
                message.show_err_info("Такого клиента не существует")
            elif self.to_open == "orders":
                self.customer_form = CustomerForm("orders", phone_number=phone)
                self.phone_line_edit.clear()
                self.close()
                self.customer_form.show()


class CustomerForm(QtWidgets.QMainWindow, Ui_CustomerForm):
    """
    Форма заполнения информации о клиенте.

    Этот класс предоставляет интерфейс для добавления или изменения информации
    о клиенте, включая имя, фамилию, телефон и заметки.
    """
    def __init__(self, step, phone_number="", name_customer="", lastname_customer="", notes_customer=""):
        super().__init__()
        self.setupUi(self)

        # Поля экземпляров классов
        self.create_order = None

        # Определяет какая проходка на данный момент
        self.step = step

        # Информация о клиенте
        self.phone = phone_number
        self.name = name_customer
        self.lastname = lastname_customer
        self.notes = notes_customer

        # Предзаполнение полей формы
        self.name_line_edit.setText(self.name)
        self.lastname_line_edit.setText(self.lastname)
        self.phone_line_edit.setText(self.phone)

        # Подключение сигналов
        self.add_or_change_button.clicked.connect(self.add_or_change_customer)

    def add_or_change_customer(self):
        """
        Обрабатывает добавление или изменение информации о клиенте.

        Этот метод собирает данные из полей формы, проверяет их на валидность
        и сохраняет информацию о клиенте в базе данных. Если этап "orders",
        открывается форма создания заказа.
        """
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
                self.notes_text_edit.clear()    # Очищаем поля окна
                self.close()
                self.create_order = CreateOrder(phone)
                self.create_order.show()


class CreateOrder(QtWidgets.QMainWindow, Ui_OrderCreate):
    """
    Меню составления заказа.

    Этот класс предоставляет интерфейс для создания нового заказа,
    включая выбор продуктов и ввод информации о клиенте.
    """
    def __init__(self, phone):
        super().__init__()
        self.setupUi(self)

        # Информация о клиенте
        self.phone = phone

        # Подключение сигналов


class ProductForm(QtWidgets.QMainWindow, Ui_ProductForm):
    """
    Форма заполнения продукта.

    Этот класс предоставляет интерфейс для добавления или редактирования
    информации о продукте, включая название, цену и описание.
    """
    def __init__(self, operation, name='', price='', sku='', category='', image_url='', expiry_date='', features=''):
        super().__init__()
        self.setupUi(self)
        self.operation = operation  # Какая проходка в данный момент

        # Выгрузка информации о продукте в LineEdit
        self.product_name_line_edit.setText(name)
        self.product_price_line_edit.setText(price)
        self.sku_line_edit.setText(sku)
        self.category_line_edit.setText(category)
        self.image_url_line_edit.setText(image_url)
        self.expire_date_line_edit.setText(expiry_date)
        self.textEdit.setText(features)

        if self.operation == "edit_product":
            self.sku_line_edit.setReadOnly(True)
        # sku
        self.sku_to_check = sku

        # Подключение сигналов
        self.add_or_change_button.clicked.connect(self.add_or_edit_product)

    def add_or_edit_product(self):
        name = self.product_name_line_edit.text().strip()
        price = self.product_price_line_edit.text().strip()
        sku = self.sku_line_edit.text().strip()
        category = self.category_line_edit.text().strip()
        image_url = self.image_url_line_edit.text().strip()
        expiry_date = self.expire_date_line_edit.text().strip()
        features = self.textEdit.toPlainText().strip()

        required_keys = (name, sku, category, price)

        if "" not in required_keys:

            if 3 == len([el for el in required_keys[:-1] if len(el) > 3]):
                print(category, name, price, sku, expiry_date, image_url, features)
                if self.operation == "add_product" and not db.is_product_in_db(sku):
                    db.add_product_to_bd(category, name, price, sku, expiry_date, image_url, features)
                    self.product_name_line_edit.clear()
                    self.product_price_line_edit.clear()
                    self.sku_line_edit.clear()
                    self.category_line_edit.clear()
                    self.image_url_line_edit.clear()
                    self.expire_date_line_edit.clear()
                    self.product_price_line_edit.clear()
                    self.close()

                elif self.operation == "edit_product":
                    print(sku, self.sku_line_edit.text())

                    db.edit_product(category, name, price, sku, expiry_date, image_url, features)
                    self.product_name_line_edit.clear()
                    self.product_price_line_edit.clear()
                    self.sku_line_edit.clear()
                    self.category_line_edit.clear()
                    self.image_url_line_edit.clear()
                    self.expire_date_line_edit.clear()
                    self.product_price_line_edit.clear()
                    self.close()

                else:
                    message.show_err_info("Продукт с данным SKU уже есть в базе данных")
            else:
                message.show_err_info("Поле должно содержать больше 3 элементов")
        else:
            message.show_err_info("Заполните обязательные поля")


app = QtWidgets.QApplication(sys.argv)
a = AuthWindow()
a.show()
sys.exit(app.exec_())
