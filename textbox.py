# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textbox.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowOCR(object):
    def setupUi(self, MainWindowOCR):
        MainWindowOCR.setObjectName("MainWindowOCR")
        MainWindowOCR.resize(1266, 1005)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowOCR.sizePolicy().hasHeightForWidth())
        MainWindowOCR.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindowOCR)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_checks = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_checks.sizePolicy().hasHeightForWidth())
        self.frame_checks.setSizePolicy(sizePolicy)
        self.frame_checks.setMinimumSize(QtCore.QSize(0, 37))
        self.frame_checks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_checks.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_checks.setObjectName("frame_checks")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_checks)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_Filt1 = QtWidgets.QCheckBox(self.frame_checks)
        self.checkBox_Filt1.setObjectName("checkBox_Filt1")
        self.horizontalLayout.addWidget(self.checkBox_Filt1)
        self.checkBox_Filt2 = QtWidgets.QCheckBox(self.frame_checks)
        self.checkBox_Filt2.setObjectName("checkBox_Filt2")
        self.horizontalLayout.addWidget(self.checkBox_Filt2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame_checks)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_Rotate = QtWidgets.QSpinBox(self.frame_checks)
        self.spinBox_Rotate.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_Rotate.setMinimum(-360)
        self.spinBox_Rotate.setMaximum(360)
        self.spinBox_Rotate.setSingleStep(1)
        self.spinBox_Rotate.setDisplayIntegerBase(10)
        self.spinBox_Rotate.setObjectName("spinBox_Rotate")
        self.horizontalLayout.addWidget(self.spinBox_Rotate)
        self.pushButton_CCW = QtWidgets.QPushButton(self.frame_checks)
        self.pushButton_CCW.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Fatcow-Farm-Fresh-Arrow-rotate-anticlockwise.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_CCW.setIcon(icon)
        self.pushButton_CCW.setObjectName("pushButton_CCW")
        self.horizontalLayout.addWidget(self.pushButton_CCW)
        self.pushButton_CW = QtWidgets.QPushButton(self.frame_checks)
        self.pushButton_CW.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Fatcow-Farm-Fresh-Arrow-rotate-clockwise.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_CW.setIcon(icon1)
        self.pushButton_CW.setObjectName("pushButton_CW")
        self.horizontalLayout.addWidget(self.pushButton_CW)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_OCR = QtWidgets.QPushButton(self.frame_checks)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_OCR.setIcon(icon2)
        self.pushButton_OCR.setAutoRepeat(False)
        self.pushButton_OCR.setAutoRepeatDelay(300)
        self.pushButton_OCR.setObjectName("pushButton_OCR")
        self.horizontalLayout.addWidget(self.pushButton_OCR)
        self.gridLayout.addWidget(self.frame_checks, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(425, 550))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 613, 788))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(595, 770))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_Image = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Image.sizePolicy().hasHeightForWidth())
        self.label_Image.setSizePolicy(sizePolicy)
        self.label_Image.setMinimumSize(QtCore.QSize(595, 770))
        self.label_Image.setMaximumSize(QtCore.QSize(595, 770))
        self.label_Image.setAcceptDrops(True)
        self.label_Image.setText("")
        self.label_Image.setPixmap(QtGui.QPixmap(":/newPrefix/mfmc logo 2015.jpg"))
        self.label_Image.setScaledContents(True)
        self.label_Image.setObjectName("label_Image")
        self.verticalLayout.addWidget(self.label_Image)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.pushButton_FirstPage = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_FirstPage.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-Actions-arrow-left-end.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_FirstPage.setIcon(icon3)
        self.pushButton_FirstPage.setObjectName("pushButton_FirstPage")
        self.horizontalLayout_3.addWidget(self.pushButton_FirstPage)
        self.pushButton_PrevPage = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_PrevPage.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-Actions-arrow-left.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_PrevPage.setIcon(icon4)
        self.pushButton_PrevPage.setObjectName("pushButton_PrevPage")
        self.horizontalLayout_3.addWidget(self.pushButton_PrevPage)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.spinBox_Page = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox_Page.setMinimum(1)
        self.spinBox_Page.setObjectName("spinBox_Page")
        self.horizontalLayout_3.addWidget(self.spinBox_Page)
        self.pushButton_NextPage = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_NextPage.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-Actions-arrow-right.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_NextPage.setIcon(icon5)
        self.pushButton_NextPage.setObjectName("pushButton_NextPage")
        self.horizontalLayout_3.addWidget(self.pushButton_NextPage)
        self.pushButton_LastPage = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_LastPage.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-Actions-arrow-right-end.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_LastPage.setIcon(icon6)
        self.pushButton_LastPage.setObjectName("pushButton_LastPage")
        self.horizontalLayout_3.addWidget(self.pushButton_LastPage)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame_3, 2, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(425, 550))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_Document = QtWidgets.QWidget()
        self.tab_Document.setObjectName("tab_Document")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_Document)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.tab_Document)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        self.textEdit_Main = QtWidgets.QTextEdit(self.tab_Document)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_Main.sizePolicy().hasHeightForWidth())
        self.textEdit_Main.setSizePolicy(sizePolicy)
        self.textEdit_Main.setToolTipDuration(0)
        self.textEdit_Main.setObjectName("textEdit_Main")
        self.verticalLayout_2.addWidget(self.textEdit_Main)
        self.tabWidget.addTab(self.tab_Document, "")
        self.tab_Preview = QtWidgets.QWidget()
        self.tab_Preview.setObjectName("tab_Preview")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_Preview)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_Preview)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.pushButton_ToClip = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ToClip.setObjectName("pushButton_ToClip")
        self.horizontalLayout_2.addWidget(self.pushButton_ToClip)
        self.pushButton_Clear = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Clear.setObjectName("pushButton_Clear")
        self.horizontalLayout_2.addWidget(self.pushButton_Clear)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.textEdit_Preview = QtWidgets.QTextEdit(self.tab_Preview)
        self.textEdit_Preview.setObjectName("textEdit_Preview")
        self.verticalLayout_3.addWidget(self.textEdit_Preview)
        self.tabWidget.addTab(self.tab_Preview, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 3, 1)
        MainWindowOCR.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowOCR)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1266, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOCR = QtWidgets.QMenu(self.menubar)
        self.menuOCR.setObjectName("menuOCR")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuRotate = QtWidgets.QMenu(self.menubar)
        self.menuRotate.setObjectName("menuRotate")
        MainWindowOCR.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowOCR)
        self.statusbar.setObjectName("statusbar")
        MainWindowOCR.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindowOCR)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setFloatable(False)
        self.toolBar.setObjectName("toolBar")
        MainWindowOCR.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_File = QtWidgets.QAction(MainWindowOCR)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Folder-open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen_File.setIcon(icon7)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.action_Save = QtWidgets.QAction(MainWindowOCR)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-document-save.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon8)
        self.action_Save.setObjectName("action_Save")
        self.actionSave_As = QtWidgets.QAction(MainWindowOCR)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-document-save-as.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon9)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionQuit = QtWidgets.QAction(MainWindowOCR)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/newPrefix/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionQuit.setIcon(icon10)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCut = QtWidgets.QAction(MainWindowOCR)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-cut.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon11)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindowOCR)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-edit-copy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon12)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindowOCR)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-clipboard.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon13)
        self.actionPaste.setObjectName("actionPaste")
        self.actionOCR_Page = QtWidgets.QAction(MainWindowOCR)
        self.actionOCR_Page.setIcon(icon2)
        self.actionOCR_Page.setObjectName("actionOCR_Page")
        self.actionUndo = QtWidgets.QAction(MainWindowOCR)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-blue-arrow-undo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon14)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindowOCR)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-blue-arrow-redo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon15)
        self.actionRedo.setObjectName("actionRedo")
        self.actionBold = QtWidgets.QAction(MainWindowOCR)
        self.actionBold.setCheckable(True)
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-format-text-bold.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBold.setIcon(icon16)
        self.actionBold.setObjectName("actionBold")
        self.actionItalic = QtWidgets.QAction(MainWindowOCR)
        self.actionItalic.setCheckable(True)
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-format-text-italic.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionItalic.setIcon(icon17)
        self.actionItalic.setObjectName("actionItalic")
        self.actionUnderline = QtWidgets.QAction(MainWindowOCR)
        self.actionUnderline.setCheckable(True)
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-format-text-underline.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUnderline.setIcon(icon18)
        self.actionUnderline.setObjectName("actionUnderline")
        self.actionSelect_all = QtWidgets.QAction(MainWindowOCR)
        self.actionSelect_all.setObjectName("actionSelect_all")
        self.actionAttributions = QtWidgets.QAction(MainWindowOCR)
        self.actionAttributions.setObjectName("actionAttributions")
        self.actionCW90 = QtWidgets.QAction(MainWindowOCR)
        self.actionCW90.setIcon(icon1)
        self.actionCW90.setObjectName("actionCW90")
        self.action180 = QtWidgets.QAction(MainWindowOCR)
        self.action180.setObjectName("action180")
        self.actionCCW90 = QtWidgets.QAction(MainWindowOCR)
        self.actionCCW90.setIcon(icon)
        self.actionCCW90.setObjectName("actionCCW90")
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionSelect_all)
        self.menuOCR.addAction(self.actionOCR_Page)
        self.menuFormat.addAction(self.actionBold)
        self.menuFormat.addAction(self.actionItalic)
        self.menuFormat.addAction(self.actionUnderline)
        self.menuRotate.addAction(self.actionCW90)
        self.menuRotate.addAction(self.action180)
        self.menuRotate.addAction(self.actionCCW90)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuRotate.menuAction())
        self.menubar.addAction(self.menuOCR.menuAction())
        self.toolBar.addAction(self.actionOpen_File)
        self.toolBar.addAction(self.action_Save)
        self.toolBar.addAction(self.actionSave_As)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBold)
        self.toolBar.addAction(self.actionItalic)
        self.toolBar.addAction(self.actionUnderline)

        self.retranslateUi(MainWindowOCR)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindowOCR)

    def retranslateUi(self, MainWindowOCR):
        _translate = QtCore.QCoreApplication.translate
        MainWindowOCR.setWindowTitle(_translate("MainWindowOCR", "MainWindow"))
        self.checkBox_Filt1.setText(_translate("MainWindowOCR", "Filter 1"))
        self.checkBox_Filt2.setText(_translate("MainWindowOCR", "Filter 2"))
        self.label.setText(_translate("MainWindowOCR", "Rotate angle"))
        self.pushButton_OCR.setText(_translate("MainWindowOCR", "Preview OCR"))
        self.label_2.setText(_translate("MainWindowOCR", "Page"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Document), _translate("MainWindowOCR", "Document"))
        self.pushButton_ToClip.setText(_translate("MainWindowOCR", "Copy all to clipboard"))
        self.pushButton_Clear.setText(_translate("MainWindowOCR", "Clear Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_Preview), _translate("MainWindowOCR", "Preview"))
        self.menuFile.setTitle(_translate("MainWindowOCR", "File"))
        self.menuEdit.setTitle(_translate("MainWindowOCR", "Edit"))
        self.menuOCR.setTitle(_translate("MainWindowOCR", "OCR"))
        self.menuFormat.setTitle(_translate("MainWindowOCR", "Format"))
        self.menuRotate.setTitle(_translate("MainWindowOCR", "Rotate"))
        self.toolBar.setWindowTitle(_translate("MainWindowOCR", "toolBar"))
        self.actionOpen_File.setText(_translate("MainWindowOCR", "Open"))
        self.actionOpen_File.setShortcut(_translate("MainWindowOCR", "Ctrl+O"))
        self.action_Save.setText(_translate("MainWindowOCR", "Save"))
        self.action_Save.setShortcut(_translate("MainWindowOCR", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindowOCR", "Save As"))
        self.actionQuit.setText(_translate("MainWindowOCR", "Quit"))
        self.actionCut.setText(_translate("MainWindowOCR", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindowOCR", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindowOCR", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindowOCR", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindowOCR", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindowOCR", "Ctrl+V"))
        self.actionOCR_Page.setText(_translate("MainWindowOCR", "Preview OCR"))
        self.actionUndo.setText(_translate("MainWindowOCR", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindowOCR", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindowOCR", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindowOCR", "Ctrl+Y"))
        self.actionBold.setText(_translate("MainWindowOCR", "Bold"))
        self.actionBold.setShortcut(_translate("MainWindowOCR", "Ctrl+B"))
        self.actionItalic.setText(_translate("MainWindowOCR", "Italic"))
        self.actionItalic.setShortcut(_translate("MainWindowOCR", "Ctrl+I"))
        self.actionUnderline.setText(_translate("MainWindowOCR", "Underline"))
        self.actionUnderline.setShortcut(_translate("MainWindowOCR", "Ctrl+U"))
        self.actionSelect_all.setText(_translate("MainWindowOCR", "Select all"))
        self.actionSelect_all.setShortcut(_translate("MainWindowOCR", "Ctrl+A"))
        self.actionAttributions.setText(_translate("MainWindowOCR", "Attributions"))
        self.actionCW90.setText(_translate("MainWindowOCR", "Rotate 90 CW"))
        self.action180.setText(_translate("MainWindowOCR", "Rotate 180"))
        self.actionCCW90.setText(_translate("MainWindowOCR", "Rotate 90 CCW"))
import textbox_rc
