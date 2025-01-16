from PyQt5.QtWidgets import QMessageBox, QApplication
import sys

app = QApplication(sys.argv)

class MsgBox:

    def show_ok_info(self, text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setText(text)
        msg_box.setWindowTitle("Информация")
        msg_box.setStandardButtons(QMessageBox.Ok)

        msg_box.exec()

    def show_err_info(self, text):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setText(text)
        msg_box.setWindowTitle("Ошибка")
        msg_box.setStandardButtons(QMessageBox.Ok)

        msg_box.exec()


message = MsgBox()

if __name__ == "__main__":
    message.show_ok_info('Супер')
    message.show_err_info('Что-то пошло не так')