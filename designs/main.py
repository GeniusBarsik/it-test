# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(314, 328)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.customer = QtWidgets.QPushButton(self.centralwidget)
        self.customer.setGeometry(QtCore.QRect(50, 150, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.customer.setFont(font)
        self.customer.setObjectName("customer")
        self.order = QtWidgets.QPushButton(self.centralwidget)
        self.order.setGeometry(QtCore.QRect(50, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.order.setFont(font)
        self.order.setObjectName("order")
        self.product = QtWidgets.QPushButton(self.centralwidget)
        self.product.setGeometry(QtCore.QRect(50, 70, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.product.setFont(font)
        self.product.setObjectName("product")
        self.admins = QtWidgets.QPushButton(self.centralwidget)
        self.admins.setGeometry(QtCore.QRect(50, 270, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.admins.setFont(font)
        self.admins.setObjectName("admins")
        self.available = QtWidgets.QPushButton(self.centralwidget)
        self.available.setGeometry(QtCore.QRect(50, 190, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.available.setFont(font)
        self.available.setObjectName("available")
        Menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "MainWindow"))
        self.customer.setText(_translate("Menu", "Информация о клиенте"))
        self.order.setText(_translate("Menu", "Заказы"))
        self.product.setText(_translate("Menu", "Продукты"))
        self.admins.setText(_translate("Menu", "Admins"))
        self.available.setText(_translate("Menu", "Наличие по складам"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(Menu)
    Menu.show()
    sys.exit(app.exec_())
