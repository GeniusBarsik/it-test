# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'phone.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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


    def retranslateUi(self, phone):
        _translate = QtCore.QCoreApplication.translate
        phone.setWindowTitle(_translate("phone", "MainWindow"))
        self.label_5.setText(_translate("phone", "Введите номер телефона клиента:"))
        self.next_button.setText(_translate("phone", "Далее"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    phone = QtWidgets.QMainWindow()
    ui = Ui_phone()
    ui.setupUi(phone)
    phone.show()
    sys.exit(app.exec_())
