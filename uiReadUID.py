# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiReadUID.ui'
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

class readUIDDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(464, 497)
        self.gridLayout_2 = QtGui.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_2.addWidget(self.cancelButton, 1, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(93, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.acceptButton = QtGui.QPushButton(Dialog)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.gridLayout_2.addWidget(self.acceptButton, 1, 1, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 93, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 1, 3, 1, 1)
        self.label = QtGui.QLabel(self.tab)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.serialPortComboBox = QtGui.QComboBox(self.tab)
        self.serialPortComboBox.setObjectName(_fromUtf8("serialPortComboBox"))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.serialPortComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.serialPortComboBox, 0, 1, 1, 1)
        self.toggleButton = QtGui.QPushButton(self.tab)
        self.toggleButton.setObjectName(_fromUtf8("toggleButton"))
        self.gridLayout.addWidget(self.toggleButton, 0, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(85, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 103, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 4, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 3, 3, 1, 1)
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.gridLayout.addWidget(self.listWidget, 1, 0, 4, 3)
        self.selectUIDButton = QtGui.QPushButton(self.tab)
        self.selectUIDButton.setObjectName(_fromUtf8("selectUIDButton"))
        self.gridLayout.addWidget(self.selectUIDButton, 2, 3, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 3)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "LECTOR UID", None))
        self.cancelButton.setText(_translate("Dialog", "Cancelar", None))
        self.acceptButton.setText(_translate("Dialog", "Aceptar", None))
        self.label.setText(_translate("Dialog", "Puerto Serial:", None))
        self.serialPortComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.serialPortComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.serialPortComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.serialPortComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.serialPortComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.toggleButton.setText(_translate("Dialog", "Conectar", None))
        self.selectUIDButton.setText(_translate("Dialog", "Seleccionar UID:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Leer UID", None))

