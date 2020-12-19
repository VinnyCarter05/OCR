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

class MyQProgressDialog(qtw.QProgressDialog):
    def __init__(self, min, max, *args, **kwargs):
        super().__init__(*args,**kwargs)

        icon = qtg.QIcon()
        icon.addPixmap(qtg.QPixmap(":/newPrefix/mfmclogo.ico"), qtg.QIcon.Normal, qtg.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("MFMC OCR")
        self.setLabelText("Loading progress")
        self.setMinimumDuration(0)
        self.setMinimum(min)
        self.setMaximum(max)
        self.iscanceled = False
        self.canceled.connect(self.cancel)
        # self.setMinimum(min)
        # self.setMaximum(max)
        # self.setValue(value)
    def cancel(self):
        self.iscanceled = True

class Worker(qtc.QRunnable):
    '''
    Worker thread

    Inherits from QRunnable to handler worker thread setup, signals and wrap-up.

    :param callback: The function callback to run on this worker thread. Supplied args and
                     kwargs will be passed through to the runner.
    :type callback: function
    :param args: Arguments to pass to the callback function
    :param kwargs: Keywords to pass to the callback function

    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    # @pyqtSlot()
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)
