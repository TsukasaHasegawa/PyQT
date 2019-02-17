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
        self.setWindowTitle('Select File')
        self.setupUI()
        self.show()

    def setupUI(self):
        # textEdit
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        # action
        file_select_gui = QApplication.style().standardIcon(QStyle.SP_DirIcon)
        file_select_action = QAction(file_select_gui, 'Select File', self)
        file_select_action.setShortcut('Ctrl+O')
        file_select_action.setStatusTip('Select file')
        file_select_action.triggered.connect(self.showDialog)

        # menuBar
        menuBar = self.menuBar()
        menuBar.setNativeMenuBar(False)
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(file_select_action)

    def showDialog(self):
        fileName = QFileDialog.getOpenFileName(self, 'Select file', '/Users/TsukasaHasegawa/')
        if fileName[0]:
            # ファイルを読み込む
            file = open(fileName[0], 'r')
            # TextEditにファイル内容を書き込む
            with file:
                data = file.read()
                self.textEdit.setText(data)

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
