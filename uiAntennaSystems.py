# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiAntennaSystems.ui'
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

class antennaSystemDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(279, 343)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 237, 237))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.antenna1CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna1CheckBox.setObjectName(_fromUtf8("antenna1CheckBox"))
        self.gridLayout_2.addWidget(self.antenna1CheckBox, 0, 0, 1, 1)
        self.antenna1ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna1ComboBox.setObjectName(_fromUtf8("antenna1ComboBox"))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.antenna1ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna1ComboBox, 0, 1, 1, 1)
        self.antenna2CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna2CheckBox.setObjectName(_fromUtf8("antenna2CheckBox"))
        self.gridLayout_2.addWidget(self.antenna2CheckBox, 1, 0, 1, 1)
        self.antenna2ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna2ComboBox.setObjectName(_fromUtf8("antenna2ComboBox"))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.antenna2ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna2ComboBox, 1, 1, 1, 1)
        self.antenna3CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna3CheckBox.setObjectName(_fromUtf8("antenna3CheckBox"))
        self.gridLayout_2.addWidget(self.antenna3CheckBox, 2, 0, 1, 1)
        self.antenna3ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna3ComboBox.setObjectName(_fromUtf8("antenna3ComboBox"))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.antenna3ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna3ComboBox, 2, 1, 1, 1)
        self.antenna4CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna4CheckBox.setObjectName(_fromUtf8("antenna4CheckBox"))
        self.gridLayout_2.addWidget(self.antenna4CheckBox, 3, 0, 1, 1)
        self.antenna4ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna4ComboBox.setObjectName(_fromUtf8("antenna4ComboBox"))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.antenna4ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna4ComboBox, 3, 1, 1, 1)
        self.antenna5CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna5CheckBox.setObjectName(_fromUtf8("antenna5CheckBox"))
        self.gridLayout_2.addWidget(self.antenna5CheckBox, 4, 0, 1, 1)
        self.antenna5ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna5ComboBox.setObjectName(_fromUtf8("antenna5ComboBox"))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.antenna5ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna5ComboBox, 4, 1, 1, 1)
        self.antenna6CheckBox = QtGui.QCheckBox(self.scrollAreaWidgetContents)
        self.antenna6CheckBox.setObjectName(_fromUtf8("antenna6CheckBox"))
        self.gridLayout_2.addWidget(self.antenna6CheckBox, 5, 0, 1, 1)
        self.antenna6ComboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.antenna6ComboBox.setObjectName(_fromUtf8("antenna6ComboBox"))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.antenna6ComboBox.addItem(_fromUtf8(""))
        self.gridLayout_2.addWidget(self.antenna6ComboBox, 5, 1, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(76, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.acceptButton = QtGui.QPushButton(Dialog)
        self.acceptButton.setObjectName(_fromUtf8("acceptButton"))
        self.gridLayout_3.addWidget(self.acceptButton, 1, 1, 1, 1)
        self.cancelButton = QtGui.QPushButton(Dialog)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout_3.addWidget(self.cancelButton, 1, 2, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "SISTEMAS DE ANTENAS", None))
        self.antenna1CheckBox.setText(_translate("Dialog", "Antena 1", None))
        self.antenna1ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna1ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna1ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna1ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna1ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna1ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna1ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna1ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna1ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna1ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna1ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna1ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.antenna2CheckBox.setText(_translate("Dialog", "Antena 2", None))
        self.antenna2ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna2ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna2ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna2ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna2ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna2ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna2ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna2ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna2ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna2ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna2ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna2ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.antenna3CheckBox.setText(_translate("Dialog", "Antena 3", None))
        self.antenna3ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna3ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna3ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna3ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna3ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna3ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna3ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna3ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna3ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna3ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna3ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna3ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.antenna4CheckBox.setText(_translate("Dialog", "Antena 4", None))
        self.antenna4ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna4ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna4ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna4ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna4ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna4ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna4ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna4ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna4ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna4ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna4ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna4ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.antenna5CheckBox.setText(_translate("Dialog", "Antena 5", None))
        self.antenna5ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna5ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna5ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna5ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna5ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna5ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna5ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna5ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna5ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna5ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna5ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna5ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.antenna6CheckBox.setText(_translate("Dialog", "Antena 6", None))
        self.antenna6ComboBox.setItemText(0, _translate("Dialog", "/dev/ttyUSB0", None))
        self.antenna6ComboBox.setItemText(1, _translate("Dialog", "/dev/ttyUSB1", None))
        self.antenna6ComboBox.setItemText(2, _translate("Dialog", "/dev/ttyUSB2", None))
        self.antenna6ComboBox.setItemText(3, _translate("Dialog", "/dev/ttyUSB3", None))
        self.antenna6ComboBox.setItemText(4, _translate("Dialog", "/dev/ttyUSB4", None))
        self.antenna6ComboBox.setItemText(5, _translate("Dialog", "/dev/ttyUSB5", None))
        self.antenna6ComboBox.setItemText(6, _translate("Dialog", "/dev/ttyS0", None))
        self.antenna6ComboBox.setItemText(7, _translate("Dialog", "/dev/ttyS1", None))
        self.antenna6ComboBox.setItemText(8, _translate("Dialog", "/dev/ttyS2", None))
        self.antenna6ComboBox.setItemText(9, _translate("Dialog", "/dev/ttyS3", None))
        self.antenna6ComboBox.setItemText(10, _translate("Dialog", "/dev/ttyS4", None))
        self.antenna6ComboBox.setItemText(11, _translate("Dialog", "/dev/ttyS5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Activar/ Desactivar:", None))
        self.acceptButton.setText(_translate("Dialog", "Aceptar", None))
        self.cancelButton.setText(_translate("Dialog", "Cancelar", None))
