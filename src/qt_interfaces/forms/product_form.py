# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'product_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductForm(object):
    def setupUi(self, ProductForm):
        ProductForm.setObjectName("ProductForm")
        ProductForm.resize(256, 480)
        self.centralwidget = QtWidgets.QWidget(ProductForm)
        self.centralwidget.setObjectName("centralwidget")
        self.add_or_change_button = QtWidgets.QPushButton(self.centralwidget)
        self.add_or_change_button.setGeometry(QtCore.QRect(60, 440, 131, 23))
        self.add_or_change_button.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.add_or_change_button.setObjectName("add_or_change_button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 61, 16))
        self.label_2.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 210, 201, 16))
        self.label_5.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 191, 16))
        self.label_6.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 310, 121, 16))
        self.label_7.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_7.setObjectName("label_7")
        self.category_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.category_line_edit.setGeometry(QtCore.QRect(20, 30, 211, 20))
        self.category_line_edit.setObjectName("category_line_edit")
        self.product_name_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.product_name_line_edit.setGeometry(QtCore.QRect(20, 80, 211, 20))
        self.product_name_line_edit.setObjectName("product_name_line_edit")
        self.sku_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.sku_line_edit.setGeometry(QtCore.QRect(20, 130, 211, 20))
        self.sku_line_edit.setObjectName("sku_line_edit")
        self.expire_date_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.expire_date_line_edit.setGeometry(QtCore.QRect(20, 230, 211, 20))
        self.expire_date_line_edit.setObjectName("expire_date_line_edit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 330, 211, 91))
        self.textEdit.setObjectName("textEdit")
        self.product_price_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.product_price_line_edit.setGeometry(QtCore.QRect(20, 180, 211, 20))
        self.product_price_line_edit.setObjectName("product_price_line_edit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 191, 16))
        self.label_8.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 260, 201, 16))
        self.label_9.setStyleSheet("font: 10pt \"Segoe UI\";")
        self.label_9.setObjectName("label_9")
        self.image_url_line_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.image_url_line_edit.setGeometry(QtCore.QRect(20, 280, 211, 20))
        self.image_url_line_edit.setObjectName("image_url_line_edit")
        ProductForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductForm)
        QtCore.QMetaObject.connectSlotsByName(ProductForm)

    def retranslateUi(self, ProductForm):
        _translate = QtCore.QCoreApplication.translate
        ProductForm.setWindowTitle(_translate("ProductForm", "Редактор продукта"))
        self.add_or_change_button.setText(_translate("ProductForm", "Добавить/изменить"))
        self.label.setText(_translate("ProductForm", "Категория:"))
        self.label_2.setText(_translate("ProductForm", "Название:"))
        self.label_5.setText(_translate("ProductForm", "Срок годности (годен до д/м/г):"))
        self.label_6.setText(_translate("ProductForm", "Артикул (уникальный номер):"))
        self.label_7.setText(_translate("ProductForm", "Характеристики:"))
        self.expire_date_line_edit.setPlaceholderText(_translate("ProductForm", "*необязательное поле"))
        self.textEdit.setPlaceholderText(_translate("ProductForm", "*необязательное поле"))
        self.label_8.setText(_translate("ProductForm", "Цена:"))
        self.label_9.setText(_translate("ProductForm", "Изображение продукта (URL)"))
        self.image_url_line_edit.setPlaceholderText(_translate("ProductForm", "*необязательное поле"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductForm = QtWidgets.QMainWindow()
    ui = Ui_ProductForm()
    ui.setupUi(ProductForm)
    ProductForm.show()
    sys.exit(app.exec_())
