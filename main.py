from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QTextEdit, QLineEdit, QPushButton, QStyleFactory
from PyQt6.QtGui import QMovie, QPainter, QPixmap
import sys
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = Chatbot()

        self.setWindowTitle("My ChatBot")

        self.setMinimumSize(700, 400)
        self.setFixedSize(700, 400)

        self.setStyleSheet("background-color: #606c97")

        # Add image
        self.movie = QMovie("image/bot.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 580, 320)
        self.chat_area.setReadOnly(True)
        self.chat_area.setStyleSheet("background-color: #ffdead; "
                                     "font-family: times; "
                                     "font-size: 20px")

        # Add the input field widget
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 580, 40)
        self.input_field.returnPressed.connect(self.send_message)
        self.input_field.setStyleSheet("background-color: #ffdead; "
                                       "font-family: times; "
                                       "font-size: 20px")

        # Add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(600, 340, 90, 40)
        self.button.clicked.connect(self.send_message)
        self.button.setStyleSheet("background-color: #ffdead; "
                                  "font-family: times; "
                                  "font-size: 20px")

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_repsonse, args=(user_input,))
        thread.start()

    def get_bot_repsonse(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333; background-color: #d3d3d3'>Bot: {response}</p>")

    def paintEvent(self, event):
        current_frame = self.movie.currentPixmap()
        frame_rect = current_frame.rect()
        frame_rect.setX(580)
        frame_rect.setY(0)
        if frame_rect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(frame_rect.left(), frame_rect.top(), current_frame)

app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
