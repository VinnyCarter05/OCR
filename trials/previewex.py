# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindowPreview(object):
    def setupUi(self, MainWindowPreview):
        MainWindowPreview.setObjectName("MainWindowPreview")
        MainWindowPreview.resize(667, 937)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/mfmclogo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowPreview.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindowPreview)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_1 = QtWidgets.QFrame(self.tab_1)
        self.frame_1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_1.setObjectName("frame_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton_ToClip_1 = QtWidgets.QPushButton(self.frame_1)
        self.pushButton_ToClip_1.setObjectName("pushButton_ToClip_1")
        self.horizontalLayout_2.addWidget(self.pushButton_ToClip_1)
        self.pushButton_Clear_1 = QtWidgets.QPushButton(self.frame_1)
        self.pushButton_Clear_1.setObjectName("pushButton_Clear_1")
        self.horizontalLayout_2.addWidget(self.pushButton_Clear_1)
        self.verticalLayout_2.addWidget(self.frame_1)
        self.textEdit_Preview_1 = QtWidgets.QTextEdit(self.tab_1)
        self.textEdit_Preview_1.setObjectName("textEdit_Preview_1")
        self.verticalLayout_2.addWidget(self.textEdit_Preview_1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pushButton_ToClip_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_ToClip_2.setObjectName("pushButton_ToClip_2")
        self.horizontalLayout_3.addWidget(self.pushButton_ToClip_2)
        self.pushButton_Clear_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_Clear_2.setObjectName("pushButton_Clear_2")
        self.horizontalLayout_3.addWidget(self.pushButton_Clear_2)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.textEdit_Preview_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_Preview_2.setObjectName("textEdit_Preview_2")
        self.verticalLayout_3.addWidget(self.textEdit_Preview_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.tab_3)
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.pushButton_ToClip_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_ToClip_3.setObjectName("pushButton_ToClip_3")
        self.horizontalLayout_4.addWidget(self.pushButton_ToClip_3)
        self.pushButton_Clear_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_Clear_3.setObjectName("pushButton_Clear_3")
        self.horizontalLayout_4.addWidget(self.pushButton_Clear_3)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.textEdit_Preview_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_Preview_3.setObjectName("textEdit_Preview_3")
        self.verticalLayout_4.addWidget(self.textEdit_Preview_3)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.tab_4)
        self.frame_4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.pushButton_ToClip_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_ToClip_4.setObjectName("pushButton_ToClip_4")
        self.horizontalLayout_5.addWidget(self.pushButton_ToClip_4)
        self.pushButton_Clear_4 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_Clear_4.setObjectName("pushButton_Clear_4")
        self.horizontalLayout_5.addWidget(self.pushButton_Clear_4)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.textEdit_Preview_4 = QtWidgets.QTextEdit(self.tab_4)
        self.textEdit_Preview_4.setObjectName("textEdit_Preview_4")
        self.verticalLayout_5.addWidget(self.textEdit_Preview_4)
        self.tabWidget.addTab(self.tab_4, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindowPreview.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindowPreview)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 667, 21))
        self.menubar.setObjectName("menubar")
        MainWindowPreview.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindowPreview)
        self.statusbar.setObjectName("statusbar")
        MainWindowPreview.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindowPreview)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName("toolBar")
        MainWindowPreview.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionCut = QtWidgets.QAction(MainWindowPreview)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-cut.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCut.setIcon(icon1)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindowPreview)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-edit-copy.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCopy.setIcon(icon2)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindowPreview)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-clipboard.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPaste.setIcon(icon3)
        self.actionPaste.setObjectName("actionPaste")
        self.actionUndo = QtWidgets.QAction(MainWindowPreview)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-blue-arrow-undo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon4)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindowPreview)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/icons/Saki-NuoveXT-2-Actions-blue-arrow-redo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon5)
        self.actionRedo.setObjectName("actionRedo")
        self.toolBar.addAction(self.actionCut)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actionPaste)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)

        self.retranslateUi(MainWindowPreview)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowPreview)

        self.tabWidget.currentChanged.connect(self.change)
        self.pushButton_ToClip_1.clicked.connect(self.ToClip_clicked)

    def retranslateUi(self, MainWindowPreview):
        _translate = QtCore.QCoreApplication.translate
        MainWindowPreview.setWindowTitle(_translate("MainWindowPreview", "OCR Preview Window"))
        self.pushButton_ToClip_1.setText(_translate("MainWindowPreview", "Copy to Clipboard"))
        self.pushButton_Clear_1.setText(_translate("MainWindowPreview", "Clear Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindowPreview", "Preview 1"))
        self.pushButton_ToClip_2.setText(_translate("MainWindowPreview", "Copy to Clipboard"))
        self.pushButton_Clear_2.setText(_translate("MainWindowPreview", "Clear Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindowPreview", "Preview 2"))
        self.pushButton_ToClip_3.setText(_translate("MainWindowPreview", "Copy to Clipboard"))
        self.pushButton_Clear_3.setText(_translate("MainWindowPreview", "Clear Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindowPreview", "Preview 3"))
        self.pushButton_ToClip_4.setText(_translate("MainWindowPreview", "Copy to Clipboard"))
        self.pushButton_Clear_4.setText(_translate("MainWindowPreview", "Clear Preview"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindowPreview", "Preview 4"))
        self.toolBar.setWindowTitle(_translate("MainWindowPreview", "toolBar"))
        self.actionCut.setText(_translate("MainWindowPreview", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindowPreview", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindowPreview", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindowPreview", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindowPreview", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindowPreview", "Ctrl+V"))
        self.actionUndo.setText(_translate("MainWindowPreview", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindowPreview", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindowPreview", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindowPreview", "Ctrl+Y"))

    def change(self):
        print(self.tabWidget.currentIndex(), self.tabWidget.currentWidget())

    def ToClip_clicked(self):
        self.prog = QtWidgets.QProgressDialog()
        self.prog.setMinimum(0)
        self.prog.setMaximum (4)
        self.prog.setLabelText("Timer")
        self.prog.setValue(2)
        self.prog.show()
import textbox_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindowPreview = QtWidgets.QMainWindow()
    ui = Ui_MainWindowPreview()
    ui.setupUi(MainWindowPreview)
    MainWindowPreview.show()
    sys.exit(app.exec_())