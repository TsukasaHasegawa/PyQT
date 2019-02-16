import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

def main():
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(1000, 600)
    widget.setWindowTitle('PyQt5 - Sample Window')
    widget.setWindowIcon(QIcon('pythonlogo.png'))
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
