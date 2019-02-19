import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Box Layout'
        self.left = 10
        self.top = 10
        self.width = 1000
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setupBasicHorizontalLayout()
        self.setupStretchedHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.basicGroupBox)
        windowLayout.addWidget(self.stretchedGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def setupBasicHorizontalLayout(self):
        self.basicGroupBox = QGroupBox('basic buttons')
        basicLayout = QHBoxLayout()

        leftButton = QPushButton('Left', self)
        leftButton.setCheckable(False)
        leftButton.clicked.connect(self.on_click)
        basicLayout.addWidget(leftButton)

        centerButton = QPushButton('Center', self)
        centerButton.setCheckable(False)
        centerButton.clicked.connect(self.on_click)
        basicLayout.addWidget(centerButton)

        rightButton = QPushButton('Right', self)
        rightButton.setCheckable(False)
        rightButton.clicked.connect(self.on_click)
        basicLayout.addWidget(rightButton)

        self.basicGroupBox.setLayout(basicLayout)

    def setupStretchedHorizontalLayout(self):
        self.stretchedGroupBox = QGroupBox('stretched buttons')
        stretchedLayout = QHBoxLayout()

        stretchedLeftButton = QPushButton('Left', self)
        stretchedLeftButton.setCheckable(False)
        stretchedLeftButton.clicked.connect(self.on_click)
        stretchedLayout.addWidget(stretchedLeftButton, 1)

        stretchedCenterButton = QPushButton('Center', self)
        stretchedCenterButton.setCheckable(False)
        stretchedCenterButton.clicked.connect(self.on_click)
        stretchedLayout.addWidget(stretchedCenterButton, 2)

        stretchedRightButton = QPushButton('Right', self)
        stretchedRightButton.setCheckable(False)
        stretchedRightButton.clicked.connect(self.on_click)
        stretchedLayout.addWidget(stretchedRightButton, 3)

        self.stretchedGroupBox.setLayout(stretchedLayout)

    def on_click(self):
        print('PyQt5 button click')

def main():
    app = QApplication(sys.argv)
    widget = Widget()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
