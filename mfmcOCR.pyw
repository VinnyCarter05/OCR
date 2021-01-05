from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw
import sys, os, shutil
import pdfplumber
# import PyPDF2
# import fitz # import for PyMuPDF
from pdf2image import convert_from_path
import cv2
import pytesseract
import numpy as np
import imutils
import time
import ctypes
myappid = u'MFMC.MFMC-OCR.OCR.10' # set taskbar icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

from textbox import Ui_MainWindowOCR
from preview import Ui_MainWindowPreview
from waiting import Ui_FormWaiting
from loading import Ui_FormLoading
from QOveride import MyQProgressDialog, Worker



class MainWindow(qtw.QMainWindow, Ui_MainWindowOCR):
    # Signals
    saveCurrentPreviewsSignal = qtc.pyqtSignal(bool)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.PDF_file = ""
        self.numPages = 0
        self.curPage = 1
        self.tempPath = "\\OCR10temp"
        self.curImg = np.array([])
        self.curStraightImg = None
        self.curPath = ""
        self.curAngle = 0
        self.curPagePreviews = [] #Different previews of current page as list
        self.save_file = ""
        self.saved = True
        self.mainChanged = True #tracker for whether Main changed
        self.progress = 0
        

        self.setupUi(self)
        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self.window2 = PreviewWindow()
        self.window2.move(850,25)


        self._format_actions = [
            # self.fonts,
            # self.fontsize,
            self.actionBold,
            self.actionItalic,
            self.actionUnderline
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]


        # self.tabWidget.setCurrentIndex(0)
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
        self.actionCW90.triggered.connect (self.CW90_clicked)
        self.actionCCW90.triggered.connect (self.CCW90_clicked)
        self.action180.triggered.connect (self.R180_clicked)
        

        self.textEdit_Main.selectionChanged.connect(self.update_format)
        self.textEdit_Main.textChanged.connect(self.main_Changed)
        self.spinBox_Rotate.valueChanged.connect(self.rotate)
        self.spinBox_Page.valueChanged.connect(self.changePage)

        self.pushButton_OCR.clicked.connect (self.OCR_Page_selected)
        self.pushButton_CW.clicked.connect (self.CW90_clicked)
        self.pushButton_CCW.clicked.connect (self.CCW90_clicked)
        self.pushButton_FirstPage.clicked.connect (self.firstPage)
        self.pushButton_PrevPage.clicked.connect (self.prevPage)
        self.pushButton_NextPage.clicked.connect (self.nextPage)
        self.pushButton_LastPage.clicked.connect (self.lastPage)
        self.label_Image.wheelTurnUp.connect(self.prevPage)
        self.label_Image.wheelTurnDown.connect(self.nextPage)
        self.label_Image.dropFile.connect(self.dropPDF)

        self.saveCurrentPreviewsSignal.connect (self.saveCurrentPreviews)
        
        

        self.move(100,0)
        self.show()

    def dropPDF(self, filename):
        try:
            _, filename = filename.split('///')
        except:
            try:
                _, filename = filename.split(':')
            except:
                return
        if os.path.isfile(filename) and filename.lower().endswith(".pdf"):
            if not self.saved:
                ans = self.want_to_save()
                if ans == qtw.QMessageBox.Yes:
                    self.save_file()
                elif ans == qtw.QMessageBox.Cancel:
                    return
            self.PDF_file = filename

            # self.loading = Loading()
            # self.loading.show()
            self.setEnabled(False)
            self.window2.setEnabled(False)
            self.window2.hide()
            # qtw.QApplication.processEvents()
            # worker = Worker(self.changePDF, self.PDF_file)
            self.changePDF(self.PDF_file)
            # worker.start()
            # self.progress = 0
            # # high =0
            # while self.progress<1.1:
            #     time.sleep (0.0000000000005)
            #     if self.progress > high and high < 1:
            #         high = self.progress
            #         self.loading.progressBar.setValue(int(high * 100))
            #         qtw.QApplication.processEvents()
            self.label_totalPages.setText(f"of {self.numPages}")

            self.update_spinBox_Rotate (self.curAngle)

            self.window2.hide()
            self.window2.textEdit_Preview_1.setHtml(self.curPagePreviews[self.curPage-1][0])
            self.window2.textEdit_Preview_2.setHtml(self.curPagePreviews[self.curPage-1][1])
            self.window2.textEdit_Preview_3.setHtml(self.curPagePreviews[self.curPage-1][2])
            self.window2.textEdit_Preview_4.setHtml(self.curPagePreviews[self.curPage-1][3])

            self.setEnabled(True)
            self.window2.setEnabled(True)
            # self.loading.close()

            # self.changePDF(self.PDF_file)

    def openFile (self):
        #choose PDF file to open
        if not self.saved:
            ans = self.want_to_save()
            if ans == qtw.QMessageBox.Yes:
                self.save_file()
            elif ans == qtw.QMessageBox.Cancel:
                return
        options = qtw.QFileDialog.Options()
        filename = ""
        filename, _ = qtw.QFileDialog().getOpenFileName(self,"File to OCR","", "PDF files (*.pdf);; All Files (*)", options=options)
        if not filename:
            return
        self.PDF_file = filename

        # self.loading = Loading()
        # self.loading.show()
        self.setEnabled(False)
        self.window2.setEnabled(False)
        self.window2.hide()
        qtw.QApplication.processEvents()
        # worker = Worker(self.changePDF, self.PDF_file)
        # worker.start()
        self.changePDF(self.PDF_file)
        # self.progress = 0
        # high =0
        # while self.progress<1.1:
        #     time.sleep (0.0000000000005)
        #     if self.progress > high and high < 1:
        #         high = self.progress
        #         self.loading.progressBar.setValue(int(high * 100))
        #         qtw.QApplication.processEvents()
        self.label_totalPages.setText(f"of {self.numPages}")

        self.update_spinBox_Rotate (self.curAngle)

        self.window2.textEdit_Preview_1.setHtml(self.curPagePreviews[self.curPage-1][0])
        self.window2.textEdit_Preview_2.setHtml(self.curPagePreviews[self.curPage-1][1])
        self.window2.textEdit_Preview_3.setHtml(self.curPagePreviews[self.curPage-1][2])
        self.window2.textEdit_Preview_4.setHtml(self.curPagePreviews[self.curPage-1][3])

        self.setEnabled(True)
        self.window2.setEnabled(True)
        # self.loading.close()

    def changePDF (self, pdf_file):
        #change new PDF
        # pdf = fitz.open(pdf_file)
        # number_of_pages = pdf.pageCount
        # if number_of_pages == 0:
        #     return
        # self.numPages = number_of_pages
        # self.curPagePreviews = []
        # for i in range(number_of_pages):
        #     page = pdf.loadPage(i)
        #     text = page.getText("text")
        #     if not text:
        #         text = "Direct PDF Text Not Available; Please check Previews 2 - 4"
        #     self.curPagePreviews.append([text,"","",""])



        # pdf = open(pdf_file, 'rb')
        # read_pdf = PyPDF2.PdfFileReader(pdf)
        
        # number_of_pages = read_pdf.getNumPages()
        # if number_of_pages == 0:
        #     return
        # self.numPages = number_of_pages
        # self.curPagePreviews = []
        # for i in range(number_of_pages):
            # page = read_pdf.getPage(i)
            # text = page.extractText()
            # if text == None:
            #     text = "Direct PDF Text Not Available; Please check Previews 2 - 4"
            # self.curPagePreviews.append([text,"","",""])



        pdf = pdfplumber.open(pdf_file)
        pages = pdf.pages
        if len(pages) == 0:
            return
        self.numPages = len(pages)
        self.curPagePreviews = []
        for page in pages:
            text = page.extract_text()
            if text == None:
                text = "Direct PDF Text Not Available; Please check Previews 2 - 4"
            self.curPagePreviews.append([text,"","",""])
        

        self.progress = 0.1
        pages = convert_from_path(pdf_file, 350, poppler_path='.\\poppler-0.68.0\\bin')
        self.progress = 0.5
        if not os.path.isdir(self.tempPath):
            os.mkdir(self.tempPath)
        i = 1
        for page in pages:
            image_name = os.path.join(self.tempPath, "Page_" + str(i) + ".jpg")
            page.save(image_name, "JPEG")
            self.progress = 0.5 + i/self.numPages/2
            i = i+1
        self.setPage(1, new=True)
        self.progress = 2
        return

    def setPage (self, pageNo = 1, new=False):
        self.mainChanged = True
        self.saveCurrentPreviewsSignal.emit(new)
        self.curPage = pageNo
        image_name = os.path.join(self.tempPath, "Page_" + str(pageNo) + ".jpg")
        if not os.path.exists (image_name):
            image_name = ":/newPrefix/mfmc logo 2015.jpg"
        self.curPath = image_name
        self.curImg = cv2.imread(image_name)    
        self.curStraightImg = self.curImg.copy()  

    def showImg (self, img):
        height, width = img.shape[:2]
        bytesPerLine = 3 * width  
        qImg = qtg.QImage(img.data, width, height, bytesPerLine, qtg.QImage.Format_RGB888)
        self.label_Image.setPixmap(qtg.QPixmap(qImg))

    def tesseractPage (self, img):
        self.progress = 0.1
        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        self.progress = 0.4
        self.curPagePreviews[self.curPage-1][1] = text

        kernel = np.ones((1,1), np.uint8)
        img = cv2.dilate(img, kernel, iterations=1)
        img = cv2.erode(img, kernel, iterations=1)
        img = cv2.GaussianBlur(img, (5,5), 0)
        img = cv2.medianBlur(img,5)

        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        self.progress = 0.70
        self.curPagePreviews[self.curPage-1][2] = text

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        adaptive_threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 11)
        img = adaptive_threshold

        text = str(pytesseract.image_to_string(img, config='--psm 6'))
        self.curPagePreviews[self.curPage-1][3] = text
        self.progress = 1.1

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
        if self.saved == False:
            ans = self.want_to_save()
            if ans == qtw.QMessageBox.Cancel:
                return
            elif ans == qtw.QMessageBox.Yes:
                self.save()
        try:
            shutil.rmtree("\OCR10temp", ignore_errors=True)
        except:
            pass

        self.window2.close()
        self.close()

    def want_to_save(self):
        #returns true if want to save unsaved data
        msgBox = qtw.QMessageBox()
        msgBox.setIcon(qtw.QMessageBox.Warning)
        msgBox.setText("Document not saved.  Do you want to save now?")
        msgBox.setWindowTitle("Not Saved Warning")
        msgBox.setStandardButtons(qtw.QMessageBox.Yes | qtw.QMessageBox.No | qtw.QMessageBox.Cancel)
        returnValue = msgBox.exec()
        return returnValue



#####################
# SLOTS             #
#####################

    def saveCurrentPreviews(self, new):
        if not new:
            self.curPagePreviews[self.curPage-1]=[self.window2.textEdit_Preview_1.toHtml(), self.window2.textEdit_Preview_2.toHtml()
                , self.window2.textEdit_Preview_3.toHtml(), self.window2.textEdit_Preview_4.toHtml()]
        else:
            self.curPagePreviews[self.curPage-1][1]=self.window2.textEdit_Preview_2.toHtml()
            self.curPagePreviews[self.curPage-1][2]=self.window2.textEdit_Preview_3.toHtml()
            self.curPagePreviews[self.curPage-1][3]=self.window2.textEdit_Preview_4.toHtml()


    def main_Changed(self):
        self.mainChanged = True

    def preview_Changed(self):
        self.mainChanged = False

    def cut_clicked(self):
        self.textEdit_Main.cut()
 
    def copy_clicked(self):
        self.textEdit_Main.copy()
 
    def paste_clicked(self):
        self.textEdit_Main.paste()

    def undo_clicked(self):
        self.textEdit_Main.undo()

    def redo_clicked(self):
        self.textEdit_Main.redo()

    def bold_toggled(self):
        if self.actionBold.isChecked():
            self.textEdit_Main.setFontWeight(qtg.QFont.Bold)
        else:
            self.textEdit_Main.setFontWeight(qtg.QFont.Normal)

    def italic_toggled(self):
        self.textEdit_Main.setFontItalic(self.actionItalic.isChecked())

    def underline_toggled(self):
        self.textEdit_Main.setFontUnderline(self.actionUnderline.isChecked())

    def select_all_clicked(self):
        self.textEdit_Main.selectAll()

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
        self.actionItalic.setChecked(self.textEdit_Main.fontItalic())
        self.actionUnderline.setChecked(self.textEdit_Main.fontUnderline())
        self.actionBold.setChecked(self.textEdit_Main.fontWeight() == qtg.QFont.Bold)

        # self.alignl_action.setChecked(self.editor.alignment() == Qt.AlignLeft)
        # self.alignc_action.setChecked(self.editor.alignment() == Qt.AlignCenter)
        # self.alignr_action.setChecked(self.editor.alignment() == Qt.AlignRight)
        # self.alignj_action.setChecked(self.editor.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

 
    def OCR_Page_selected(self):
        if self.curImg.size == 0:
            return
        # self.waiting = Waiting()
        # self.waiting.show()
        self.setEnabled(False)
        self.window2.setEnabled(False)
        qtw.QApplication.processEvents()
        # worker = Worker(self.tesseractPage, self.curImg)
        # worker.start()
        self.tesseractPage(self.curImg)
        # self.progress = 0
        # high =0
        # while self.progress<1.1:
        #     time.sleep (0.0000000000005)
        #     if self.progress > high:
        #         high = self.progress
        #         self.waiting.progressBar.setValue(int(self.progress*100))
        #         qtw.QApplication.processEvents()
        self.setEnabled(True)
        self.window2.setEnabled(True)
        self.window2.textEdit_Preview_2.setText(self.curPagePreviews[self.curPage-1][1])
        self.window2.textEdit_Preview_3.setText(self.curPagePreviews[self.curPage-1][2])
        self.window2.textEdit_Preview_4.setText(self.curPagePreviews[self.curPage-1][3])
        self.window2.textEdit_Preview_1.setText(self.curPagePreviews[self.curPage-1][0])
        self.window2.show()
        self.window2.activateWindow()

        # self.waiting.close()

    def attributions_selected(self):
        qtw.QMessageBox.information(self, "MFMC OCR"
            , "Icons by VisualPharm;  http://creativecommons.org/licenses/by-nd/3.0/ web page")

    def update_spinBox_Rotate(self, newAngle = 0):
        while newAngle < 0:
            newAngle += 360
        newAngle = newAngle % 360
        self.spinBox_Rotate.setValue(newAngle)
        self.curAngle = newAngle
        self.curImg = imutils.rotate_bound(self.curStraightImg, self.curAngle)
        self.showImg(self.curImg)

    def CW90_clicked(self):
        self.update_spinBox_Rotate(self.curAngle+90)

    def CCW90_clicked(self):
        self.update_spinBox_Rotate(self.curAngle-90)

    def R180_clicked(self):
        self.update_spinBox_Rotate(self.curAngle+180)

    def rotate(self):
        angle = self.spinBox_Rotate.value()
        self.update_spinBox_Rotate(angle)

    def changePage(self):
        if self.spinBox_Page.value() == self.curPage:
            return
        if self.spinBox_Page.value() > self.numPages:
            self.spinBox_Page.setValue(self.numPages)
        elif self.spinBox_Page.value() < 1:
            self.spinBox_Page.setValue(1)
        self.setPage(self.spinBox_Page.value())

        self.update_spinBox_Rotate (self.curAngle)

        self.window2.textEdit_Preview_1.setHtml(self.curPagePreviews[self.curPage-1][0])
        self.window2.textEdit_Preview_2.setHtml(self.curPagePreviews[self.curPage-1][1])
        self.window2.textEdit_Preview_3.setHtml(self.curPagePreviews[self.curPage-1][2])
        self.window2.textEdit_Preview_4.setHtml(self.curPagePreviews[self.curPage-1][3])


    def firstPage(self):
        self.spinBox_Page.setValue(1)
    
    def prevPage(self):
        if self.spinBox_Page.value() <= 1:
            self.spinBox_Page.setValue(1)
            return
        self.spinBox_Page.setValue(self.spinBox_Page.value() - 1)
    
    def nextPage(self):
        if self.spinBox_Page.value() >= self.numPages:
            self.spinBox_Page.setValue(self.numPages)
            return
        self.spinBox_Page.setValue(self.spinBox_Page.value() + 1)
    
    def lastPage(self):
        self.spinBox_Page.setValue(self.numPages)
    
    def keyPressEvent(self, e):
        if e.key() == qtc.Qt.Key_Escape:
            self.exit()

    def closeEvent(self,e):
        self.exit()

    def textChanged(self):
        self.saved = False


##########################
# PREVIEW WIDGET         #
##########################


class PreviewWindow(qtw.QMainWindow, Ui_MainWindowPreview):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.setupUi(self)
    
        self.actionCut.triggered.connect (self.cut_clicked)
        self.actionCopy.triggered.connect (self.copy_clicked)
        self.actionPaste.triggered.connect (self.paste_clicked)
        self.actionUndo.triggered.connect (self.undo_clicked)
        self.actionRedo.triggered.connect (self.redo_clicked)

        self.pushButton_Clear_1.clicked.connect (self.Clear_clicked)
        self.pushButton_ToClip_1.clicked.connect (self.ToClip_clicked)
        self.pushButton_Clear_2.clicked.connect (self.Clear_clicked)
        self.pushButton_ToClip_2.clicked.connect (self.ToClip_clicked)
        self.pushButton_Clear_3.clicked.connect (self.Clear_clicked)
        self.pushButton_ToClip_3.clicked.connect (self.ToClip_clicked)
        self.pushButton_Clear_4.clicked.connect (self.Clear_clicked)
        self.pushButton_ToClip_4.clicked.connect (self.ToClip_clicked)


    #########################
    # SLOTS                 #
    #########################

    def cut_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.cut()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.cut()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.cut()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.cut()
 
    def copy_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.copy()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.copy()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.copy()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.copy()
 
    def paste_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.paste()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.paste()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.paste()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.paste()
 
    def undo_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.undo()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.undo()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.undo()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.undo()
 
    def redo_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.redo()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.redo()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.redo()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.redo()

    def Clear_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.clear()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.clear()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.clear()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.clear()

    def ToClip_clicked(self):
        if self.tabWidget.currentIndex() == 0:
            self.textEdit_Preview_1.selectAll()
            self.textEdit_Preview_1.copy()
        elif self.tabWidget.currentIndex() == 1:
            self.textEdit_Preview_2.selectAll()
            self.textEdit_Preview_2.copy()
        elif self.tabWidget.currentIndex() == 2:
            self.textEdit_Preview_3.selectAll()
            self.textEdit_Preview_3.copy()
        elif self.tabWidget.currentIndex() == 3:
            self.textEdit_Preview_4.selectAll()
            self.textEdit_Preview_4.copy()

    def closeEvent(self,e):
        self.setVisible = False

class Loading(qtw.QWidget, Ui_FormLoading):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.setupUi(self)

class Waiting(qtw.QWidget, Ui_FormWaiting):
    # Signals

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #variables
        self.setupUi(self)


        


#####################
# MAIN              #
#####################
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    window = MainWindow()
       
 
    sys.exit(app.exec_())
    