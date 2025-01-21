import re
from src.models.message_box import message
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

class HelpMethod:
    def validate_num(self, num):
        try:
            pattern = r'^\+375(25|33|29|17)\d{3}\d{2}\d{2}$'
            if re.match(pattern, num):
                return True
            message.show_err_info("Неверный формат номера телефона")
            return False
        except Exception as e:
            message.show_err_info(e)

    def validate_name(self, name):
        if " " in name:
            message.show_err_info("Имя не может содержать пробелов")
            return False

        elif not name.isalpha():
            message.show_err_info("Заполните имя клиента")
            return False
        return True

    def validate_lastname(self, lastname):
        if " " in lastname:
            message.show_err_info("Фамилия не может содержать пробелов")
            return False
        elif not lastname.isalpha():
            message.show_err_info("Заполните фамилию клиента")
            return False
        return True



class LoadToWidget:
    def load_info_to_table_widget(self, info, widget):

        print(info)
        widget.setRowCount(len(info))
        widget.setColumnCount(len(info[0]) if info else 0)

        for row_index, row_data in enumerate(info):
            for column_index, item in enumerate(row_data):
                widget.setItem(row_index, column_index, QTableWidgetItem(str(item)))

widget_operation = LoadToWidget()
validation = HelpMethod()