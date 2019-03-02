# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiLogin.ui'
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

class loginMainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(273, 493)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.scrollArea = QtGui.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 231, 342))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout_5 = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_6 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setStyleSheet(_fromUtf8("border-image: url(logo.png);"))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_4 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.serverLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.serverLineEdit.setObjectName(_fromUtf8("serverLineEdit"))
        self.verticalLayout_2.addWidget(self.serverLineEdit)
        self.dataBaseLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.dataBaseLineEdit.setObjectName(_fromUtf8("dataBaseLineEdit"))
        self.verticalLayout_2.addWidget(self.dataBaseLineEdit)
        self.userLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.userLineEdit.setObjectName(_fromUtf8("userLineEdit"))
        self.verticalLayout_2.addWidget(self.userLineEdit)

        self.passwordLineEdit = QtGui.QLineEdit(self.scrollAreaWidgetContents)
        self.passwordLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordLineEdit.setObjectName(_fromUtf8("passwordLineEdit"))

        self.verticalLayout_2.addWidget(self.passwordLineEdit)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 3)
        spacerItem = QtGui.QSpacerItem(70, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.loginButton = QtGui.QPushButton(self.centralwidget)
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.gridLayout_2.addWidget(self.loginButton, 1, 1, 1, 1)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.gridLayout_2.addWidget(self.closeButton, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 273, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArchivo = QtGui.QMenu(self.menubar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.connectAction = QtGui.QAction(MainWindow)
        self.connectAction.setObjectName(_fromUtf8("connectAction"))
        self.closeAction = QtGui.QAction(MainWindow)
        self.closeAction.setObjectName(_fromUtf8("closeAction"))
        self.menuArchivo.addAction(self.connectAction)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.closeAction)
        self.menubar.addAction(self.menuArchivo.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.serverLineEdit, self.dataBaseLineEdit)
        MainWindow.setTabOrder(self.dataBaseLineEdit, self.userLineEdit)
        MainWindow.setTabOrder(self.userLineEdit, self.passwordLineEdit)
        MainWindow.setTabOrder(self.passwordLineEdit, self.loginButton)
        MainWindow.setTabOrder(self.loginButton, self.closeButton)
        MainWindow.setTabOrder(self.closeButton, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.scrollArea)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "INICIO DE SESIÓN", None))
        self.label_4.setText(_translate("MainWindow", "Servidor :", None))
        self.label_3.setText(_translate("MainWindow", "Base de Datos :", None))
        self.label.setText(_translate("MainWindow", "Usuario :", None))
        self.label_2.setText(_translate("MainWindow", "Contraseña :", None))
        self.serverLineEdit.setText(_translate("MainWindow", "127.0.0.1", None))
        self.dataBaseLineEdit.setText(_translate("MainWindow", "SENA INDUSTRIAL", None))
        self.userLineEdit.setText(_translate("MainWindow", "root", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Iniciar Sesión", None))
        self.loginButton.setText(_translate("MainWindow", "Ingresar", None))
        self.closeButton.setText(_translate("MainWindow", "Salir", None))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo", None))
        self.connectAction.setText(_translate("MainWindow", "Conectar", None))
        self.closeAction.setText(_translate("MainWindow", "Salir", None))


