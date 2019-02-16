import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Statusbar')
        self.statusBar().showMessage( 'Here is Status Bar...')
        self.show()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
