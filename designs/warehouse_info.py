# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_warehouse_info(object):
    def setupUi(self, warehouse_info):
        warehouse_info.setObjectName("warehouse_info")
        warehouse_info.resize(957, 681)
        self.centralwidget = QtWidgets.QWidget(warehouse_info)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(40, 70, 881, 541))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["Товар", "Количество"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 30, 161, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 630, 211, 19))
        self.label.setObjectName("label")
        self.value = QtWidgets.QLabel(self.centralwidget)
        self.value.setGeometry(QtCore.QRect(260, 630, 251, 19))
        self.value.setObjectName("value")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 10, 71, 19))
        self.label_2.setObjectName("label_2")
        warehouse_info.setCentralWidget(self.centralwidget)

        self.retranslateUi(warehouse_info)
        QtCore.QMetaObject.connectSlotsByName(warehouse_info)

        # Initialize data and setup connections
        self.database_path = "warehouse.db"  # Путь к базе данных
        self.setupData()
        self.comboBox.currentIndexChanged.connect(self.updateTableAndValue)

    def retranslateUi(self, warehouse_info):
        _translate = QtCore.QCoreApplication.translate
        warehouse_info.setWindowTitle(_translate("warehouse_info", "Информация о складах"))
        self.label.setText(_translate("warehouse_info", "Общее количество товара:"))
        self.value.setText(_translate("warehouse_info", "*value*"))
        self.label_2.setText(_translate("warehouse_info", "Склад:"))

    def setupData(self):
        # Подключение к базе данных
        try:
            connection = sqlite3.connect(self.database_path)
            cursor = connection.cursor()

            # Получение списка таблиц (названия складов)
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = [table[0] for table in cursor.fetchall()]

            # Заполнение comboBox названиями складов
            self.comboBox.addItems(tables)

            # Закрытие соединения
            connection.close()

            # Инициализация таблицы и значения
            self.updateTableAndValue()

        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")

    def updateTableAndValue(self):
        # Получение выбранного склада
        selected_warehouse = self.comboBox.currentText()

        if not selected_warehouse:
            return

        # Подключение к базе данных и получение данных из выбранной таблицы
        try:
            connection = sqlite3.connect(self.database_path)
            cursor = connection.cursor()

            # Получение данных из таблицы
            query = f"SELECT product_name, quantity FROM {selected_warehouse};"
            cursor.execute(query)
            items = cursor.fetchall()

            # Обновление таблицы tableWidget
            self.tableWidget.setRowCount(len(items))
            for row, (product_name, quantity) in enumerate(items):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(product_name))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(quantity)))

            # Расчет общего количества товаров
            total_quantity = sum(item[1] for item in items)
            self.value.setText(str(total_quantity))

            # Закрытие соединения
            connection.close()

        except sqlite3.Error as e:
            print(f"Ошибка выполнения запроса: {e}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    warehouse_info = QtWidgets.QMainWindow()
    ui = Ui_warehouse_info()
    ui.setupUi(warehouse_info)
    warehouse_info.show()
    sys.exit(app.exec_())
