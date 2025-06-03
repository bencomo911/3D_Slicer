from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMessageBox
from slicer_project.backend.matlab_backend import run_matlab_slicer


class Ui_MainWindow(object):
    # print settings
    print_settings = []
    
    # Action function
    def get_layerHeight(self):
        # get current value
        value = self.layerHeight_spinbox.value()
        # add layerHeight to settings list 
        self.print_settings.append(value)
        print("layerHeight:", value)
        
    def get_shellThickness(self):
        # get current value
        value = self.shellThickness_spinbox.value()
        self.print_settings.append(value)
        print("shellThickness:", value)
        
    def get_infillDensity(self):
        value = self.infillDensity_spinbox.value()
        self.print_settings.append(value)
        print("infillDensity:", value)
        
    def get_printSpeed(self):
        value = self.printSpeed_spinbox.value()
        self.print_settings.append(value)
        print("printSpeed:", value)
        
    def set_inputFile(self):
        value = self.inputfile_lineEdit.text()
        self.print_settings.append(value)
        print("inputFile:", value)
        
    def set_outputFile(self):
        value = self.outputFile_lineEdit.text()
        self.print_settings.append(value)
        print("outputFile:", value)

    def slice_model(self):
        layer_height = self.layerHeight_spinbox.value()
        shell_thickness = self.shellThickness_spinbox.value()
        infill_density = self.infillDensity_spinbox.value()
        print_speed = self.printSpeed_spinbox.value()
        input_file = self.inputfile_lineEdit.text()
        output_file = self.outputFile_lineEdit.text()

        # Call MATLAB backend
        try:
            run_matlab_slicer(
                layer_height=layer_height,
                shell_thickness=shell_thickness,
                infill_density=infill_density,
                print_speed=print_speed,
                input_stl=input_file,
                output_gcode=output_file
            )
            QtWidgets.QMessageBox.information(None, "Success", "Slicing Completed Successfuly.")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {e}")


    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sliceSettings_tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.sliceSettings_tabWidget.setGeometry(QtCore.QRect(470, 10, 321, 431))
        self.sliceSettings_tabWidget.setObjectName("sliceSettings_tabWidget")
        self.slice_parameters_tab = QtWidgets.QWidget()
        self.slice_parameters_tab.setObjectName("slice_parameters_tab")
        self.formLayoutWidget = QtWidgets.QWidget(self.slice_parameters_tab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 10, 301, 211))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        # Layer Height ----------------------------------------------------------------------------
        # create label
        self.layerHeight_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.layerHeight_label.setObjectName("layerHeight_label")
        # add label to layout
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.layerHeight_label)
        # create spinbox 
        self.layerHeight_spinbox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget, 
            suffix=" (mm)",
            singleStep=0.1)
        # add action to spinbox
        self.layerHeight_spinbox.valueChanged.connect(self.get_layerHeight)
        # create spinbox object variable
        self.layerHeight_spinbox.setObjectName("layerHeight_spinbox")
        # Limit value for layer height to 3 decimals
        self.layerHeight_spinbox.setDecimals(3)
        # add spinbox to layout
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.layerHeight_spinbox)
        # -----------------------------------------------------------------------------------------


        # Shell Thickness ----------------------------------------------------------------------------
        # create label
        self.shellThickness_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.shellThickness_label.setObjectName("shellThickness_label")
        # add label to layout
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.shellThickness_label)
        # create spinbox
        self.shellThickness_spinbox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget, 
            suffix=" (mm)", 
            singleStep=0.1)
        # add action to spinbox
        self.shellThickness_spinbox.valueChanged.connect(self.get_shellThickness)
        # create spinbox object variable
        self.shellThickness_spinbox.setObjectName("shellThickness_spinbox")
        # Limit value for shell thickness to 3 decimals
        self.shellThickness_spinbox.setDecimals(3)
        # add spinbox to layout
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.shellThickness_spinbox)
        # -----------------------------------------------------------------------------------------

        # Infill Density ----------------------------------------------------------------------------
        # create label
        self.infillDensity_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.infillDensity_label.setObjectName("infillDensity_label")
        # add label to layout
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.infillDensity_label)
        # create spinbox
        self.infillDensity_spinbox = QtWidgets.QSpinBox(self.formLayoutWidget,
            suffix= " (0-100%)")
        # add action to spinbox
        self.infillDensity_spinbox.valueChanged.connect(self.get_infillDensity)
        # create spinbox object variable
        self.infillDensity_spinbox.setObjectName("infillDensity_spinbox")
        # Add range for infill density -----------
        self.infillDensity_spinbox.setMinimum(0)
        self.infillDensity_spinbox.setMaximum(100)
        # ----------------------------------------
        # add spinbox to layout
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infillDensity_spinbox)
        # -----------------------------------------------------------------------------------------

        # Print Speed ----------------------------------------------------------------------------
        # create label
        self.printSpeed_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.printSpeed_label.setObjectName("printSpeed_label")
        # add label to layout
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.printSpeed_label)
        # create spinbox
        self.printSpeed_spinbox = QtWidgets.QSpinBox(self.formLayoutWidget, 
            suffix=" (mm/s)")
        # add action to spinbox
        self.printSpeed_spinbox.valueChanged.connect(self.get_printSpeed)
        # create spinbox object variable
        self.printSpeed_spinbox.setObjectName("printSpeed_spinbox")
        # Add range for print speed -----------
        self.printSpeed_spinbox.setMinimum(1)
        self.printSpeed_spinbox.setMaximum(100)
        #--------------------------------------
        # add spinbox to layout
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.printSpeed_spinbox)
        # -----------------------------------------------------------------------------------------

        # Input File ----------------------------------------------------------------------------
        # create label
        self.inputFile_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.inputFile_label.setObjectName("inputFile_label")
        # add label to layout
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.inputFile_label)
        # create QLineEdit
        self.inputfile_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        # add action to line edit when enter key is pressed
        self.inputfile_lineEdit.returnPressed.connect(self.set_inputFile)
        # create QLineEdit object variable
        self.inputfile_lineEdit.setObjectName("inputfile_lineEdit")
        # add QLineEdit to layout
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.inputfile_lineEdit)
        # -----------------------------------------------------------------------------------------

        # Output File ----------------------------------------------------------------------------
        # create label
        self.outputFile_label = QtWidgets.QLabel(self.formLayoutWidget)
        # create label object variable
        self.outputFile_label.setObjectName("outputFile_label")
        # add label to layout
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.outputFile_label)
        # create QLineEdit
        self.outputFile_lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        # save output file
        self.outputFile_lineEdit.returnPressed.connect(self.set_outputFile)
        # create QLineEdit object variable
        self.outputFile_lineEdit.setObjectName("outputFile_lineEdit")
        # add QLineEdit to layout
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.outputFile_lineEdit)
        # -----------------------------------------------------------------------------------------

        # Slice Button ----------------------------------------------------------------------------
        # Create the QPushButton
        self.slice_button = QtWidgets.QPushButton("Slice", self.formLayoutWidget)
        self.slice_button.setObjectName("slice_button")
        self.slice_button.clicked.connect(self.slice_model)
        # Add it to the layout
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.slice_button)
        # -----------------------------------------------------------------------------------------



        self.sliceSettings_tabWidget.addTab(self.slice_parameters_tab, "")



        self.infill_options_tab = QtWidgets.QWidget()
        self.infill_options_tab.setObjectName("infill_options_tab")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.infill_options_tab)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 171, 221))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.infillType_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.infillType_label.setObjectName("infillType_label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.infillType_label)
        self.infillType_comboBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.infillType_comboBox.setObjectName("infillType_comboBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infillType_comboBox)
        self.placeholder_label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.placeholder_label.setText("")
        self.placeholder_label.setObjectName("placeholder_label")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.placeholder_label)
        self.sliceSettings_tabWidget.addTab(self.infill_options_tab, "")
        self.modelDisplay_frame = QtWidgets.QFrame(self.centralwidget)
        self.modelDisplay_frame.setGeometry(QtCore.QRect(10, 10, 451, 521))
        self.modelDisplay_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.modelDisplay_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.modelDisplay_frame.setObjectName("modelDisplay_frame")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(680, 460, 111, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("slicer_project/gui/resources/logos/keck_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 24))
        self.menubar.setObjectName("menubar")
        self.menuPrinter_Profile = QtWidgets.QMenu(self.menubar)
        self.menuPrinter_Profile.setObjectName("menuPrinter_Profile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionprinterProfile_icon = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("slicer_project/gui/resources/logos/printer_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionprinterProfile_icon.setIcon(icon)
        self.actionprinterProfile_icon.setObjectName("actionprinterProfile_icon")
        self.actionnewFile_Icon = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("slicer_project/gui/resources/logos/newFile_Icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionnewFile_Icon.setIcon(icon1)
        self.actionnewFile_Icon.setObjectName("actionnewFile_Icon")
        self.menuPrinter_Profile.addAction(self.actionEdit)
        self.menuPrinter_Profile.addAction(self.actionNew)
        self.menubar.addAction(self.menuPrinter_Profile.menuAction())
        self.toolBar.addAction(self.actionprinterProfile_icon)
        self.toolBar.addAction(self.actionnewFile_Icon)

        self.retranslateUi(MainWindow)
        self.sliceSettings_tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

 
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.layerHeight_label.setText(_translate("MainWindow", "Layer Height   :"))
        self.shellThickness_label.setText(_translate("MainWindow", "Shell Thicnkess  :"))
        self.infillDensity_label.setText(_translate("MainWindow", "Infill Density  :"))
        self.printSpeed_label.setText(_translate("MainWindow", "Print Speed  :"))
        self.inputFile_label.setText(_translate("MainWindow", "Input File Name (.stl) :"))
        self.outputFile_label.setText(_translate("MainWindow", "Output File Name (.gcode):"))
        self.sliceSettings_tabWidget.setTabText(self.sliceSettings_tabWidget.indexOf(self.slice_parameters_tab), _translate("MainWindow", "Slice Parameters"))
        self.infillType_label.setText(_translate("MainWindow", "Type :"))
        self.sliceSettings_tabWidget.setTabText(self.sliceSettings_tabWidget.indexOf(self.infill_options_tab), _translate("MainWindow", "Infill Options"))
        self.menuPrinter_Profile.setTitle(_translate("MainWindow", "Printer Profile"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionprinterProfile_icon.setText(_translate("MainWindow", "printerProfile_icon"))
        self.actionnewFile_Icon.setText(_translate("MainWindow", "newFile_Icon"))

def launch_gui():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    launch_gui()



