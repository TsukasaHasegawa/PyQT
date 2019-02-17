import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Slider')
        self.setupSlider()
        self.setupLabel()
        self.show()

    def setupSlider(self):
        slider = QSlider(Qt.Horizontal, self)
        slider.setFocusPolicy(Qt.NoFocus)
        slider.setGeometry(30, 30, 100, 30)
        slider.valueChanged[int].connect(self.changeValue)

    def setupLabel(self):
        self.label = QLabel('0', self)
        self.label.setGeometry(150, 30, 80, 30)

    def changeValue(self, value):
        # スライダーの位置によってラベルの文言を変更する
        self.label.setText(str(value))

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
