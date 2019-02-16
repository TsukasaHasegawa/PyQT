import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.setupMenuBar()
        self.setupStatusBar()
        self.show()

    def setupMenuBar(self):
        exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exit_action = QAction(exit_gui, '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application.')
        exit_action.triggered.connect(qApp.quit)

        about_qt_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        about_qt_action = QAction(about_qt_gui, '&About Qt', self)
        about_qt_action.setShortcut('Ctrl+I')
        about_qt_action.setStatusTip('Show Qt Information.')
        about_qt_action.triggered.connect(qApp.aboutQt)

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&Information')
        fileMenu.addAction(about_qt_action)
        fileMenu.addAction(exit_action)
        menuBar.setNativeMenuBar(False)

        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Menu Bar')

    def setupStatusBar(self):
        self.statusBar().showMessage( 'Here is Status Bar...')

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
