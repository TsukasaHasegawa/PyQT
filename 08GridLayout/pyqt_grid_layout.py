import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Grid Layout'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 600
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.verticalBoxLayout = QVBoxLayout()

        self.setupGridLayout()
        self.verticalBoxLayout.addWidget(self.basicGroupBox)

        self.setLayout(self.verticalBoxLayout)

    def setupGridLayout(self):
        self.basicGroupBox = QGroupBox('basic grid layout')
        self.gridLayout = QGridLayout()

        oneButton = QPushButton('1', self)
        oneButton.clicked.connect(self.on_click)

        twoButton = QPushButton('2', self)
        twoButton.clicked.connect(self.on_click)

        threeButton = QPushButton('3', self)
        threeButton.clicked.connect(self.on_click)

        fourButton = QPushButton('4', self)
        fourButton.clicked.connect(self.on_click)

        fiveButton = QPushButton('5', self)
        fiveButton.clicked.connect(self.on_click)

        sixButton = QPushButton('6', self)
        sixButton.clicked.connect(self.on_click)

        sevenButton = QPushButton('7', self)
        sevenButton.clicked.connect(self.on_click)

        eightButton = QPushButton('8', self)
        eightButton.clicked.connect(self.on_click)

        nineButton = QPushButton('9', self)
        nineButton.clicked.connect(self.on_click)

        self.gridLayout.addWidget(oneButton, 0, 0)
        self.gridLayout.addWidget(twoButton, 0, 1)
        self.gridLayout.addWidget(threeButton, 0, 2)

        self.gridLayout.addWidget(fourButton, 1, 0)
        self.gridLayout.addWidget(fiveButton, 1, 1)
        self.gridLayout.addWidget(sixButton, 1, 2)

        self.gridLayout.addWidget(sevenButton, 2, 0)
        self.gridLayout.addWidget(eightButton, 2, 1)
        self.gridLayout.addWidget(nineButton, 2, 2)

        self.basicGroupBox.setLayout(self.gridLayout)


    def on_click(self):
        print('PyQt5 button click')

def main():
    app = QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
