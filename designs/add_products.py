# -*- coding: utf-8 -*-

# Form implementation generated from custom design
# Created using PyQt5

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductEditor(object):
    def setupUi(self, ProductEditor):
        ProductEditor.setObjectName("ProductEditor")
        ProductEditor.resize(800, 500)
        self.centralwidget = QtWidgets.QWidget(ProductEditor)
        self.centralwidget.setObjectName("centralwidget")
        self.label_sku = QtWidgets.QLabel(self.centralwidget)
        self.label_sku.setGeometry(QtCore.QRect(40, 30, 120, 30))
        self.label_sku.setObjectName("label_sku")
        self.input_sku = QtWidgets.QLineEdit(self.centralwidget)
        self.input_sku.setGeometry(QtCore.QRect(180, 30, 580, 30))
        self.input_sku.setObjectName("input_sku")
        self.label_category = QtWidgets.QLabel(self.centralwidget)
        self.label_category.setGeometry(QtCore.QRect(40, 80, 120, 30))
        self.label_category.setObjectName("label_category")
        self.input_category = QtWidgets.QLineEdit(self.centralwidget)
        self.input_category.setGeometry(QtCore.QRect(180, 80, 580, 30))
        self.input_category.setObjectName("input_category")
        self.label_features = QtWidgets.QLabel(self.centralwidget)
        self.label_features.setGeometry(QtCore.QRect(40, 130, 120, 30))
        self.label_features.setObjectName("label_features")
        self.input_features = QtWidgets.QTextEdit(self.centralwidget)
        self.input_features.setGeometry(QtCore.QRect(180, 130, 580, 100))
        self.input_features.setObjectName("input_features")
        self.label_expiry = QtWidgets.QLabel(self.centralwidget)
        self.label_expiry.setGeometry(QtCore.QRect(40, 250, 150, 30))
        self.label_expiry.setObjectName("label_expiry")
        self.input_expiry = QtWidgets.QLineEdit(self.centralwidget)
        self.input_expiry.setGeometry(QtCore.QRect(180, 250, 580, 30))
        self.input_expiry.setObjectName("input_expiry")
        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(40, 300, 120, 30))
        self.label_image.setObjectName("label_image")
        self.input_image = QtWidgets.QLineEdit(self.centralwidget)
        self.input_image.setGeometry(QtCore.QRect(180, 300, 580, 30))
        self.input_image.setObjectName("input_image")
        self.button_add = QtWidgets.QPushButton(self.centralwidget)
        self.button_add.setGeometry(QtCore.QRect(120, 400, 580, 40))
        self.button_add.setObjectName("button_add")
        ProductEditor.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProductEditor)
        QtCore.QMetaObject.connectSlotsByName(ProductEditor)

    def retranslateUi(self, ProductEditor):
        _translate = QtCore.QCoreApplication.translate
        ProductEditor.setWindowTitle(_translate("ProductEditor", "Редактор продукта"))
        self.label_sku.setText(_translate("ProductEditor", "SKU* (Обязательно):"))
        self.label_category.setText(_translate("ProductEditor", "Категория:"))
        self.label_features.setText(_translate("ProductEditor", "Характеристики:"))
        self.label_expiry.setText(_translate("ProductEditor", "Срок годности:"))
        self.label_image.setText(_translate("ProductEditor", "URL изображения:"))
        self.button_add.setText(_translate("ProductEditor", "Добавить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProductEditor = QtWidgets.QMainWindow()
    ui = Ui_ProductEditor()
    ui.setupUi(ProductEditor)
    ProductEditor.show()
    sys.exit(app.exec_())
