import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 1000
        self.height = 600
        self.setGeometry(0, 0, self.width, self.height)
        self.setWindowTitle('Line Edit')
        self.setupLineEdit()

    def setupLineEdit(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(10, 10)
        self.lineEdit.resize(300, 60)
        self.show()

        timer = QTimer(self)
        timer.timeout.connect(self.timeDraw)
        timer.start(1000)

    def timeDraw(self):
        date = datetime.datetime.today()
        dateString = date.strftime("%Y-%m-%d %H:%M:%S")
        self.statusBar().showMessage(dateString)
        self.lineEdit.setText(dateString)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
