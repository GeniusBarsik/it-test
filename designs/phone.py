# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phone.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox #добавил

class Ui_phone(object):
    def setupUi(self, phone, db_connection=None): # просто передал подключение к БД
        phone.setObjectName("phone")
        phone.resize(241, 164)
        self.centralwidget = QtWidgets.QWidget(phone)
        self.centralwidget.setObjectName("centralwidget")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 261, 19))
        self.label_5.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.number_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.number_edit.setGeometry(QtCore.QRect(50, 70, 141, 21))
        self.number_edit.setObjectName("number_edit")
        self.next_button = QtWidgets.QPushButton(self.centralwidget)
        self.next_button.setGeometry(QtCore.QRect(60, 110, 121, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.next_button.setFont(font)
        self.next_button.setObjectName("next_button")
        phone.setCentralWidget(self.centralwidget)

        self.retranslateUi(phone)
        QtCore.QMetaObject.connectSlotsByName(phone)

        # Сохраняем подключение к базе данных, переданное из MainApp
        self.db_connection = db_connection

        # Привязка кнопки "Далее" к методу проверки телефона
        self.next_button.clicked.connect(self.check_phone_in_db)

    def retranslateUi(self, phone):
        _translate = QtCore.QCoreApplication.translate
        phone.setWindowTitle(_translate("phone", "MainWindow"))
        self.label_5.setText(_translate("phone", "Введите номер телефона клиента:"))
        self.next_button.setText(_translate("phone", "Далее"))


    def retranslateUi(self, phone):
        _translate = QtCore.QCoreApplication.translate
        phone.setWindowTitle(_translate("phone", "MainWindow"))
        self.label_5.setText(_translate("phone", "Введите номер телефона клиента:"))
        self.next_button.setText(_translate("phone", "Далее"))

# Метод для проверки телефона в базе данных
    def check_phone_in_db(self):
        # Проверяем, передано ли подключение к базе данных
        if not self.db_connection:
            QMessageBox.critical(
                None,
                "Ошибка",
                "Подключение к базе данных отсутствует."
            )
            return
        # Получаем введённый номер телефона
        phone_number = self.number_edit.text()

        # Проверяем телефон в базе данных
        query = "SELECT * FROM Customers WHERE phone = ?"
        try:
            result = self.db_connection.execute(query, (phone_number,)).fetchall()
        except Exception as e:
            QMessageBox.critical(
                None,
                "Ошибка",
                "Не удалось выполнить запрос к базе данных"
            )
            return

        # Отображение результата
        if result:
            if self.open_insert_customer:
                self.open_insert_customer()
        else:
            QMessageBox.warning(
                None,
                "Ошибка",
                f"Телефон {phone_number} отсутствует в базе данных"
            )



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    phone = QtWidgets.QMainWindow()
    ui = Ui_phone()
    ui.setupUi(phone)
    phone.show()
    sys.exit(app.exec_())