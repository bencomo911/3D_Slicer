from PyQt5 import QtCore, QtGui, QtWidgets
# from slicer_project.backend.matlab_backend import run_matlab_slicer
import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

def window():
    app = QtWidgets.QApplication(sys.argv) # create main window with Application
    wid = QtWidgets.QWidget() # create widget
    wid_label = QtWidgets.QLabel(wid) # create label for widget

    wid_label.setText("Hello world!") # set text
    wid.setGeometry(0,0,200,50) # set position of main window (app) relative to user's screen
    wid_label.move(50,20) # set position of the widget label relative to the right corner of the app
    wid.setWindowTitle("Pyqt5")
    wid.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()

