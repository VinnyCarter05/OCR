from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys, os, shutil
import pdfplumber
from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np
# import img2pdf
# from PIL import Image, ImageQt

from textbox import Ui_MainWindowOCR
from preview import Ui_Preview
# from welcome3 import Ui_DialogWelcome



class MainWindow(qtw.QMainWindow, Ui_MainWindowOCR):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.PDF_file = ""
        self.numPages = 0
        self.curPage = 1
        self.tempPath = "\\OCR10temp"
        self.save_file = ""
        self.saved = True
        

        self.setupUi(self)
        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            # self.fonts,
            # self.fontsize,
            self.actionBold,
            self.actionItalic,
            self.actionUnderline
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]


        self.tabWidget.setCurrentIndex(0)
        self.update_format()
        self.openFile()
        

        

        #connect to slots
        self.actionOpen_File.triggered.connect (self.openFile)
        self.action_Save.triggered.connect (self.save)
        self.actionSave_As.triggered.connect (self.saveAs)
        self.actionQuit.triggered.connect (self.exit)
        self.actionCut.triggered.connect (self.cut_clicked)
        self.actionCopy.triggered.connect (self.copy_clicked)
        self.actionPaste.triggered.connect (self.paste_clicked)
        self.actionOCR_Page.triggered.connect (self.OCR_Page_selected)
        self.actionUndo.triggered.connect (self.undo_clicked)
        self.actionRedo.triggered.connect (self.redo_clicked)
        self.actionBold.toggled.connect (self.bold_toggled)
        self.actionItalic.toggled.connect (self.italic_toggled)
        self.actionUnderline.toggled.connect (self.underline_toggled)
        self.actionSelect_all.triggered.connect (self.select_all_clicked)
        self.actionAttributions.triggered.connect (self.attributions_selected)
        self.textEdit_Main.textChanged.connect (self.textChanged)

        self.textEdit_Main.selectionChanged.connect(self.update_format)
        self.textEdit_Preview.selectionChanged.connect(self.update_format)
        self.tabWidget.currentChanged.connect(self.update_format)

        # self.checkBox_Filt1.stateChanged.connect (self.OCR_Page_selected)
        # self.checkBox_Filt2.stateChanged.connect (self.OCR_Page_selected)
        self.pushButton_OCR.clicked.connect (self.OCR_Page_selected)
        self.pushButton_Clear.clicked.connect (self.Clear_clicked)
        self.pushButton_ToClip.clicked.connect (self.ToClip_clicked)

        self.move(100,25)
        self.show()

       

    def openFile (self):
        #choose PDF file to open
        options = qtw.QFileDialog.Options()
        filename = ""
        filename, _ = qtw.QFileDialog.getOpenFileName(self,"File to OCR","", "PDF files (*.pdf);; All Files (*)", options=options)
        if not filename:
            return
        self.PDF_file = filename
        self.changePDF(self.PDF_file)

    def changePDF (self, pdf_file):
        #change new PDF
        pdf = pdfplumber.open(pdf_file)
        pages = pdf.pages
        if len(pages) == 0:
            return
        self.numPages = len(pages)
        pages = convert_from_path(pdf_file, 350)
        if not os.path.isdir(self.tempPath):
            os.mkdir(self.tempPath)
        i = 1
        for page in pages:
            image_name = os.path.join(self.tempPath, "Page_" + str(i) + ".jpg")
            page.save(image_name, "JPEG")
            i = i+1
        self.curPage = 1
        self.showPage (self.curPage)
###################################################
####################################################
###################################################
    def showPage (self, pageNo):
        #show pageNo in left pane(label_Image)
        image_name = os.path.join(self.tempPath, "Page_" + str(pageNo) + ".jpg")
        if not os.path.exists (image_name):
            image_name = ":/newPrefix/mfmc logo 2015.jpg"
        img = cv2.imread(image_name)
        # height, width, channel = img.shape
        # bytesPerLine = 3 * width
        # if self.checkBox_Gray.isChecked() == True:
        #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #     adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
        #     img = adaptive_threshold
        #     height, width = img.shape
        #     bytesPerLine += 1

        
        
        # qImg = qtg.QImage(img.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888)
        # print ("gray1")
        # self.label_Image.setPixmap(qtg.QPixmap(qImg))
        # print ("gray2")
        
        self.label_Image.setPixmap(qtg.QPixmap(image_name))

    def tesseractPage (self, pageNo):
        # self.widget = Preview (self.tempPath, pageNo, Filt1_state = self.checkBox_Filt1.isChecked(), Filt2_state = self.checkBox_Filt2.isChecked())
        # self.widget.show()
        image_name = os.path.join(self.tempPath, "Page_" + str(pageNo) + ".jpg")
        if not os.path.exists (image_name):
            return
        img = cv2.imread(image_name)
        kernel = np.ones((1,1), np.uint8)
        if self.checkBox_Filt2.isChecked() == True:
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)
            img = cv2.GaussianBlur(img, (5,5), 0)
            img = cv2.medianBlur(img,5)


        if self.checkBox_Filt1.isChecked() == True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
            img = adaptive_threshold
        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        self.textEdit_Preview.setText(text)
        self.tabWidget.setCurrentIndex(1)
        # self.textEdit_Preview.insertPlainText(text)

    def saveAs (self):
        options = qtw.QFileDialog.Options()
        filename = ""
        filename, _ = qtw.QFileDialog.getSaveFileName(self,"Save to file", self.save_file, "text files (*.txt);;HTML files (*.html);; All Files (*)", options=options)
        if filename:
            self.save_file = filename
            self.save()

    def save (self):
        if self.save_file == "":
            self.saveAs()
        else:
            with open(self.save_file, "w", encoding='utf-8') as f2:
                if self.save_file.lower().endswith('.html'):
                    f2.write(self.textEdit_Main.toHtml())
                else:
                    f2.write(self.textEdit_Main.toPlainText())
                self.saved = True

    def exit(self):
        # shutil.rmtree("\OCR10temp", ignore_errors=True)
        if self.saved == False:
            self.save()
        self.close()


#####################
# SLOTS             #
#####################

    def wheelEvent(self,event):
        #change page shown when while scrolled
        self.y = 0
        delta = event.angleDelta().y()
        self.y += (delta and delta // abs(delta))
        if (self.curPage<self.numPages) and (self.y < 0):
            self.curPage += 1 #negative y increase page no
            self.showPage(self.curPage)
        if (self.curPage>1) and (self.y>0):
            self.curPage -= 1
            self.showPage(self.curPage)

    def cut_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.cut()
        else:
            self.textEdit_Preview.cut()
 
    def copy_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.copy()
        else:
            self.textEdit_Preview.copy()
 
    def paste_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.paste()
        else:
            self.textEdit_Preview.paste()

    def undo_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.undo()
        else:
            self.textEdit_Preview.undo()

    def redo_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.redo()
        else:
            self.textEdit_Preview.redo()

    def bold_toggled(self):
        if self.tabWidget.currentIndex() == 0:
            if self.actionBold.isChecked():
                self.textEdit_Main.setFontWeight(qtg.QFont.Bold)
            else:
                self.textEdit_Main.setFontWeight(qtg.QFont.Normal)
        else:
            if self.actionBold.isChecked():
                self.textEdit_Preview.setFontWeight(qtg.QFont.Bold)
            else:
                self.textEdit_Preview.setFontWeight(qtg.QFont.Normal)

    def italic_toggled(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.setFontItalic(self.actionItalic.isChecked())
        else:
            self.textEdit_Preview.setFontItalic(self.actionItalic.isChecked())

    def underline_toggled(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.setFontUnderline(self.actionUnderline.isChecked())
        else:
            self.textEdit_Preview.setFontUnderline(self.actionUnderline.isChecked())

    def select_all_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Main.selectAll()
        else:
            self.textEdit_Preview.selectAll()


    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
        """
        Update the font format toolbar/actions when a new text selection is made. This is neccessary to keep
        toolbars/etc. in sync with the current edit state.
        :return:
        """
        # Disable signals for all format widgets, so changing values here does not trigger further formatting.
        self.block_signals(self._format_actions, True)

        # self.fonts.setCurrentFont(self.editor.currentFont())
        # # Nasty, but we get the font-size as a float but want it was an int
        # self.fontsize.setCurrentText(str(int(self.editor.fontPointSize())))
        if self.tabWidget.currentIndex() == 0:
            self.actionItalic.setChecked(self.textEdit_Main.fontItalic())
            self.actionUnderline.setChecked(self.textEdit_Main.fontUnderline())
            self.actionBold.setChecked(self.textEdit_Main.fontWeight() == qtg.QFont.Bold)
        else:
            self.actionItalic.setChecked(self.textEdit_Preview.fontItalic())
            self.actionUnderline.setChecked(self.textEdit_Preview.fontUnderline())
            self.actionBold.setChecked(self.textEdit_Preview.fontWeight() == qtg.QFont.Bold)

        # self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        # self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        # self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        # self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

 
    def OCR_Page_selected(self):
        self.tesseractPage(self.curPage)

    def attributions_selected(self):
        qtw.QMessageBox.information(self, "MFMC OCR"
            , "Icons by VisualPharm;  http://creativecommons.org/licenses/by-nd/3.0/ web page")

    def Clear_clicked(self):
        self.textEdit_Preview.setText("")

    def ToClip_clicked(self):
        self.textEdit_Preview.selectAll()
        self.textEdit_Preview.copy()

    def keyPressEvent(self, e):
        if e.key() == qtc.Qt.Key_Escape:
            self.exit()

    def closeEvent(self,e):
        self.exit()

    def textChanged(self):
        self.saved = False

'''
##########################
# PREVIEW WIDGET         #
##########################


class Preview(qtw.QWidget, Ui_Preview):
    # Signals

    def __init__(self, tempPath, pageNo=1, Filt1_state = False, Filt2_state = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.tempPath = tempPath
        self.pageNo = pageNo
        self.setupUi(self)
        self.checkBox_Filt1.setCheckState(Filt1_state)
        self.checkBox_Filt2.setCheckState(Filt2_state)

        self.OCR()
        

        #connect to slots
        self.checkBox_Filt1.stateChanged.connect(self.OCR)
        self.checkBox_Filt1.stateChanged.connect(self.OCR)
       


    def OCR (self):
        image_name = os.path.join(self.tempPath, "Page_" + str(self.pageNo) + ".jpg")
        if not os.path.exists (image_name):
            return
        img = cv2.imread(image_name)
        kernel = np.ones((1,1), np.uint8)
        if self.checkBox_Filt2.isChecked() == True:
            img = cv2.dilate(img, kernel, iterations=1)
            img = cv2.erode(img, kernel, iterations=1)
            img = cv2.GaussianBlur(img, (5,5), 0)
            img = cv2.medianBlur(img,5)


        if self.checkBox_Filt1.isChecked() == True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
            img = adaptive_threshold
        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        self.textEdit_Main.setText(text)
        if self.checkBox_Filt2.isChecked() == True:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
            img = adaptive_threshold
        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        print("here")
        self.textEdit_Main.setText(text)
        print("there")

'''


#####################
# MAIN              #
#####################
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())
    