from qtf import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QProgressBar, QVBoxLayout




class Engez(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_txt_file)
        self.pushButton_3.clicked.connect(self.start_script)
        
    def get_txt_file(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Open file')[0]

    def start_script(self):
        with open(self.fname, 'r') as f:
            lines = f.readlines()
            for line in lines:
                print(line)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = Engez()
    widget.show()
    sys.exit(app.exec_())

