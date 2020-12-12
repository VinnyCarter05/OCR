from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys, os
# import img2pdf
# from PIL import Image, ImageQt

from textbox import Ui_MainWindowOCR
# from welcome3 import Ui_DialogWelcome



class MainWindow(qtw.QMainWindow, Ui_MainWindowOCR):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.filename = ""
        self.openFile()
        self.setupUi(self)

        #connect to slots
        self.actionQuit.triggered.connect (self.close)

        self.show()

    def openFile (self):
        options = qtw.QFileDialog.Options()
        self.filename, _ = qtw.QFileDialog.getOpenFileName(self,"File to OCR","", "PDF files (*.pdf);; All Files (*)", options=options)

if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())
    