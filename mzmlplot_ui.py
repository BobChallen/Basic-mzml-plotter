# Form implementation generated from reading ui file 'mzmlplotter.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(386, 415)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 361, 149))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.modeBox = QtWidgets.QComboBox(parent=self.formLayoutWidget)
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.modeBox)
        self.fileselectButton = QtWidgets.QPushButton(parent=self.formLayoutWidget)
        self.fileselectButton.setObjectName("fileselectButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fileselectButton)
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.scannumberSpinbox = QtWidgets.QSpinBox(parent=self.formLayoutWidget)
        self.scannumberSpinbox.setMaximum(9999999)
        self.scannumberSpinbox.setObjectName("scannumberSpinbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.scannumberSpinbox)
        self.fileLineedit = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        self.fileLineedit.setObjectName("fileLineedit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fileLineedit)
        self.label_9 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_9)
        self.mzSpinbox = QtWidgets.QDoubleSpinBox(parent=self.formLayoutWidget)
        self.mzSpinbox.setDecimals(5)
        self.mzSpinbox.setMaximum(1e+17)
        self.mzSpinbox.setObjectName("mzSpinbox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.mzSpinbox)
        self.label_10 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_10)
        self.profileButton = QtWidgets.QRadioButton(parent=self.formLayoutWidget)
        self.profileButton.setChecked(True)
        self.profileButton.setObjectName("profileButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.profileButton)
        self.centroidButton = QtWidgets.QRadioButton(parent=self.formLayoutWidget)
        self.centroidButton.setObjectName("centroidButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.centroidButton)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 170, 361, 164))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 1)
        self.lowxSpinbox = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.lowxSpinbox.setMaximum(9999999.0)
        self.lowxSpinbox.setProperty("value", 200.0)
        self.lowxSpinbox.setObjectName("lowxSpinbox")
        self.gridLayout_2.addWidget(self.lowxSpinbox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)
        self.highySpinbox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.highySpinbox.setMaximum(999999999)
        self.highySpinbox.setObjectName("highySpinbox")
        self.gridLayout_2.addWidget(self.highySpinbox, 3, 2, 1, 1)
        self.lowySpinbox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.lowySpinbox.setObjectName("lowySpinbox")
        self.gridLayout_2.addWidget(self.lowySpinbox, 3, 1, 1, 1)
        self.highscanSpinbox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.highscanSpinbox.setMaximum(999999999)
        self.highscanSpinbox.setObjectName("highscanSpinbox")
        self.gridLayout_2.addWidget(self.highscanSpinbox, 2, 2, 1, 1)
        self.colourBox = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.colourBox.setObjectName("colourBox")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.colourBox.addItem("")
        self.gridLayout_2.addWidget(self.colourBox, 4, 1, 1, 2)
        self.lowscanSpinbox = QtWidgets.QSpinBox(parent=self.gridLayoutWidget)
        self.lowscanSpinbox.setObjectName("lowscanSpinbox")
        self.gridLayout_2.addWidget(self.lowscanSpinbox, 2, 1, 1, 1)
        self.highxSpinbox = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.highxSpinbox.setMaximum(9999999.0)
        self.highxSpinbox.setProperty("value", 3000.0)
        self.highxSpinbox.setObjectName("highxSpinbox")
        self.gridLayout_2.addWidget(self.highxSpinbox, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.widthBox = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.widthBox.setProperty("value", 0.4)
        self.widthBox.setObjectName("widthBox")
        self.gridLayout_2.addWidget(self.widthBox, 5, 1, 1, 2)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 5, 0, 1, 1)
        self.plotButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.plotButton.setGeometry(QtCore.QRect(150, 340, 75, 23))
        self.plotButton.setObjectName("plotButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 386, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Mode:"))
        self.modeBox.setItemText(0, _translate("MainWindow", "Single Scan"))
        self.modeBox.setItemText(1, _translate("MainWindow", "Combine Scans"))
        self.modeBox.setItemText(2, _translate("MainWindow", "Plot TIC"))
        self.modeBox.setItemText(3, _translate("MainWindow", "Plot EIC"))
        self.fileselectButton.setText(_translate("MainWindow", "Select File"))
        self.label_2.setText(_translate("MainWindow", "Scan Number:"))
        self.label_9.setText(_translate("MainWindow", "m/z value for EIC:"))
        self.label_10.setText(_translate("MainWindow", "Data Type:"))
        self.profileButton.setText(_translate("MainWindow", "Profile"))
        self.centroidButton.setText(_translate("MainWindow", "Centroid"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; text-decoration: underline;\">Plot Settings</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Intensity Range:"))
        self.label_5.setText(_translate("MainWindow", "m/z range:"))
        self.label_3.setText(_translate("MainWindow", "Line Colour:"))
        self.colourBox.setItemText(0, _translate("MainWindow", "Black"))
        self.colourBox.setItemText(1, _translate("MainWindow", "Blue"))
        self.colourBox.setItemText(2, _translate("MainWindow", "Red"))
        self.colourBox.setItemText(3, _translate("MainWindow", "Yellow"))
        self.colourBox.setItemText(4, _translate("MainWindow", "Green"))
        self.colourBox.setItemText(5, _translate("MainWindow", "Orange"))
        self.colourBox.setItemText(6, _translate("MainWindow", "Pink"))
        self.label_8.setText(_translate("MainWindow", "Scan Range:"))
        self.label_7.setText(_translate("MainWindow", "Line Width:"))
        self.plotButton.setText(_translate("MainWindow", "Plot"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())