from PyQt5 import QtCore, QtGui
# from slicer_project.backend.matlab_backend import run_matlab_slicer
import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # initialize QMainWindow
        self.setWindowTitle("W.M. Keck Center Slicer")


def main():
    slicer_app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(slicer_app.exec_())

if __name__ == '__main__':
    main()

   

