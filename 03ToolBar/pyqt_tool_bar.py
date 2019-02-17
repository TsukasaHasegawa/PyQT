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
        self.setWindowTitle('Tool Bar')
        self.setupToolBar()

    def setupToolBar(self):
        exit_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarCloseButton)
        exit_action = QAction(exit_gui, 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        about_qt_gui = QApplication.style().standardIcon(QStyle.SP_TitleBarMenuButton)
        about_qt_action = QAction(about_qt_gui, 'About Qt', self)
        about_qt_action.setShortcut('Ctrl+I')
        about_qt_action.setStatusTip('Show Qt Information.')
        about_qt_action.triggered.connect(qApp.aboutQt)

        # その他はひとまずアプリを終了するように設定
        play_gui = QApplication.style().standardIcon(QStyle.SP_MediaPlay)
        play_action = QAction(play_gui, 'Play', self)
        play_action.setShortcut('Ctrl+P')
        play_action.triggered.connect(qApp.quit)

        pause_gui = QApplication.style().standardIcon(QStyle.SP_MediaPause)
        pause_action = QAction(pause_gui, 'Pause', self)
        pause_action.setShortcut('Ctrl+T')
        pause_action.triggered.connect(qApp.quit)

        seek_forward_gui = QApplication.style().standardIcon(QStyle.SP_MediaSeekForward)
        seek_forward_action = QAction(seek_forward_gui, 'Seek Forward', self)
        seek_forward_action.setShortcut('Ctrl+F')
        seek_forward_action.triggered.connect(qApp.quit)

        seek_backward_gui = QApplication.style().standardIcon(QStyle.SP_MediaSeekBackward)
        seek_backword_action = QAction(seek_backward_gui, 'Seek Backward', self)
        seek_backword_action.setShortcut('Ctrl+B')
        seek_backword_action.triggered.connect(qApp.quit)

        stop_gui = QApplication.style().standardIcon(QStyle.SP_MediaStop)
        stop_action = QAction(stop_gui, 'Stop', self)
        stop_action.setShortcut('Ctrl+S')
        stop_action.triggered.connect(qApp.quit)

        self.toolBar = self.addToolBar('toolbar')
        self.toolBar.addAction(exit_action)
        self.toolBar.addAction(about_qt_action)
        self.toolBar.addAction(play_action)
        self.toolBar.addAction(pause_action)
        self.toolBar.addAction(seek_forward_action)
        self.toolBar.addAction(seek_backword_action)
        self.toolBar.addAction(stop_action)

        self.show()

def main():
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
