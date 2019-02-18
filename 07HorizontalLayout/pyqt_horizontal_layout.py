import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Horizontal Layout'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setupHorizontalLayout()
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def setupHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox('Horizontal buttons!')
        layout = QHBoxLayout()

        leftButton = QPushButton('Left', self)
        leftButton.setCheckable(False)
        leftButton.clicked.connect(self.on_click)
        layout.addWidget(leftButton)

        centerButton = QPushButton('Center', self)
        centerButton.setCheckable(False)
        centerButton.clicked.connect(self.on_click)
        layout.addWidget(centerButton)

        rightButton = QPushButton('Right', self)
        rightButton.setCheckable(False)
        rightButton.clicked.connect(self.on_click)
        layout.addWidget(rightButton)

        self.horizontalGroupBox.setLayout(layout)

    def on_click(self):
        print('PyQt5 button click')

def main():
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
