from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 400)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 580, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 580, 40)

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(600, 340, 90, 40)

        self.show()


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())