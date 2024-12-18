from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_orders(object):
    def setupUi(self, orders):
        orders.setObjectName("orders")
        orders.resize(959, 712)
        self.centralwidget = QtWidgets.QWidget(orders)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 30, 881, 581))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.add_order = QtWidgets.QPushButton(self.centralwidget)
        self.add_order.setGeometry(QtCore.QRect(40, 630, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_order.setFont(font)
        self.add_order.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.add_order.setObjectName("add_order")
        self.remove_order = QtWidgets.QPushButton(self.centralwidget)
        self.remove_order.setGeometry(QtCore.QRect(190, 630, 141, 41))
        self.remove_order.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.remove_order.setObjectName("remove_order")
        self.save_button = QtWidgets.QPushButton(self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(750, 630, 81, 41))
        self.save_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.save_button.setObjectName("save_button")
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(840, 630, 81, 41))
        self.reset_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.reset_button.setObjectName("reset_button")
        orders.setCentralWidget(self.centralwidget)

        self.retranslateUi(orders)
        QtCore.QMetaObject.connectSlotsByName(orders)

    def retranslateUi(self, orders):
        _translate = QtCore.QCoreApplication.translate
        orders.setWindowTitle(_translate("orders", "MainWindow"))
        self.add_order.setText(_translate("orders", "Добавить заказ"))
        self.remove_order.setText(_translate("orders", "Удалить заказ"))
        self.save_button.setText(_translate("orders", "SAVE"))
        self.reset_button.setText(_translate("orders", "RESET"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    orders = QtWidgets.QMainWindow()
    ui = Ui_orders()
    ui.setupUi(orders)
    orders.show()
    sys.exit(app.exec_())
