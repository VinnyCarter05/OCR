from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys, os, shutil

from drag import Ui_MainWindow

class MainWindow(qtw.QMainWindow, Ui_MainWindow):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAcceptDrops(True)
        self.setupUi(self)
        # self.label1.enterEvent.connect(self.lab1)
        # self.label2.enterEvent.connect(self.lab2)
        self.lab = 0

    # def dragEnterEvent(self, e):
    #     print("drag" + self.lab)
    #     # if self.label1.underMouse():
        #     print('label1')
        # else:
        #     print("label2")
        # e.accept()
        # print(e.mimeData().formats())
        # if e.mimeData().hasFormat('text/plain'):
        #     e.accept()
        # else:
        #     e.ignore()

    def lab1(self):
        self.lab = 1

    def lab2(self):
        self.lab = 2

    def dropEvent(self, e):
        if self.label1.underMouse():
            print("label1")
        elif self.label2.underMouse():
            print ("label2")
        print(e.mimeData().text())

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
    window.show()
       
 
    sys.exit(app.exec_())
