from PyQt5 import QtCore as qtc, QtGui as qtg, QtWidgets as qtw

class QLabelAcceptDrops(qtw.QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setAcceptDrops(True)
        
    def dragEnterEvent(self,e):
        print(self.text())

class QLabelMouseWheel(qtw.QLabel):
    wheelTurnUp = qtc.pyqtSignal()
    wheelTurnDown = qtc.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.setAcceptDrops(True)
        
    def wheelEvent(self,event):
        #change page shown when while scrolled
        self.y = 0
        delta = event.angleDelta().y()
        self.y += (delta and delta // abs(delta))
        if self.y < 0:
            self.wheelTurnDown.emit()
            # print(-1)
            # self.nextPage()
            return
        else:
            self.wheelTurnUp.emit()
            # print(+1)
            # self.prevPage()
            return

