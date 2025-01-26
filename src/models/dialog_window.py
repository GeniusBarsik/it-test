import sys
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QLabel, QLineEdit


class WhatWindow(QDialog):
    def __init__(self, to_del, name):
        super().__init__()
        self.setWindowTitle("Подтверждение")
        self.to_del = to_del
        self.name = name
        layout = QVBoxLayout()

        if to_del == "product":
            self.label = QLabel(f"Вы уверены, что хотите удалить продукт {name}?")
            layout.addWidget(self.label)

        #self.line_edit = QLineEdit()
        #layout.addWidget(self.line_edit)

        self.ok = QPushButton("Да")
        self.ok.clicked.connect(self.accept)  # Закрыть диалог при нажатии
        layout.addWidget(self.ok)

        self.cancel = QPushButton("Нет")
        self.cancel.clicked.connect(self.reject)  # Закрыть диалог при нажатии
        layout.addWidget(self.cancel)
        self.setLayout(layout)


class SearchWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Поиск")

        layout = QVBoxLayout()

        self.label = QLabel("Введите любой критерий")
        layout.addWidget(self.label)

        self.search_line_edit = QLineEdit()
        layout.addWidget(self.search_line_edit)

        self.ok = QPushButton("Искать")
        self.ok.clicked.connect(self.accept)  # Закрыть диалог при нажатии
        layout.addWidget(self.ok)

        self.cancel = QPushButton("Отмена")
        self.cancel.clicked.connect(self.reject)  # Закрыть диалог при нажатии
        layout.addWidget(self.cancel)
        self.setLayout(layout)


app = QApplication(sys.argv)