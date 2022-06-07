from qtf import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QProgressBar, QVBoxLayout

        


class Engez(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Engez()
    widget.show()
    sys.exit(app.exec_())

