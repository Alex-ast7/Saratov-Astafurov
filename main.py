import random
import sys

from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_MainWindow



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)
        self.figures = []

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            self.do_paint = False
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        try:
            qp.setBrush(QColor(255, 255, 0))
            r = random.randint(10, 200)
            x = random.randint(0, 554)
            y = random.randint(0, 379)
            self.figures.append((x, y, r))
            for i in self.figures:
                qp.drawEllipse(i[0], i[1], i[2], i[2])
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
