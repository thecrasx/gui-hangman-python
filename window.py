from PySide6.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
import sys

from hangman_ui import HangmanUI
from string import ascii_letters


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.hangman = HangmanUI(self)
        
        self.show()

    
    def keyPressEvent(self, event):
        char = event.text()
        
        if char and char in ascii_letters:
            self.hangman.guess(char)

        return super().keyPressEvent(event)






if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Window()

    sys.exit(app.exec())