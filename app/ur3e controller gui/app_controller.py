from app_gui import *
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.mutex = QMutex()
        self.condition = QWaitCondition()
        self.setupUi(self)



app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()