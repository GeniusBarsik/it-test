# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'order_list.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_order_list(object):
    def setupUi(self, order_list):
        order_list.setObjectName("order_list")
        order_list.resize(959, 712)
        self.centralwidget = QtWidgets.QWidget(order_list)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 30, 881, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_pos = QtWidgets.QPushButton(self.centralwidget)
        self.add_pos.setGeometry(QtCore.QRect(40, 630, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_pos.setFont(font)
        self.add_pos.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.add_pos.setObjectName("add_pos")
        self.remove_pos = QtWidgets.QPushButton(self.centralwidget)
        self.remove_pos.setGeometry(QtCore.QRect(200, 630, 141, 41))
        self.remove_pos.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.remove_pos.setObjectName("remove_pos")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(840, 630, 81, 41))
        self.reset_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.reset_button.setObjectName("reset_button")
        self.save_order = QtWidgets.QPushButton(self.centralwidget)
        self.save_order.setGeometry(QtCore.QRect(690, 630, 141, 41))
        self.save_order.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.save_order.setObjectName("save_order")
        order_list.setCentralWidget(self.centralwidget)

        self.retranslateUi(order_list)
        QtCore.QMetaObject.connectSlotsByName(order_list)

    def retranslateUi(self, order_list):
        _translate = QtCore.QCoreApplication.translate
        order_list.setWindowTitle(_translate("order_list", "MainWindow"))
        self.add_pos.setText(_translate("order_list", "Добавить позицию"))
        self.remove_pos.setText(_translate("order_list", "Удалить позицию"))
        self.reset_button.setText(_translate("order_list", "Сброс"))
        self.save_order.setText(_translate("order_list", "Добавить заказ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    order_list = QtWidgets.QMainWindow()
    ui = Ui_order_list()
    ui.setupUi(order_list)
    order_list.show()
    sys.exit(app.exec_())
