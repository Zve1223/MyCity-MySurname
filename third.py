import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import random

from ui import MainWindow


class Circles(MainWindow):
    circles: list[tuple[int, int, int, tuple[int, int, int]], ...]

    def __init__(self):
        super(Circles, self).__init__()
        self.circles = []
        self.button.clicked.connect(self.add_circle)

    def add_circle(self):
        try:
            diameter = random.randint(1, 100)
            x = random.randint(diameter // 2, self.size().width() - diameter // 2)
            y = random.randint(diameter // 2, self.size().height() - diameter // 2)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            self.circles.append((x, y, diameter, color))
        except Exception as e:
            print(e)

    def paintEvent(self, event):
        try:
            painter = QPainter(self)
            painter.begin(self)
            for x, y, diameter, color in self.circles:
                painter.setBrush(QColor(*color))
                painter.drawEllipse(x, y, diameter, diameter)
        except Exception as e:
            print(e)


app = QApplication(sys.argv)
window = Circles()
window.show()
sys.exit(app.exec_())
