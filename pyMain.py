#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys  # Variables y funciones que interactuan directamente con el interprete de python
from PyQt4 import QtSql

from uiLogin import *
from uiMain import *
from uiInsert import *
from uiRegister import *
from uiReadUID import *
from uiSerialPort import *
from uiScanSerialPorts import *
from uiAuthorization import *
from uiAntennaSystems import *

import serial, threading, time


global dataBaseGlobal, UIDGlobal, updateData, antennaSystem
global antennaPort, antennaState, defaultSerialPort, serialPortSettings

antennaSystem = ["Antena 1", "Antena 2", "Antena 3", "Antena 4", "Antena 5", "Antena 6"]
antennaPort = [0,0,0,0,0,0]; antennaState = [False, False, False, False, False, False]
serialPortTemp = [6, 3, 0, 0]; updateData = ["Actualizacion de Datos"]
serialPortSettings = ["/dev/ttyUSB0", 9600, serial.PARITY_NONE, serial.STOPBITS_ONE, serial.EIGHTBITS]

"""---------------------------------------------------------------------------------------------------------------------
                Hilo para subir datos desde el Sistema de Antenas a la Base de Datos
---------------------------------------------------------------------------------------------------------------------"""
class updateDataBaseClass(QtCore.QThread):
    def __init__(self):
        # Inicia el Hilo
        QtCore.QThread.__init__(self)
        self.stop = False
    def run(self):
        while True:
            time.sleep(1)
            self.emit(QtCore.SIGNAL("insert DATA"))
            self.emit(QtCore.SIGNAL("update Time"))
            if self.stop == True:
                break

    def setStop(self):
        self.stop = False

"""---------------------------------------------------------------------------------------------------------------------
                        Hilos para iniciar el Sistema de Antenas
---------------------------------------------------------------------------------------------------------------------"""
class Testing(QtCore.QThread):
    def __init__(self, port, Laboratorio, Antenna, intComboBox):
        # Inicia el Hilo
        QtCore.QThread.__init__(self)
        self.Laboratorio = Laboratorio
        self.Antenna = Antenna
        self.port = port
        try:
            self.stop = False
            self.serialPort = serial.Serial(
                port=port,
                baudrate=serialPortSettings[1],
                parity=serialPortSettings[2],
                stopbits=serialPortSettings[3],
                bytesize=serialPortSettings[4],
            )
            antennaState[Antenna - 1] = True
            antennaPort[Antenna - 1] = intComboBox
        except serial.SerialException:
            self.stop = True
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText(
                "Puerto serial de Antena %d:\n%s ---> No disponible" % (Antenna,port))
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        except serial.portNotOpenError:
            self.stop = True
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText(
                "Intentando usar un puerto que no esta abierto")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()

    def run(self):
        try:
            while True:
                if (self.serialPort.inWaiting() > 0):
                    uid = self.serialPort.read(3).encode("hex")
                    self.emit(QtCore.SIGNAL("insert DATA"), uid, self.Laboratorio)
                if self.stop == True:
                    break
        except:
            self.stop = True
            antennaState[self.Antenna - 1] = False
            self.emit(QtCore.SIGNAL("msg Error"), self.port)

    def setStop(self):
        self.stop = True
        antennaState[self.Antenna - 1] = False
        self.serialPort.close()

"""---------------------------------------------------------------------------------------------------------------------
                        Ventana para autorizar la configuracion del Sistema de Antenas
---------------------------------------------------------------------------------------------------------------------"""
class authorizationWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.authorizationWindow = QtGui.QDialog()
        self.uiAuthorization = authorizationDialog()
        self.uiAuthorization.setupUi(self.authorizationWindow)
        self.authorizationWindow.show()

        self.uiAuthorization.acceptButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                                    "SP_DialogYesButton")))
        self.uiAuthorization.cancelButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                                    "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiAuthorization.acceptButton, QtCore.SIGNAL('clicked()'),
                               self.acceptFunction)
        QtCore.QObject.connect(self.uiAuthorization.cancelButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

    def acceptFunction(self):
        if self.uiAuthorization.passwordLineEdit.text() == "123":
            antennaSystemWindowClass(self)
            self.authorizationWindow.close()

    def closeFunction(self):
        self.authorizationWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                        Configuracion del Sistema de Antenas
---------------------------------------------------------------------------------------------------------------------"""
class antennaSystemWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.antennaSystemWindow = QtGui.QDialog()
        self.uiAntennaSystem = antennaSystemDialog()
        self.uiAntennaSystem.setupUi(self.antennaSystemWindow)
        self.antennaSystemWindow.show()

        self.uiAntennaSystem.acceptButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                                    "SP_DialogYesButton")))
        self.uiAntennaSystem.cancelButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                                    "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiAntennaSystem.acceptButton, QtCore.SIGNAL('clicked()'),
                               self.acceptFunction)
        QtCore.QObject.connect(self.uiAntennaSystem.cancelButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

        self.uiAntennaSystem.antenna1CheckBox.setChecked(antennaState[0])
        self.uiAntennaSystem.antenna2CheckBox.setChecked(antennaState[1])
        self.uiAntennaSystem.antenna3CheckBox.setChecked(antennaState[2])
        self.uiAntennaSystem.antenna4CheckBox.setChecked(antennaState[3])
        self.uiAntennaSystem.antenna5CheckBox.setChecked(antennaState[4])
        self.uiAntennaSystem.antenna6CheckBox.setChecked(antennaState[5])

        self.uiAntennaSystem.antenna1ComboBox.setCurrentIndex(antennaPort[0])
        self.uiAntennaSystem.antenna2ComboBox.setCurrentIndex(antennaPort[1])
        self.uiAntennaSystem.antenna3ComboBox.setCurrentIndex(antennaPort[2])
        self.uiAntennaSystem.antenna4ComboBox.setCurrentIndex(antennaPort[3])
        self.uiAntennaSystem.antenna5ComboBox.setCurrentIndex(antennaPort[4])
        self.uiAntennaSystem.antenna6ComboBox.setCurrentIndex(antennaPort[5])

    def acceptFunction(self):
        # Antena 1
        if self.uiAntennaSystem.antenna1CheckBox.isChecked():
            try:
                if antennaSystem[0].is_alive:
                    antennaSystem[0].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna1ComboBox.currentIndex()
            antennaSystem[0] = Testing(self.uiAntennaSystem.antenna1ComboBox.currentText(), "Laboratorio 1", 1,
                                     intComboBox)
            self.connect(antennaSystem[0], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[0], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[0].start()
        else:
            antennaState[0] = False
            try:
                antennaSystem[0].setStop()
            except:
                pass
        # Antena 2
        if self.uiAntennaSystem.antenna2CheckBox.isChecked():
            try:
                if antennaSystem[1].is_alive:
                    antennaSystem[1].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna2ComboBox.currentIndex()
            antennaSystem[1] = Testing(self.uiAntennaSystem.antenna2ComboBox.currentText(), "Laboratorio 2", 2,
                                     intComboBox)
            self.connect(antennaSystem[1], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[1], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[1].start()
        else:
            antennaState[1] = False
            try:
                antennaSystem[1].setStop()
            except:
                pass
        # Antena 3
        if self.uiAntennaSystem.antenna3CheckBox.isChecked():
            try:
                if antennaSystem[2].is_alive:
                    antennaSystem[2].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna3ComboBox.currentIndex()
            antennaSystem[2] = Testing(self.uiAntennaSystem.antenna3ComboBox.currentText(), "Laboratorio 3", 3,
                                     intComboBox)
            self.connect(antennaSystem[2], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[2], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[2].start()
        else:
            antennaState[2] = False
            try:
                antennaSystem[2].setStop()
            except:
                pass
        # Antena 4
        if self.uiAntennaSystem.antenna4CheckBox.isChecked():
            try:
                if antennaSystem[3].is_alive:
                    antennaSystem[3].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna4ComboBox.currentIndex()
            antennaSystem[3] = Testing(self.uiAntennaSystem.antenna4ComboBox.currentText(), "Laboratorio 4", 4,
                                     intComboBox)
            self.connect(antennaSystem[3], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[3], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[3].start()
        else:
            antennaState[3] = False
            try:
                antennaSystem[3].setStop()
            except:
                pass
        # Antena 5
        if self.uiAntennaSystem.antenna5CheckBox.isChecked():
            try:
                if antennaSystem[4].is_alive:
                    antennaSystem[4].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna5ComboBox.currentIndex()
            antennaSystem[4] = Testing(self.uiAntennaSystem.antenna5ComboBox.currentText(), "Laboratorio 5", 5,
                                     intComboBox)
            self.connect(antennaSystem[4], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[4], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[4].start()
        else:
            antennaState[4] = False
            try:
                antennaSystem[4].setStop()
            except:
                pass
        # Antena 6
        if self.uiAntennaSystem.antenna6CheckBox.isChecked():
            try:
                if antennaSystem[5].is_alive:
                    antennaSystem[5].setStop()
            except:
                pass
            intComboBox = self.uiAntennaSystem.antenna6ComboBox.currentIndex()
            antennaSystem[5] = Testing(self.uiAntennaSystem.antenna6ComboBox.currentText(), "Laboratorio 6", 6,
                                     intComboBox)
            self.connect(antennaSystem[5], QtCore.SIGNAL("msg Error"), self.msgErrorFunction)
            self.connect(antennaSystem[5], QtCore.SIGNAL("insert DATA"), self.insertDataBaseFunction)
            antennaSystem[5].start()
        else:
            antennaState[5] = False
            try:
                antennaSystem[5].setStop()
            except:
                pass
        self.antennaSystemWindow.close()

    def msgErrorFunction(self, port):
        msgBox = QtGui.QMessageBox()
        msgBox.setIcon(QtGui.QMessageBox.Warning)
        msgBox.setWindowTitle("Error")
        msgBox.setText(
            "Dispositivo desconectado o multiple acceso \nal puerto serial: %s" % port)
        msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def insertDataBaseFunction(self, uid, Laboratorio):
        # Preparando la tabla de la Base de Datos
        self.tableModel = QtSql.QSqlTableModel(self)
        self.tableModel.setTable("INVENTARIO")
        self.tableModel.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableModel.select()
        self.tableModel.setFilter("%s = '%s'" % ("UID", uid))
        Record = self.tableModel.record(0)
        temp1 = int(Record.value("PLACA").toString())
        temp2 = Record.value("DESCRIPCION").toString()
        sql = "INSERT INTO REGISTROS(UID, PLACA, DESCRIPCION, LABORATORIO, HORA, FECHA) VALUES (:UID," \
              " :PLACA, :DESCRIPCION, :LABORATORIO, :HORA, :FECHA)"
        consulta = QtSql.QSqlQuery()
        consulta.prepare(sql)
        consulta.bindValue(":UID", uid)
        consulta.bindValue(":PLACA", temp1)
        consulta.bindValue(":DESCRIPCION", temp2)
        consulta.bindValue(":LABORATORIO", Laboratorio)
        consulta.bindValue(":HORA", QtCore.QTime.currentTime().toString("hh:mm"))
        consulta.bindValue(":FECHA", QtCore.QDate.currentDate().toString("yyyy/MM/dd"))
        consulta.exec_()

    def closeFunction(self):
        self.antennaSystemWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                        Ventana para visualizar los Registros
---------------------------------------------------------------------------------------------------------------------"""
class registerWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.registerWindow = QtGui.QDialog()
        self.uiRegister = registerDialog()
        self.uiRegister.setupUi(self.registerWindow)
        self.registerWindow.show()

        self.tableModelWindow = QtSql.QSqlTableModel(self)
        self.tableModelWindow.setTable("REGISTROS")
        self.tableModelWindow.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableModelWindow.select()
        self.uiRegister.tableView.setModel(self.tableModelWindow)
        self.uiRegister.tableView.show()
        #Deshabilitar edición de tabla
        self.uiRegister.tableView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

"""---------------------------------------------------------------------------------------------------------------------
                                        Ventana Leer UID
---------------------------------------------------------------------------------------------------------------------"""
class readUIDWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.readUIDWindow = QtGui.QDialog()
        self.uiReadUID = readUIDDialog()
        self.uiReadUID.setupUi(self.readUIDWindow)
        self.readUIDWindow.show()

        self.uiReadUID.toggleButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
        self.uiReadUID.acceptButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogYesButton")))
        self.uiReadUID.cancelButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiReadUID.toggleButton, QtCore.SIGNAL('clicked()'),
                               self.toggleFunction)
        QtCore.QObject.connect(self.uiReadUID.selectUIDButton, QtCore.SIGNAL('clicked()'),
                               self.selectUIDFunction)
        QtCore.QObject.connect(self.uiReadUID.acceptButton, QtCore.SIGNAL('clicked()'),
                               self.acceptFunction)
        QtCore.QObject.connect(self.uiReadUID.cancelButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

    def toggleFunction(self):
        if self.uiReadUID.toggleButton.text() == "Desconectar" :
            self.uiReadUID.toggleButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
            self.uiReadUID.toggleButton.setText("Conectar")
        else:
            self.uiReadUID.listWidget.clear()
            self.uiReadUID.toggleButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_BrowserStop")))
            self.uiReadUID.toggleButton.setText("Desconectar")
            try:
                self.serialPort = serial.Serial(
                    port = self.uiReadUID.serialPortComboBox.currentText(),
                    baudrate=serialPortSettings[1],
                    parity=serialPortSettings[2],
                    stopbits=serialPortSettings[3],
                    bytesize=serialPortSettings[4],
                )
                if True:
                    self.testerThread = threading.Thread(target = self.testerThreadFunction)
                    self.testerThread.start()
            except:
                if True:
                    self.uiReadUID.toggleButton.setIcon(
                        self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
                    self.uiReadUID.toggleButton.setText("Conectar")
                    msgBox = QtGui.QMessageBox()
                    msgBox.setIcon(QtGui.QMessageBox.Warning)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText(
                        "Puerto serial:\n%s ---> Inactivo" % self.uiReadUID.serialPortComboBox.currentText())
                    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                    msgBox.exec_()

    def testerThreadFunction(self):
        try:
            while (self.uiReadUID.toggleButton.text() == "Desconectar"):
                if (self.serialPort.inWaiting() > 0):
                    self.uiReadUID.listWidget.addItem(self.serialPort.read(3).encode("hex"))
        except:
            self.serialPort.close()
            self.uiReadUID.listWidget.addItem("Dispositivo desconectado o multiple acceso \nal puerto serial: %s"
                                              % self.uiReadUID.serialPortComboBox.currentText())

    def selectUIDFunction(self):
        self.uiReadUID.lineEdit.setText(self.uiReadUID.listWidget.currentItem().text())

    def acceptFunction(self):
        UIDGlobal.setText(self.uiReadUID.lineEdit.text())
        self.readUIDWindow.close()

    def closeFunction(self):
        self.readUIDWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                            Ventana para insertar datos en la Base de Datos
---------------------------------------------------------------------------------------------------------------------"""
class insertWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.insertWindow = QtGui.QDialog()
        self.uiInsert = insertDialog()
        self.uiInsert.setupUi(self.insertWindow)
        self.insertWindow.show()

        self.uiInsert.timeLabel.setText(QtCore.QTime.currentTime().toString("hh:mm"))
        self.uiInsert.dateLabel.setText(QtCore.QDate.currentDate().toString(QtCore.Qt.DefaultLocaleLongDate))

        self.uiInsert.readButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
        self.uiInsert.clearButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                            "SP_DialogResetButton")))
        self.uiInsert.saveButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveFDIcon")))
        self.uiInsert.closeButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiInsert.readButton, QtCore.SIGNAL('clicked()'),
                               self.readFunction)
        QtCore.QObject.connect(self.uiInsert.clearButton, QtCore.SIGNAL('clicked()'),
                               self.clearFunction)
        QtCore.QObject.connect(self.uiInsert.saveButton, QtCore.SIGNAL('clicked()'),
                               self.saveFunction)
        QtCore.QObject.connect(self.uiInsert.closeButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

    def readFunction(self):
        UIDGlobal = self.uiInsert.UIDLineEdit
        readUIDWindowClass(self)

    def clearFunction(self):
        self.uiInsert.UIDLineEdit.setText("")
        self.uiInsert.placaLineEdit.setText("")
        self.uiInsert.descripcionLineEdit.setText("")
        self.uiInsert.serialLineEdit.setText("")
        self.uiInsert.marcaLineEdit.setText("")
        self.uiInsert.modeloLineEdit.setText("")

    def saveFunction(self):
        if self.uiInsert.UIDLineEdit.text() == "":
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Ingresar Datos")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        else:
            try:
                sql = "INSERT INTO INVENTARIO(UID, PLACA, DESCRIPCION, SERIAL, MARCA, MODELO) VALUES (:UID, :PLACA, " \
                      ":DESCRIPCION, :SERIAL, :MARCA, :MODELO)"
                consulta = QtSql.QSqlQuery()
                consulta.prepare(sql)
                consulta.bindValue(0, self.uiInsert.UIDLineEdit.text())
                consulta.bindValue(1, int(self.uiInsert.placaLineEdit.text()))
                consulta.bindValue(2, self.uiInsert.descripcionLineEdit.text())
                consulta.bindValue(3, self.uiInsert.serialLineEdit.text())
                consulta.bindValue(4, self.uiInsert.marcaLineEdit.text())
                consulta.bindValue(5, self.uiInsert.modeloLineEdit.text())
                consulta.exec_()
                if True:
                    QtGui.QMessageBox.information(self, "Correcto", "Datos guardados", QtGui.QMessageBox.Accepted)
                    self.insertWindow.close()
            except ValueError:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText("El tipo de dato de 'PLACA' es entero\nTipo de dato invalido")
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.exec_()
            except:
                msgBox = QtGui.QMessageBox()
                msgBox.setIcon(QtGui.QMessageBox.Warning)
                msgBox.setWindowTitle("Error")
                msgBox.setText(dataBaseGlobal.lastError().text())
                msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                msgBox.exec_()


    def closeFunction(self):
        self.insertWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                        Ventana para modificar la configuracion del puerto serial
---------------------------------------------------------------------------------------------------------------------"""
class preferencesWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.preferencesWindow = QtGui.QDialog()
        self.uiPreferences = preferencesDialog()
        self.uiPreferences.setupUi(self.preferencesWindow)
        self.preferencesWindow.show()

        self.uiPreferences.acceptButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogYesButton")))
        self.uiPreferences.cancelButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiPreferences.defaultButton, QtCore.SIGNAL('clicked()'),
                               self.defaultFunction)
        QtCore.QObject.connect(self.uiPreferences.acceptButton, QtCore.SIGNAL('clicked()'),
                               self.acceptFunction)
        QtCore.QObject.connect(self.uiPreferences.cancelButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

        self.uiPreferences.baudRateComboBox.setCurrentIndex(serialPortTemp[0])
        self.uiPreferences.dataBitsComboBox.setCurrentIndex(serialPortTemp[1])
        self.uiPreferences.parityComboBox.setCurrentIndex(serialPortTemp[2])
        self.uiPreferences.stopBitsComboBox.setCurrentIndex(serialPortTemp[3])

    def defaultFunction(self):
        self.uiPreferences.baudRateComboBox.setCurrentIndex(6)
        self.uiPreferences.dataBitsComboBox.setCurrentIndex(3)
        self.uiPreferences.parityComboBox.setCurrentIndex(0)
        self.uiPreferences.stopBitsComboBox.setCurrentIndex(0)

    def acceptFunction(self):
        serialPortTemp[0] = self.uiPreferences.baudRateComboBox.currentIndex()
        serialPortSettings [1] = self.uiPreferences.baudRateComboBox.currentText()

        if self.uiPreferences.dataBitsComboBox.currentIndex() == 0:
            serialPortTemp[1] = 0
            serialPortSettings[4] = serial.FIVEBITS
        elif self.uiPreferences.dataBitsComboBox.currentIndex() == 1:
            serialPortTemp[1] = 1
            serialPortSettings[4] = serial.SIXBITS
        elif self.uiPreferences.dataBitsComboBox.currentIndex() == 2:
            serialPortTemp[1] = 2
            serialPortSettings[4] = serial.SEVENBITS
        elif self.uiPreferences.dataBitsComboBox.currentIndex() == 3:
            serialPortTemp[1] = 3
            serialPortSettings[4] = serial.EIGHTBITS

        if self.uiPreferences.parityComboBox.currentIndex() == 0:
            serialPortTemp[2] = 0
            serialPortSettings[2] = serial.PARITY_NONE
        elif self.uiPreferences.parityComboBox.currentIndex() == 1:
            serialPortTemp[2] = 1
            serialPortSettings[2] = serial.PARITY_ODD
        elif self.uiPreferences.parityComboBox.currentIndex() == 2:
            serialPortTemp[2] = 2
            serialPortSettings[2] = serial.PARITY_EVEN
        elif self.uiPreferences.parityComboBox.currentIndex() == 3:
            serialPortTemp[2] = 3
            serialPortSettings[2] = serial.PARITY_MARK
        elif self.uiPreferences.parityComboBox.currentIndex() == 4:
            serialPortTemp[2] = 4
            serialPortSettings[2] = serial.PARITY_SPACE

        if self.uiPreferences.stopBitsComboBox.currentIndex() == 0:
            serialPortTemp[3] = 0
            serialPortSettings[3] = serial.STOPBITS_ONE
        elif self.uiPreferences.stopBitsComboBox.currentIndex() == 1:
            serialPortTemp[3] = 1
            serialPortSettings[3] = serial.STOPBITS_ONE_POINT_FIVE
        elif self.uiPreferences.stopBitsComboBox.currentIndex() == 2:
            serialPortTemp[3] = 2
            serialPortSettings[3] = serial.STOPBITS_TWO
        self.preferencesWindow.close()

    def closeFunction(self):
        self.preferencesWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                    Ventana para escanear los puertos seriales disponibles
---------------------------------------------------------------------------------------------------------------------"""
class scanSerialPortsWindowClass(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.scanSerialPortsWindow = QtGui.QDialog()
        self.uiScanSerialPorts = scanSerialPortsDialog()
        self.uiScanSerialPorts.setupUi(self.scanSerialPortsWindow)
        self.scanSerialPortsWindow.show()

        self.uiScanSerialPorts.toggleButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
        self.uiScanSerialPorts.closeButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))
        QtCore.QObject.connect(self.uiScanSerialPorts.toggleButton, QtCore.SIGNAL('clicked()'),
                               self.scanSerialPortsFunction)
        QtCore.QObject.connect(self.uiScanSerialPorts.closeButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunction)

    def scanSerialPortsFunction(self, numberPort=10):
        self.uiScanSerialPorts.serialPortsListWidget.clear()
        self.uiScanSerialPorts.scanSerialPortsListWidget.clear()
        if self.uiScanSerialPorts.serialPortComboBox.currentText() == "/dev/ttyUSBx" :
            for i in range(numberPort):
                try:
                    numberSerialPort = "/dev/ttyUSB%d" % i
                    serial.Serial(numberSerialPort)
                    if True:
                        self.uiScanSerialPorts.scanSerialPortsListWidget.addItem("Activo --> %s" % numberSerialPort)
                        self.uiScanSerialPorts.serialPortsListWidget.addItem("%s" % numberSerialPort)
                except:
                    if True:
                        self.uiScanSerialPorts.scanSerialPortsListWidget.addItem("Inactivo --> %s" % numberSerialPort)
                        pass
        else:
            for i in range(numberPort):
                try:
                    numberSerialPort = "//dev/ttyS%d" % i
                    serial.Serial(numberSerialPort)
                    if True:
                        self.uiScanSerialPorts.scanSerialPortsListWidget.addItem("Activo --> %s" % numberSerialPort)
                        self.uiScanSerialPorts.serialPortsListWidget.addItem("%s" % numberSerialPort)
                except:
                    if True:
                        self.uiScanSerialPorts.scanSerialPortsListWidget.addItem("Inactivo --> %s" % numberSerialPort)
                        pass

    def closeFunction(self):
        self.scanSerialPortsWindow.close()

"""---------------------------------------------------------------------------------------------------------------------
                                        Ventana Principal
---------------------------------------------------------------------------------------------------------------------"""
class mainWindowClass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.mainWindow = QtGui.QMainWindow()
        self.uiMain = Ui_MainWindow()
        self.uiMain.setupUi(self.mainWindow)
        self.mainWindow.show()

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                    Botones
        ------------------------------------------------------------------------------------------------------------ """
        QtCore.QObject.connect(self.uiMain.onOffAction, QtCore.SIGNAL('triggered()'),
                               self.authorizationFunction)
        QtCore.QObject.connect(self.uiMain.scanSerialPortsAction, QtCore.SIGNAL('triggered()'),
                               self.scanSerialPortsFunction)
        QtCore.QObject.connect(self.uiMain.preferencesAction, QtCore.SIGNAL('triggered()'),
                               self.preferencesFunction)
        QtCore.QObject.connect(self.uiMain.closeButton, QtCore.SIGNAL('clicked()'),
                               self.closeFunctionMainWindow)
        self.uiMain.closeButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))
        updateData[0] = updateDataBaseClass()
        self.connect(updateData[0], QtCore.SIGNAL("insert DATA"), self.showTableFuntionTab1)
        self.connect(updateData[0], QtCore.SIGNAL("update Time"), self.timeFunctionMainWindow)
        updateData[0].start()


        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                Pestaña 1 - Botones
        ------------------------------------------------------------------------------------------------------------ """
        QtCore.QObject.connect(self.uiMain.seeMoreButtonTab1, QtCore.SIGNAL('clicked()'),
                               self.seeMoreFunctionTab1)
        self.showTableFuntionTab1()

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                Pestaña 2 - Botones
        ------------------------------------------------------------------------------------------------------------ """
        QtCore.QObject.connect(self.uiMain.searchButtonTab2, QtCore.SIGNAL('clicked()'),
                               self.searchFuntionTab2)
        QtCore.QObject.connect(self.uiMain.clearSearchButtonTab2, QtCore.SIGNAL('clicked()'),
                               self.clearSearchFunctionTab2)
        QtCore.QObject.connect(self.uiMain.insertButtonTab2, QtCore.SIGNAL('clicked()'),
                               self.insertFuntionTab2)
        QtCore.QObject.connect(self.uiMain.deleteButtonTab2, QtCore.SIGNAL('clicked()'),
                               self.deleteFuntionTab2)
        QtCore.QObject.connect(self.uiMain.updateButtonTab2, QtCore.SIGNAL('clicked()'),
                               self.updateFuntionTab2)
        self.uiMain.searchButtonTab2.setIcon(
            self.style().standardIcon(getattr(QtGui.QStyle, "SP_FileDialogContentsView")))
        self.uiMain.clearSearchButtonTab2.setIcon(self.style().standardIcon(getattr(QtGui.QStyle,
                                                                                    "SP_DialogResetButton")))
        self.uiMain.insertButtonTab2.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_FileDialogNewFolder")))
        self.uiMain.deleteButtonTab2.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_TrashIcon")))
        self.uiMain.updateButtonTab2.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_BrowserReload")))
        self.showTableFuntionTab2()

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                Pestaña 3 - Botones
        ------------------------------------------------------------------------------------------------------------ """
        QtCore.QObject.connect(self.uiMain.toggleButtonTab3, QtCore.SIGNAL('clicked()'),
                               self.searchFuntionTab3)
        QtCore.QObject.connect(self.uiMain.selectUIDButtonTab3, QtCore.SIGNAL('clicked()'),
                               self.selectUIDFunctionTab3)
        """menu = QtGui.QMenu()
        for indice, columna in enumerate(nombreColumnas, start=0):
            accion = QtGui.QAction(columna,menu)
            accion.setCheckable(True)
            accion.setChecked(True)
            accion.setData(indice)
            menu.addAction(accion)"""

        self.uiMain.toggleButtonTab3.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
        self.tableModelTab3 = QtSql.QSqlTableModel(self)
        self.tableModelTab3.setTable("INVENTARIO")
        self.tableModelTab3.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableModelTab3.select()
        self.uiMain.tableViewTab3.setModel(self.tableModelTab3)
        self.uiMain.tableViewTab3.show()
        # Deshabilitar edición de tabla
        self.uiMain.tableViewTab3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                    Acciones
        ------------------------------------------------------------------------------------------------------------ """
    def authorizationFunction(self):
        authorizationWindowClass(self)

    def timeFunctionMainWindow(self):
        self.uiMain.timeLabel.setText(QtCore.QTime.currentTime().toString("hh:mm"))
        self.uiMain.dateLabel.setText(QtCore.QDate.currentDate().toString(QtCore.Qt.DefaultLocaleLongDate))
        if antennaState[0] == True:
            self.uiMain.antenna1Label.setText("Antena 1 / Activado")
        else:
            self.uiMain.antenna1Label.setText("Antena 1 / Desactivado")
        if antennaState[1] == True:
            self.uiMain.antenna2Label.setText("Antena 2 / Activado")
        else:
            self.uiMain.antenna2Label.setText("Antena 2 / Desactivado")
        if antennaState[2] == True:
            self.uiMain.antenna3Label.setText("Antena 3 / Activado")
        else:
            self.uiMain.antenna3Label.setText("Antena 3 / Desactivado")
        if antennaState[3] == True:
            self.uiMain.antenna4Label.setText("Antena 4 / Activado")
        else:
            self.uiMain.antenna4Label.setText("Antena 4 / Desactivado")
        if antennaState[4] == True:
            self.uiMain.antenna5Label.setText("Antena 5 / Activado")
        else:
            self.uiMain.antenna5Label.setText("Antena 5 / Desactivado")
        if antennaState[5] == True:
            self.uiMain.antenna6Label.setText("Antena 6 / Activado")
        else:
            self.uiMain.antenna6Label.setText("Antena 6 / Desactivado")

    def preferencesFunction(self):
        preferencesWindowClass(self)

    def scanSerialPortsFunction(self):
        scanSerialPortsWindowClass(self)

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                                    Funciones
        ------------------------------------------------------------------------------------------------------------ """

    def closeFunctionMainWindow(self):
        self.mainWindow.close()

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                            Pestaña 1 - Funciones
        ------------------------------------------------------------------------------------------------------------ """

    def seeMoreFunctionTab1(self):
        registerWindowClass(self)

    def showTableFuntionTab1(self):
        self.uiMain.tableWidgetTab1.setColumnCount(5)
        self.uiMain.tableWidgetTab1.setRowCount(5)
        self.uiMain.tableWidgetTab1.setHorizontalHeaderItem(0, QtGui.QTableWidgetItem("UID"))
        self.uiMain.tableWidgetTab1.setHorizontalHeaderItem(1, QtGui.QTableWidgetItem("PLACA"))
        self.uiMain.tableWidgetTab1.setHorizontalHeaderItem(2, QtGui.QTableWidgetItem("DESCRIPCION"))
        self.uiMain.tableWidgetTab1.setHorizontalHeaderItem(3, QtGui.QTableWidgetItem("HORA"))
        self.uiMain.tableWidgetTab1.setHorizontalHeaderItem(4, QtGui.QTableWidgetItem("FECHA"))
        self.uiMain.tableWidgetTab1.show()
        # Deshabilitar edición de tabla
        self.uiMain.tableWidgetTab1.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.modelWidget = QtSql.QSqlQueryModel(self)
        self.modelWidget.setQuery("select * from REGISTROS")
        for i in range(0, 5):
            for j in range(0, 5):
                self.Row = self.modelWidget.rowCount() - 1 - i
                self.Record = self.modelWidget.record(self.Row)
                self.Temp = self.Record.value(j).toString()
                self.uiMain.tableWidgetTab1.setItem(i, j, QtGui.QTableWidgetItem(self.Temp))

        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                            Pestaña 2 - Funciones
        ------------------------------------------------------------------------------------------------------------ """

    def showTableFuntionTab2(self):
        self.tableModelTab2 = QtSql.QSqlTableModel(self)
        self.tableModelTab2.setTable("INVENTARIO")
        self.tableModelTab2.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
        self.tableModelTab2.select()
        self.uiMain.tableViewTab2.setModel(self.tableModelTab2)
        self.uiMain.tableViewTab2.show()

    def searchFuntionTab2(self):
        tableColumn = self.uiMain.itemTablecomboBoxTab2.currentText()
        text = self.uiMain.searchLineEditTab2.text()
        if len(text) == 0:
            self.tableModelTab2.setFilter("")
        else:
            self.tableModelTab2.setFilter("%s = '%s'" % (tableColumn, text))

    def clearSearchFunctionTab2(self):
        self.uiMain.searchLineEditTab2.setText("")
        self.showTableFuntionTab2()

    def insertFuntionTab2(self):
        insertWindowClass(self)

    def deleteFuntionTab2(self):
        self.numeroFilaSeleccionada = self.uiMain.tableViewTab2.currentIndex().row()
        self.fila = QtSql.QSqlQueryModel()
        self.fila.setQuery("SELECT * FROM INVENTARIO")
        self.filaSeleccionada = (
        "UID: " + self.fila.record(self.numeroFilaSeleccionada).value("UID").toString() + "\n" +
        "PLACA: " + self.fila.record(self.numeroFilaSeleccionada).value("PLACA").toString() + "\n" +
        "DESCRIPCION: " + self.fila.record(self.numeroFilaSeleccionada).value("DESCRIPCION").toString() + "\n" +
        "SERIAL: " + self.fila.record(self.numeroFilaSeleccionada).value("SERIAL").toString() + "\n" +
        "MARCA: " + self.fila.record(self.numeroFilaSeleccionada).value("MARCA").toString() + "\n" +
        "MODELO: " + self.fila.record(self.numeroFilaSeleccionada).value("MODELO").toString())
        reply = QtGui.QMessageBox.question(self,
                                           'Events - Slot',
                                           "Desea Borrar la fila seleccionada:\n" + self.filaSeleccionada,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self.tableModelTab2.removeRow(self.uiMain.tableViewTab2.currentIndex().row())
            self.tableModelTab2.submitAll()

    def updateFuntionTab2(self):
        self.tableModelTab2.submitAll()
        self.tableModelTab3.submitAll()
        """ ------------------------------------------------------------------------------------------------------------
                                                Ventana Principal
                                            Pestaña 3 - Funciones
        ------------------------------------------------------------------------------------------------------------ """

    def searchFuntionTab3(self):
        if self.uiMain.searchLineEditTab3.text() == "":
            msgBox = QtGui.QMessageBox()
            msgBox.setIcon(QtGui.QMessageBox.Warning)
            msgBox.setWindowTitle("Error")
            msgBox.setText("Ingresar un valor de UID")
            msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
            msgBox.exec_()
        else:
            if self.uiMain.toggleButtonTab3.text() == "Pausar":
                self.uiMain.toggleButtonTab3.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
                self.uiMain.toggleButtonTab3.setText("Detectar")
            else:
                self.uiMain.listWidgetTab3.clear()
                self.uiMain.toggleButtonTab3.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_BrowserStop")))
                self.uiMain.toggleButtonTab3.setText("Pausar")
                try:
                    self.serialPort = serial.Serial(
                        port=self.uiMain.serialPortComboBoxTab3.currentText(),
                        baudrate=serialPortSettings[1],
                        parity=serialPortSettings[2],
                        stopbits=serialPortSettings[3],
                        bytesize=serialPortSettings[4],
                    )
                    self.testerThreadTab3 = threading.Thread(target=self.testerThreadFunctionTab3)
                    self.testerThreadTab3.start()
                except serial.SerialException:
                    self.uiMain.toggleButtonTab3.setIcon(
                        self.style().standardIcon(getattr(QtGui.QStyle, "SP_DriveNetIcon")))
                    self.uiMain.toggleButtonTab3.setText("Detectar")
                    msgBox = QtGui.QMessageBox()
                    msgBox.setIcon(QtGui.QMessageBox.Warning)
                    msgBox.setWindowTitle("Error")
                    msgBox.setText("Puerto serial:\n%s ---> Inactivo"
                                   % self.uiMain.serialPortComboBoxTab3.currentText())
                    msgBox.setStandardButtons(QtGui.QMessageBox.Ok)
                    msgBox.exec_()

    def testerThreadFunctionTab3(self):
        try:
            self.uiMain.labelTab3.setText("No Disponible")
            print threading.current_thread().getName()
            print threading.enumerate()
            while True:
                if (self.serialPort.inWaiting() > 0):
                    temp = self.serialPort.read(3).encode("hex")
                    self.uiMain.listWidgetTab3.addItem(temp)
                    if temp == self.uiMain.searchLineEditTab3.text():
                        self.uiMain.labelTab3.setText("Disponible")
                        break
                if self.uiMain.toggleButtonTab3.text() == "Detectar":
                    break
            self.serialPort.close()
        except:
            self.serialPort.close()
            self.uiMain.listWidgetTab3.addItem("Dispositivo desconectado o multiple acceso \nal puerto serial: %s"
                                              % self.uiMain.serialPortComboBoxTab3.currentText())

    def selectUIDFunctionTab3(self):
        self.numeroFilaSeleccionada = self.uiMain.tableViewTab3.currentIndex().row()
        self.fila = QtSql.QSqlQueryModel()
        self.fila.setQuery("SELECT * FROM INVENTARIO")
        self.tempTab3 = self.fila.record(self.numeroFilaSeleccionada).value("UID").toString()
        self.uiMain.searchLineEditTab3.setText(self.tempTab3)

"""---------------------------------------------------------------------------------------------------------------------
                                    Ventana de inicio de sesión
---------------------------------------------------------------------------------------------------------------------"""
class loginWindowClass(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.uiLogin = loginMainWindow()
        self.uiLogin.setupUi(self)

        self.uiLogin.loginButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogYesButton")))
        self.uiLogin.closeButton.setIcon(self.style().standardIcon(getattr(QtGui.QStyle, "SP_DialogNoButton")))

        QtCore.QObject.connect(self.uiLogin.connectAction, QtCore.SIGNAL('triggered()'),
                               self.loginFunction)
        QtCore.QObject.connect(self.uiLogin.closeAction, QtCore.SIGNAL('triggered()'),
                               self.closeFunction)
        QtCore.QObject.connect(self.uiLogin.loginButton, QtCore.SIGNAL('clicked()'), self.loginFunction)
        QtCore.QObject.connect(self.uiLogin.closeButton, QtCore.SIGNAL('clicked()'), self.closeFunction)

    #Conectando a la Base de Datos
    def loginFunction(self):
        self.dataBase = QtSql.QSqlDatabase.addDatabase('QMYSQL')
        self.dataBase.setHostName("%s" % self.uiLogin.serverLineEdit.text())
        self.dataBase.setDatabaseName("%s" % self.uiLogin.dataBaseLineEdit.text())
        self.dataBase.setUserName("%s" % self.uiLogin.userLineEdit.text())
        self.dataBase.setPassword("%s" % self.uiLogin.passwordLineEdit.text())
        self.dataBaseStatus = self.dataBase.open()
        dataBaseGlobal = self.dataBase
        if self.dataBaseStatus == True:
            self.close()
            mainWindowClass(self)
        else:
            QtGui.QMessageBox.warning(self, "Error", self.dataBase.lastError().text(), QtGui.QMessageBox.Discard)

    def closeFunction(self):
        self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)  # Crea aplicacion objeto
    Login = loginWindowClass()
    Login.show()
    sys.exit(app.exec_())