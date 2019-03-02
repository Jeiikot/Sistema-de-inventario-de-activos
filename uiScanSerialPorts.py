# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiScanSerialPorts.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class scanSerialPortsDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(382, 459)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.serialPortComboBox = QtGui.QComboBox(self.tab)
        self.serialPortComboBox.setObjectName(_fromUtf8("serialPortComboBox"))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.serialPortComboBox, 0, 1, 1, 1)
        self.toggleButton = QtGui.QPushButton(self.tab)
        self.toggleButton.setObjectName(_fromUtf8("toggleButton"))
        self.gridLayout_2.addWidget(self.toggleButton, 0, 2, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 340, 318))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_3 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_3.addWidget(self.label_3, 0, 1, 1, 1)
        self.scanSerialPortsListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.scanSerialPortsListWidget.setObjectName(_fromUtf8("scanSerialPortsListWidget"))
        self.gridLayout_3.addWidget(self.scanSerialPortsListWidget, 1, 0, 1, 1)
        self.serialPortsListWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.serialPortsListWidget.setObjectName(_fromUtf8("serialPortsListWidget"))
        self.gridLayout_3.addWidget(self.serialPortsListWidget, 1, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 3)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(220, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.closeButton = QtGui.QPushButton(Dialog)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout.addWidget(self.closeButton, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "ESCANER DE PUERTOS", None))
        self.label.setText(_translate("Dialog", "Puerto:", None))
        self.serialPortComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSBx", None))
        self.serialPortComboBox.setItemText(1, _translate("Dialog", "/dev/ttySx", None))
        self.toggleButton.setText(_translate("Dialog", "Escanear", None))
        self.label_2.setText(_translate("Dialog", "Puerto Escaneados:", None))
        self.label_3.setText(_translate("Dialog", "Puertos Detectados:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Escanear Puertos", None))
        self.closeButton.setText(_translate("Dialog", "Salir", None))

