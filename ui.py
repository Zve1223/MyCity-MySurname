from PyQt5.QtWidgets import QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setFixedSize(400, 400)
        self.button = QPushButton(self)
        self.button.setGeometry(8, 8, self.size().width() - 8 * 2, self.size().height() - 8 * 2)
        self.button.setStyleSheet('background-color: transparent;')
