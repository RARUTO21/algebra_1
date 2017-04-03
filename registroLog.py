# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\alvar_000\Documents\registro\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(606, 562)
        self.cerrarBtn = QtWidgets.QPushButton(Dialog)
        self.cerrarBtn.setGeometry(QtCore.QRect(480, 520, 75, 23))
        self.cerrarBtn.setObjectName("cerrarBtn")
        self.actualizarBtn = QtWidgets.QPushButton(Dialog)
        self.actualizarBtn.setGeometry(QtCore.QRect(60, 520, 75, 23))
        self.actualizarBtn.setObjectName("actualizarBtn")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 60, 491, 431))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.actualizarBtn.clicked.connect(self.actualizaText)
        self.cerrarBtn.clicked.connect(self.cerrar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.cerrarBtn.setText(_translate("Dialog", "Cerrar"))
        self.actualizarBtn.setText(_translate("Dialog", "Actualizar"))
        self.label.setText(_translate("Dialog", "Registro de cambios"))
        self.cerrarBtn.setVisible(False)
        self.actualizaText()


    def actualizaText(self):
        self.textEdit.clear()
        fileHandle = open("Resultados.txt", "r+")
        tmp = fileHandle.read()
        print("Abriendo acrh " + tmp)
        self.textEdit.setText(tmp)
        fileHandle.close()

    def cerrar(self):
        self.hide()


class Log(QtWidgets.QDialog):
    def __init__(self, parent):
        QtWidgets.QDialog.__init__(self)
        self.ventana = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.ventana)
        self.ventana.show()