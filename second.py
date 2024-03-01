import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random


class MainWindow(QMainWindow):
    circles: list[tuple[int, int, int], ...]

    def __init__(self):
        super(MainWindow, self).__init__()
        self.circles = []
        loadUi('UI.ui', self)
        self.button.clicked.connect(self.add_circle)
        self.button.setStyleSheet('background-color: transparent;')

    def add_circle(self):
        try:
            diameter = random.randint(1, 100)
            x = random.randint(diameter // 2, self.size().width() - diameter // 2)
            y = random.randint(diameter // 2, self.size().height() - diameter // 2)
            self.circles.append((x, y, diameter))
        except Exception as e:
            print(e)

    def paintEvent(self, event):
        try:
            painter = QPainter(self)
            painter.begin(self)
            painter.setBrush(QColor(Qt.yellow))
            for x, y, diameter in self.circles:
                painter.drawEllipse(x, y, diameter, diameter)
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
