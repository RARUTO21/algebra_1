# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanita.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SistemaMatricial import *
import copy
import numpy as np


class Ui_ventanita(object):
    matrizA = []
    matrizB = []
    matrizC = []
    matrizX = []

    def setupUi(self, ventanita):
        ventanita.setObjectName("ventanita")
        ventanita.resize(700, 568)
        self.centralWidget = QtWidgets.QWidget(ventanita)
        self.centralWidget.setObjectName("centralWidget")
        self.cboOrden = QtWidgets.QComboBox(self.centralWidget)
        self.cboOrden.setGeometry(QtCore.QRect(30, 110, 79, 24))
        self.cboOrden.setObjectName("cboOrden")
        self.cboOrden.addItem("")
        self.cboOrden.addItem("")
        self.cboOrden.addItem("")
        self.cboOrden.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 50, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnDefinirOrden = QtWidgets.QPushButton(self.centralWidget)
        self.btnDefinirOrden.setGeometry(QtCore.QRect(180, 110, 80, 24))
        self.btnDefinirOrden.setObjectName("btnDefinirOrden")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cboMatriz = QtWidgets.QComboBox(self.centralWidget)
        self.cboMatriz.setGeometry(QtCore.QRect(30, 200, 79, 24))
        self.cboMatriz.setObjectName("cboMatriz")
        self.cboMatriz.addItem("")
        self.cboMatriz.addItem("")
        self.cboMatriz.addItem("")
        self.grpBox11 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox11.setGeometry(QtCore.QRect(310, 20, 61, 101))
        self.grpBox11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox11.setObjectName("grpBox11")
        self.txtNum11 = QtWidgets.QLineEdit(self.grpBox11)
        self.txtNum11.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum11.setText("")
        self.txtNum11.setObjectName("txtNum11")
        self.line = QtWidgets.QFrame(self.grpBox11)
        self.line.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.txtDen11 = QtWidgets.QLineEdit(self.grpBox11)
        self.txtDen11.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen11.setText("")
        self.txtDen11.setObjectName("txtDen11")
        self.btnGuardarCambios = QtWidgets.QPushButton(self.centralWidget)
        self.btnGuardarCambios.setGeometry(QtCore.QRect(180, 200, 80, 24))
        self.btnGuardarCambios.setObjectName("btnGuardarCambios")
        self.label_38 = QtWidgets.QLabel(self.centralWidget)
        self.label_38.setGeometry(QtCore.QRect(20, 360, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.btnCalcularX = QtWidgets.QPushButton(self.centralWidget)
        self.btnCalcularX.setGeometry(QtCore.QRect(90, 420, 80, 24))
        self.btnCalcularX.setObjectName("btnCalcularX")
        self.txaResultado = QtWidgets.QTextEdit(self.centralWidget)
        self.txaResultado.setGeometry(QtCore.QRect(20, 450, 271, 70))
        self.txaResultado.setObjectName("txaResultado")
        self.grpBox12 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox12.setGeometry(QtCore.QRect(390, 20, 61, 101))
        self.grpBox12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox12.setObjectName("grpBox12")
        self.txtNum12 = QtWidgets.QLineEdit(self.grpBox12)
        self.txtNum12.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum12.setText("")
        self.txtNum12.setObjectName("txtNum12")
        self.line_2 = QtWidgets.QFrame(self.grpBox12)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.txtDen12 = QtWidgets.QLineEdit(self.grpBox12)
        self.txtDen12.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen12.setText("")
        self.txtDen12.setObjectName("txtDen12")
        self.grpBox15 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox15.setGeometry(QtCore.QRect(630, 20, 61, 101))
        self.grpBox15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox15.setObjectName("grpBox15")
        self.txtNum15 = QtWidgets.QLineEdit(self.grpBox15)
        self.txtNum15.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum15.setText("")
        self.txtNum15.setObjectName("txtNum15")
        self.line_4 = QtWidgets.QFrame(self.grpBox15)
        self.line_4.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.txtDen15 = QtWidgets.QLineEdit(self.grpBox15)
        self.txtDen15.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen15.setText("")
        self.txtDen15.setObjectName("txtDen15")
        self.grpBox14 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox14.setGeometry(QtCore.QRect(550, 20, 61, 101))
        self.grpBox14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox14.setObjectName("grpBox14")
        self.txtNum14 = QtWidgets.QLineEdit(self.grpBox14)
        self.txtNum14.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum14.setText("")
        self.txtNum14.setObjectName("txtNum14")
        self.line_5 = QtWidgets.QFrame(self.grpBox14)
        self.line_5.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.txtDen14 = QtWidgets.QLineEdit(self.grpBox14)
        self.txtDen14.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen14.setText("")
        self.txtDen14.setObjectName("txtDen14")
        self.grpBox13 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox13.setGeometry(QtCore.QRect(470, 20, 61, 101))
        self.grpBox13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox13.setObjectName("grpBox13")
        self.txtNum13 = QtWidgets.QLineEdit(self.grpBox13)
        self.txtNum13.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum13.setText("")
        self.txtNum13.setObjectName("txtNum13")
        self.line_6 = QtWidgets.QFrame(self.grpBox13)
        self.line_6.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.txtDen13 = QtWidgets.QLineEdit(self.grpBox13)
        self.txtDen13.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen13.setText("")
        self.txtDen13.setObjectName("txtDen13")
        self.grpBox23 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox23.setGeometry(QtCore.QRect(470, 120, 61, 101))
        self.grpBox23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox23.setObjectName("grpBox23")
        self.txtNum23 = QtWidgets.QLineEdit(self.grpBox23)
        self.txtNum23.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum23.setText("")
        self.txtNum23.setObjectName("txtNum23")
        self.line_7 = QtWidgets.QFrame(self.grpBox23)
        self.line_7.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.txtDen23 = QtWidgets.QLineEdit(self.grpBox23)
        self.txtDen23.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen23.setText("")
        self.txtDen23.setObjectName("txtDen23")
        self.grpBox25 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox25.setGeometry(QtCore.QRect(630, 120, 61, 101))
        self.grpBox25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox25.setObjectName("grpBox25")
        self.txtNum25 = QtWidgets.QLineEdit(self.grpBox25)
        self.txtNum25.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum25.setText("")
        self.txtNum25.setObjectName("txtNum25")
        self.line_8 = QtWidgets.QFrame(self.grpBox25)
        self.line_8.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.txtDen25 = QtWidgets.QLineEdit(self.grpBox25)
        self.txtDen25.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen25.setText("")
        self.txtDen25.setObjectName("txtDen25")
        self.grpBox22 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox22.setGeometry(QtCore.QRect(390, 120, 61, 101))
        self.grpBox22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox22.setObjectName("grpBox22")
        self.txtNum22 = QtWidgets.QLineEdit(self.grpBox22)
        self.txtNum22.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum22.setText("")
        self.txtNum22.setObjectName("txtNum22")
        self.line_9 = QtWidgets.QFrame(self.grpBox22)
        self.line_9.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.txtDen22 = QtWidgets.QLineEdit(self.grpBox22)
        self.txtDen22.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen22.setText("")
        self.txtDen22.setObjectName("txtDen22")
        self.grpBox24 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox24.setGeometry(QtCore.QRect(550, 120, 61, 101))
        self.grpBox24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox24.setObjectName("grpBox24")
        self.txtNum24 = QtWidgets.QLineEdit(self.grpBox24)
        self.txtNum24.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum24.setText("")
        self.txtNum24.setObjectName("txtNum24")
        self.line_10 = QtWidgets.QFrame(self.grpBox24)
        self.line_10.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.txtDen24 = QtWidgets.QLineEdit(self.grpBox24)
        self.txtDen24.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen24.setText("")
        self.txtDen24.setObjectName("txtDen24")
        self.grpBox21 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox21.setGeometry(QtCore.QRect(310, 120, 61, 101))
        self.grpBox21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox21.setObjectName("grpBox21")
        self.txtNum21 = QtWidgets.QLineEdit(self.grpBox21)
        self.txtNum21.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum21.setText("")
        self.txtNum21.setObjectName("txtNum21")
        self.line_11 = QtWidgets.QFrame(self.grpBox21)
        self.line_11.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.txtDen21 = QtWidgets.QLineEdit(self.grpBox21)
        self.txtDen21.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen21.setText("")
        self.txtDen21.setObjectName("txtDen21")
        self.grpBox33 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox33.setGeometry(QtCore.QRect(470, 220, 61, 101))
        self.grpBox33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox33.setObjectName("grpBox33")
        self.txtNum33 = QtWidgets.QLineEdit(self.grpBox33)
        self.txtNum33.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum33.setText("")
        self.txtNum33.setObjectName("txtNum33")
        self.line_12 = QtWidgets.QFrame(self.grpBox33)
        self.line_12.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.txtDen33 = QtWidgets.QLineEdit(self.grpBox33)
        self.txtDen33.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen33.setText("")
        self.txtDen33.setObjectName("txtDen33")
        self.grpBox35 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox35.setGeometry(QtCore.QRect(630, 220, 61, 101))
        self.grpBox35.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox35.setObjectName("grpBox35")
        self.txtNum35 = QtWidgets.QLineEdit(self.grpBox35)
        self.txtNum35.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum35.setText("")
        self.txtNum35.setObjectName("txtNum35")
        self.line_13 = QtWidgets.QFrame(self.grpBox35)
        self.line_13.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.txtDen35 = QtWidgets.QLineEdit(self.grpBox35)
        self.txtDen35.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen35.setText("")
        self.txtDen35.setObjectName("txtDen35")
        self.grpBox32 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox32.setGeometry(QtCore.QRect(390, 220, 61, 101))
        self.grpBox32.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox32.setObjectName("grpBox32")
        self.txtNum32 = QtWidgets.QLineEdit(self.grpBox32)
        self.txtNum32.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum32.setText("")
        self.txtNum32.setObjectName("txtNum32")
        self.line_14 = QtWidgets.QFrame(self.grpBox32)
        self.line_14.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.txtDen32 = QtWidgets.QLineEdit(self.grpBox32)
        self.txtDen32.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen32.setText("")
        self.txtDen32.setObjectName("txtDen32")
        self.grpBox34 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox34.setGeometry(QtCore.QRect(550, 220, 61, 101))
        self.grpBox34.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox34.setObjectName("grpBox34")
        self.txtNum34 = QtWidgets.QLineEdit(self.grpBox34)
        self.txtNum34.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum34.setText("")
        self.txtNum34.setObjectName("txtNum34")
        self.line_15 = QtWidgets.QFrame(self.grpBox34)
        self.line_15.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.txtDen34 = QtWidgets.QLineEdit(self.grpBox34)
        self.txtDen34.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen34.setText("")
        self.txtDen34.setObjectName("txtDen34")
        self.grpBox31 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox31.setGeometry(QtCore.QRect(310, 220, 61, 101))
        self.grpBox31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox31.setObjectName("grpBox31")
        self.txtNum31 = QtWidgets.QLineEdit(self.grpBox31)
        self.txtNum31.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum31.setText("")
        self.txtNum31.setObjectName("txtNum31")
        self.line_16 = QtWidgets.QFrame(self.grpBox31)
        self.line_16.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.txtDen31 = QtWidgets.QLineEdit(self.grpBox31)
        self.txtDen31.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen31.setText("")
        self.txtDen31.setObjectName("txtDen31")
        self.grpBox43 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox43.setGeometry(QtCore.QRect(470, 320, 61, 101))
        self.grpBox43.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox43.setObjectName("grpBox43")
        self.txtNum43 = QtWidgets.QLineEdit(self.grpBox43)
        self.txtNum43.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum43.setText("")
        self.txtNum43.setObjectName("txtNum43")
        self.line_17 = QtWidgets.QFrame(self.grpBox43)
        self.line_17.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.txtDen43 = QtWidgets.QLineEdit(self.grpBox43)
        self.txtDen43.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen43.setText("")
        self.txtDen43.setObjectName("txtDen43")
        self.grpBox45 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox45.setGeometry(QtCore.QRect(630, 320, 61, 101))
        self.grpBox45.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox45.setObjectName("grpBox45")
        self.txtNum45 = QtWidgets.QLineEdit(self.grpBox45)
        self.txtNum45.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum45.setText("")
        self.txtNum45.setObjectName("txtNum45")
        self.line_18 = QtWidgets.QFrame(self.grpBox45)
        self.line_18.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.txtDen45 = QtWidgets.QLineEdit(self.grpBox45)
        self.txtDen45.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen45.setText("")
        self.txtDen45.setObjectName("txtDen45")
        self.grpBox42 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox42.setGeometry(QtCore.QRect(390, 320, 61, 101))
        self.grpBox42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox42.setObjectName("grpBox42")
        self.txtNum42 = QtWidgets.QLineEdit(self.grpBox42)
        self.txtNum42.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum42.setText("")
        self.txtNum42.setObjectName("txtNum42")
        self.line_19 = QtWidgets.QFrame(self.grpBox42)
        self.line_19.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.txtDen42 = QtWidgets.QLineEdit(self.grpBox42)
        self.txtDen42.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen42.setText("")
        self.txtDen42.setObjectName("txtDen42")
        self.grpBox44 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox44.setGeometry(QtCore.QRect(550, 320, 61, 101))
        self.grpBox44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox44.setObjectName("grpBox44")
        self.txtNum44 = QtWidgets.QLineEdit(self.grpBox44)
        self.txtNum44.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum44.setText("")
        self.txtNum44.setObjectName("txtNum44")
        self.line_20 = QtWidgets.QFrame(self.grpBox44)
        self.line_20.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_20.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.txtDen44 = QtWidgets.QLineEdit(self.grpBox44)
        self.txtDen44.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen44.setText("")
        self.txtDen44.setObjectName("txtDen44")
        self.grpBox41 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox41.setGeometry(QtCore.QRect(310, 320, 61, 101))
        self.grpBox41.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox41.setObjectName("grpBox41")
        self.txtNum41 = QtWidgets.QLineEdit(self.grpBox41)
        self.txtNum41.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum41.setText("")
        self.txtNum41.setObjectName("txtNum41")
        self.line_21 = QtWidgets.QFrame(self.grpBox41)
        self.line_21.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_21.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.txtDen41 = QtWidgets.QLineEdit(self.grpBox41)
        self.txtDen41.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen41.setText("")
        self.txtDen41.setObjectName("txtDen41")
        self.grpBox53 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox53.setGeometry(QtCore.QRect(470, 420, 61, 101))
        self.grpBox53.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox53.setObjectName("grpBox53")
        self.txtNum53 = QtWidgets.QLineEdit(self.grpBox53)
        self.txtNum53.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum53.setText("")
        self.txtNum53.setObjectName("txtNum53")
        self.line_22 = QtWidgets.QFrame(self.grpBox53)
        self.line_22.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.txtDen53 = QtWidgets.QLineEdit(self.grpBox53)
        self.txtDen53.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen53.setText("")
        self.txtDen53.setObjectName("txtDen53")
        self.grpBox55 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox55.setGeometry(QtCore.QRect(630, 420, 61, 101))
        self.grpBox55.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox55.setObjectName("grpBox55")
        self.txtNum55 = QtWidgets.QLineEdit(self.grpBox55)
        self.txtNum55.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum55.setText("")
        self.txtNum55.setObjectName("txtNum55")
        self.line_23 = QtWidgets.QFrame(self.grpBox55)
        self.line_23.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.txtDen55 = QtWidgets.QLineEdit(self.grpBox55)
        self.txtDen55.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen55.setText("")
        self.txtDen55.setObjectName("txtDen55")
        self.grpBox52 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox52.setGeometry(QtCore.QRect(390, 420, 61, 101))
        self.grpBox52.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox52.setObjectName("grpBox52")
        self.txtNum52 = QtWidgets.QLineEdit(self.grpBox52)
        self.txtNum52.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum52.setText("")
        self.txtNum52.setObjectName("txtNum52")
        self.line_24 = QtWidgets.QFrame(self.grpBox52)
        self.line_24.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_24.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.txtDen52 = QtWidgets.QLineEdit(self.grpBox52)
        self.txtDen52.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen52.setText("")
        self.txtDen52.setObjectName("txtDen52")
        self.grpBox54 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox54.setGeometry(QtCore.QRect(550, 420, 61, 101))
        self.grpBox54.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox54.setObjectName("grpBox54")
        self.txtNum54 = QtWidgets.QLineEdit(self.grpBox54)
        self.txtNum54.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum54.setText("")
        self.txtNum54.setObjectName("txtNum54")
        self.line_25 = QtWidgets.QFrame(self.grpBox54)
        self.line_25.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_25.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.txtDen54 = QtWidgets.QLineEdit(self.grpBox54)
        self.txtDen54.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen54.setText("")
        self.txtDen54.setObjectName("txtDen54")
        self.grpBox51 = QtWidgets.QGroupBox(self.centralWidget)
        self.grpBox51.setGeometry(QtCore.QRect(310, 420, 61, 101))
        self.grpBox51.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.grpBox51.setObjectName("grpBox51")
        self.txtNum51 = QtWidgets.QLineEdit(self.grpBox51)
        self.txtNum51.setGeometry(QtCore.QRect(10, 30, 41, 21))
        self.txtNum51.setText("")
        self.txtNum51.setObjectName("txtNum51")
        self.line_26 = QtWidgets.QFrame(self.grpBox51)
        self.line_26.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.line_26.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.txtDen51 = QtWidgets.QLineEdit(self.grpBox51)
        self.txtDen51.setGeometry(QtCore.QRect(10, 70, 41, 21))
        self.txtDen51.setText("")
        self.txtDen51.setObjectName("txtDen51")
        ventanita.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ventanita)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 700, 20))
        self.menuBar.setObjectName("menuBar")
        ventanita.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(ventanita)
        self.statusBar.setObjectName("statusBar")
        ventanita.setStatusBar(self.statusBar)
        # Código para bloquear cosas en el startup
        self.btnCalcularX.setEnabled(False)
        self.btnGuardarCambios.setEnabled(False)
        self.txaResultado.setEnabled(False)
        self.cboMatriz.setEnabled(False)

        self.grpBox11.setEnabled(False)
        self.grpBox12.setEnabled(False)
        self.grpBox13.setEnabled(False)
        self.grpBox14.setEnabled(False)
        self.grpBox15.setEnabled(False)

        self.grpBox21.setEnabled(False)
        self.grpBox22.setEnabled(False)
        self.grpBox23.setEnabled(False)
        self.grpBox24.setEnabled(False)
        self.grpBox25.setEnabled(False)

        self.grpBox31.setEnabled(False)
        self.grpBox32.setEnabled(False)
        self.grpBox33.setEnabled(False)
        self.grpBox34.setEnabled(False)
        self.grpBox35.setEnabled(False)

        self.grpBox41.setEnabled(False)
        self.grpBox42.setEnabled(False)
        self.grpBox43.setEnabled(False)
        self.grpBox44.setEnabled(False)
        self.grpBox45.setEnabled(False)

        self.grpBox51.setEnabled(False)
        self.grpBox52.setEnabled(False)
        self.grpBox53.setEnabled(False)
        self.grpBox54.setEnabled(False)
        self.grpBox55.setEnabled(False)
        # Código ---------------------------------
        self.btnDefinirOrden.clicked.connect(self.inicializarMatrices)
        self.btnGuardarCambios.clicked.connect(self.guardarMatriz)
        self.cboMatriz.currentIndexChanged.connect(self.mostrarMatriz)
        self.btnCalcularX.clicked.connect(self.calcularMatrizX)
        self.retranslateUi(ventanita)
        QtCore.QMetaObject.connectSlotsByName(ventanita)

    def retranslateUi(self, ventanita):
        _translate = QtCore.QCoreApplication.translate
        ventanita.setWindowTitle(_translate("ventanita", "Ejercicio 2"))
        self.cboOrden.setItemText(0, _translate("ventanita", "2"))
        self.cboOrden.setItemText(1, _translate("ventanita", "3"))
        self.cboOrden.setItemText(2, _translate("ventanita", "4"))
        self.cboOrden.setItemText(3, _translate("ventanita", "5"))
        self.label.setText(_translate("ventanita", "Orden de las matrices"))
        self.label_2.setText(_translate("ventanita", "AX + B = C"))
        self.btnDefinirOrden.setText(_translate("ventanita", "Definir"))
        self.label_4.setText(_translate("ventanita", "Consultar / Insertar"))
        self.cboMatriz.setItemText(0, _translate("ventanita", "A"))
        self.cboMatriz.setItemText(1, _translate("ventanita", "B"))
        self.cboMatriz.setItemText(2, _translate("ventanita", "C"))
        self.grpBox11.setTitle(_translate("ventanita", "   (1,1)"))
        self.btnGuardarCambios.setText(_translate("ventanita", "Guardar"))
        self.label_38.setText(_translate("ventanita", "Calcular el valor de X"))
        self.btnCalcularX.setText(_translate("ventanita", "Calcular"))
        self.grpBox12.setTitle(_translate("ventanita", "   (1,2)"))
        self.grpBox15.setTitle(_translate("ventanita", "   (1,5)"))
        self.grpBox14.setTitle(_translate("ventanita", "   (1,4)"))
        self.grpBox13.setTitle(_translate("ventanita", "   (1,3)"))
        self.grpBox23.setTitle(_translate("ventanita", "   (2,3)"))
        self.grpBox25.setTitle(_translate("ventanita", "   (2,5)"))
        self.grpBox22.setTitle(_translate("ventanita", "   (2,2)"))
        self.grpBox24.setTitle(_translate("ventanita", "   (2,4)"))
        self.grpBox21.setTitle(_translate("ventanita", "   (2,1)"))
        self.grpBox33.setTitle(_translate("ventanita", "   (3,3)"))
        self.grpBox35.setTitle(_translate("ventanita", "   (3,5)"))
        self.grpBox32.setTitle(_translate("ventanita", "   (3,2)"))
        self.grpBox34.setTitle(_translate("ventanita", "   (3,4)"))
        self.grpBox31.setTitle(_translate("ventanita", "   (3,1)"))
        self.grpBox43.setTitle(_translate("ventanita", "   (4,3)"))
        self.grpBox45.setTitle(_translate("ventanita", "   (4,5)"))
        self.grpBox42.setTitle(_translate("ventanita", "   (4,2)"))
        self.grpBox44.setTitle(_translate("ventanita", "   (4,4)"))
        self.grpBox41.setTitle(_translate("ventanita", "   (4,1)"))
        self.grpBox53.setTitle(_translate("ventanita", "   (5,3)"))
        self.grpBox55.setTitle(_translate("ventanita", "   (5,5)"))
        self.grpBox52.setTitle(_translate("ventanita", "   (5,2)"))
        self.grpBox54.setTitle(_translate("ventanita", "   (5,4)"))
        self.grpBox51.setTitle(_translate("ventanita", "   (5,1)"))


    def mostrarMatriz(self):
        matrixIndex = self.cboMatriz.currentIndex()
        vista =   [
                        [[self.txtNum11,self.txtDen11]],
                        [[self.txtNum12,self.txtDen12],[self.txtNum21,self.txtDen21],[self.txtNum22,self.txtDen22]],
                        [[self.txtNum13,self.txtDen13],[self.txtNum23,self.txtDen23],[self.txtNum31,self.txtDen31],[self.txtNum32,self.txtDen32],[self.txtNum33,self.txtDen33]],
                        [[self.txtNum14,self.txtDen14],[self.txtNum24,self.txtDen24],[self.txtNum34,self.txtDen34],[self.txtNum41,self.txtDen41],[self.txtNum42,self.txtDen42],[self.txtNum43,self.txtDen43],[self.txtNum44,self.txtDen44]],
                        [[self.txtNum15,self.txtDen15],[self.txtNum25,self.txtDen25],[self.txtNum35,self.txtDen35],[self.txtNum45,self.txtDen45],[self.txtNum51,self.txtDen51],[self.txtNum52,self.txtDen52],[self.txtNum53,self.txtDen53],[self.txtNum54,self.txtDen54],[self.txtNum55,self.txtDen55]]
                  ]

        matriz = [matrizA,matrizB,matrizC,matrizX]

        valores = []

        if len(matriz[matrixIndex]) >= 2:
            valores += [ [[matriz[matrixIndex][0][0].numerator, matriz[matrixIndex][0][0].denominator]] ]
            valores += [ [[matriz[matrixIndex][0][1].numerator, matriz[matrixIndex][0][1].denominator], [matriz[matrixIndex][1][0].numerator, matriz[matrixIndex][1][0].denominator], [matriz[matrixIndex][1][1].numerator, matriz[matrixIndex][1][1].denominator]] ]

        if len(matriz[matrixIndex]) >= 3:
            valores += [ [[matriz[matrixIndex][0][2].numerator, matriz[matrixIndex][0][2].denominator], [matriz[matrixIndex][1][2].numerator, matriz[matrixIndex][1][2].denominator], [matriz[matrixIndex][2][0].numerator, matriz[matrixIndex][2][0].denominator], [matriz[matrixIndex][2][1].numerator, matriz[matrixIndex][2][1].denominator], [matriz[matrixIndex][2][2].numerator, matriz[matrixIndex][2][2].denominator]] ]

        if len(matriz[matrixIndex]) >= 4:
            valores += [ [[matriz[matrixIndex][0][3].numerator, matriz[matrixIndex][0][3].denominator], [matriz[matrixIndex][1][3].numerator, matriz[matrixIndex][1][3].denominator], [matriz[matrixIndex][2][3].numerator, matriz[matrixIndex][2][3].denominator], [matriz[matrixIndex][3][0].numerator, matriz[matrixIndex][3][0].denominator], [matriz[matrixIndex][3][1].numerator, matriz[matrixIndex][3][1].denominator], [matriz[matrixIndex][3][2].numerator, matriz[matrixIndex][3][2].denominator], [matriz[matrixIndex][3][3].numerator, matriz[matrixIndex][3][3].denominator]] ]

        if len(matriz[matrixIndex]) >= 5:
            valores += [ [[matriz[matrixIndex][0][4].numerator, matriz[matrixIndex][0][4].denominator], [matriz[matrixIndex][1][4].numerator, matriz[matrixIndex][1][4].denominator], [matriz[matrixIndex][2][4].numerator, matriz[matrixIndex][2][4].denominator], [matriz[matrixIndex][3][4].numerator, matriz[matrixIndex][3][4].denominator], [matriz[matrixIndex][4][0].numerator, matriz[matrixIndex][4][0].denominator], [matriz[matrixIndex][4][1].numerator, matriz[matrixIndex][4][1].denominator], [matriz[matrixIndex][4][2].numerator, matriz[matrixIndex][4][2].denominator], [matriz[matrixIndex][4][3].numerator, matriz[matrixIndex][4][3].denominator], [matriz[matrixIndex][4][4].numerator, matriz[matrixIndex][4][4].denominator]] ]

        print("matrixIndex: ", matrixIndex)
        print("Indice del orden: ", self.cboOrden.currentIndex())
        print("Len de las matrices A, B, C",len(matrizA),len(matrizB),len(matrizC))
        print("Len de valores: ", len(valores))

        for i in range(0,int(self.cboOrden.currentIndex()+2)):
            for j,k in zip(vista[i],valores[i]):
                j[0].setText(str(k[0]))
                j[1].setText(str(k[1]))

    def validarCasillas(self):
        vista = [
            [[self.txtNum11, self.txtDen11]],
            [[self.txtNum12, self.txtDen12], [self.txtNum21, self.txtDen21], [self.txtNum22, self.txtDen22]],
            [[self.txtNum13, self.txtDen13], [self.txtNum23, self.txtDen23], [self.txtNum31, self.txtDen31], [self.txtNum32, self.txtDen32], [self.txtNum33, self.txtDen33]],
            [[self.txtNum14, self.txtDen14], [self.txtNum24, self.txtDen24], [self.txtNum34, self.txtDen34], [self.txtNum41, self.txtDen41], [self.txtNum42, self.txtDen42], [self.txtNum43, self.txtDen43],[self.txtNum44, self.txtDen44]],
            [[self.txtNum15, self.txtDen15], [self.txtNum25, self.txtDen25], [self.txtNum35, self.txtDen35], [self.txtNum45, self.txtDen45], [self.txtNum51, self.txtDen51], [self.txtNum52, self.txtDen52], [self.txtNum53, self.txtDen53], [self.txtNum54, self.txtDen54], [self.txtNum55, self.txtDen55]]
            ]
        orderIndex = self.cboOrden.currentIndex()

        for i in range(0,orderIndex+2):
            for j in vista[i]:
                try:
                    if type(eval(j[0].text())) != int or type(eval(j[1].text())) != int or j[1].text() == "0" or eval(j[1].text()) < 0:
                        return False
                except:
                        return False
        return True

    def calcularMatrizX(self):
        global matrizX
        if Invertible(matrizA):
            matrizX = np.array(sistemaMatricial(matrizA, matrizB, matrizC)).reshape(len(sistemaMatricial(matrizA, matrizB, matrizC)), len(sistemaMatricial(matrizA, matrizB, matrizC)[0]))
            self.txaResultado.setText("El valor de X ahora se muestra en pantalla.")
            print("El valor de X es: ",matrizX)
            #Suponiendo que está bien:

            self.cboMatriz.addItem("X")
            self.cboMatriz.setCurrentIndex(3)

            self.btnGuardarCambios.setEnabled(False)
            #self.btnCalcularX.setEnabled(False)
            self.btnDefinirOrden.setEnabled(False)
            self.cboOrden.setEnabled(False)
            #self.cboOrden.setCurrentIndex(0)

            cajas = [[self.grpBox11],
                     [self.grpBox12, self.grpBox21, self.grpBox22],
                     [self.grpBox13, self.grpBox23, self.grpBox31, self.grpBox32, self.grpBox33],
                     [self.grpBox14, self.grpBox24, self.grpBox34, self.grpBox41, self.grpBox42, self.grpBox43,
                      self.grpBox44],
                     [self.grpBox15, self.grpBox25, self.grpBox35, self.grpBox45, self.grpBox51, self.grpBox52,
                      self.grpBox53, self.grpBox54, self.grpBox55]
                     ]
            for i in cajas:
                for j in i:
                    j.setEnabled(False)

            #self.btnDefinirOrden.clicked.connect(self.inicializarMatrices)
            self.btnCalcularX.setText("Resetear")
            self.btnCalcularX.clicked.connect(self.resetear)
            self.cboMatriz.setEnabled(True)
            self.btnCalcularX.setEnabled(True)


        else:
            self.txaResultado.setText("Error al calcular la matriz X: \nLa matriz A no tiene inversa.")
            self.cboOrden.setEnabled(False)
            self.btnDefinirOrden.setEnabled(False)
            self.cboMatriz.setEnabled(True)
            self.btnGuardarCambios.setEnabled(True)
            self.btnCalcularX.setEnabled(True)
            self.btnCalcularX.setText("Calcular")
            self.btnCalcularX.clicked.connect(self.calcularMatrizX)

    def getErroresCasillas(self):
        matrixIndex = self.cboMatriz.currentIndex()
        orderIndex  = self.cboOrden.currentIndex()
        res = "Error al guardar la matriz "+["A","B","C"][matrixIndex]+": \n"
        vista = [
            [[self.txtNum11, self.txtDen11]],
            [[self.txtNum12, self.txtDen12], [self.txtNum21, self.txtDen21], [self.txtNum22, self.txtDen22]],
            [[self.txtNum13, self.txtDen13], [self.txtNum23, self.txtDen23], [self.txtNum31, self.txtDen31],
             [self.txtNum32, self.txtDen32], [self.txtNum33, self.txtDen33]],
            [[self.txtNum14, self.txtDen14], [self.txtNum24, self.txtDen24], [self.txtNum34, self.txtDen34],
             [self.txtNum41, self.txtDen41], [self.txtNum42, self.txtDen42], [self.txtNum43, self.txtDen43],
             [self.txtNum44, self.txtDen44]],
            [[self.txtNum15, self.txtDen15], [self.txtNum25, self.txtDen25], [self.txtNum35, self.txtDen35],
             [self.txtNum45, self.txtDen45], [self.txtNum51, self.txtDen51], [self.txtNum52, self.txtDen52],
             [self.txtNum53, self.txtDen53], [self.txtNum54, self.txtDen54], [self.txtNum55, self.txtDen55]]
        ]
        for i in range(0, orderIndex + 2):
            subj = 1
            for j in vista[i]:
                try:
                    if type(eval(j[0].text())) != int or type(eval(j[1].text())) != int:
                        res += "Valor inválido \n"

                except:
                    res += "Valor inválido \n"
                try:
                    if eval(j[1].text()) < 0:
                        res += "Denominador negativo \n"
                except:
                    res += "Valor inválido \n"


                if j[1].text() == "0":
                    res += "Denominador 0 \n"
                subj += 1
        return res

    def guardarMatriz(self):

        if self.validarCasillas():

            matrixIndex = self.cboMatriz.currentIndex()
            matriz = []
            if matrixIndex == 0:
                matriz = matrizA
            elif matrixIndex == 1:
                matriz = matrizB
            else:
                matriz = matrizC

            if len(matriz)  >= 1:
                matriz[0][0] = Fraction(self.txtNum11.text()+"/"+self.txtDen11.text())

            if len(matriz) >= 2:
                matriz[0][1] = Fraction(self.txtNum12.text() + "/" + self.txtDen12.text())
                matriz[1][0] = Fraction(self.txtNum21.text() + "/" + self.txtDen21.text())
                matriz[1][1] = Fraction(self.txtNum22.text() + "/" + self.txtDen22.text())

            if len(matriz) >= 3:
                matriz[0][2] = Fraction(self.txtNum13.text() + "/" + self.txtDen13.text())
                matriz[1][2] = Fraction(self.txtNum23.text() + "/" + self.txtDen23.text())
                matriz[2][0] = Fraction(self.txtNum31.text() + "/" + self.txtDen31.text())
                matriz[2][1] = Fraction(self.txtNum32.text() + "/" + self.txtDen32.text())
                matriz[2][2] = Fraction(self.txtNum33.text() + "/" + self.txtDen33.text())

            if len(matriz) >= 4:
                matriz[0][3] = Fraction(self.txtNum14.text() + "/" + self.txtDen14.text())
                matriz[1][3] = Fraction(self.txtNum24.text() + "/" + self.txtDen24.text())
                matriz[2][3] = Fraction(self.txtNum34.text() + "/" + self.txtDen34.text())
                matriz[3][0] = Fraction(self.txtNum41.text() + "/" + self.txtDen41.text())
                matriz[3][1] = Fraction(self.txtNum42.text() + "/" + self.txtDen42.text())
                matriz[3][2] = Fraction(self.txtNum43.text() + "/" + self.txtDen43.text())
                matriz[3][3] = Fraction(self.txtNum44.text() + "/" + self.txtDen44.text())

            if len(matriz) >= 5:
                matriz[0][4] = Fraction(self.txtNum15.text() + "/" + self.txtDen15.text())
                matriz[1][4] = Fraction(self.txtNum25.text() + "/" + self.txtDen25.text())
                matriz[2][4] = Fraction(self.txtNum35.text() + "/" + self.txtDen35.text())
                matriz[3][4] = Fraction(self.txtNum45.text() + "/" + self.txtDen45.text())
                matriz[4][0] = Fraction(self.txtNum51.text() + "/" + self.txtDen51.text())
                matriz[4][1] = Fraction(self.txtNum52.text() + "/" + self.txtDen52.text())
                matriz[4][2] = Fraction(self.txtNum53.text() + "/" + self.txtDen53.text())
                matriz[4][3] = Fraction(self.txtNum54.text() + "/" + self.txtDen54.text())
                matriz[4][4] = Fraction(self.txtNum55.text() + "/" + self.txtDen55.text())

            #Reasignacion de los resultados guardados
            [matrizA,matrizB,matrizC][matrixIndex] = matriz

            self.txaResultado.setText("La matriz "+["A","B","C"][matrixIndex]+" ha sido guardada correctamente.")

        else: #No se valido alguna casilla
            self.txaResultado.setText(self.getErroresCasillas())

    def inicializarMatrices(self):
        global matrizA, matrizB, matrizC, matrizX
        temp = []
        final = []

        self.limpiarCasillas()

        cajas= [[self.grpBox11],
                [self.grpBox12, self.grpBox21, self.grpBox22],
                [self.grpBox13, self.grpBox23, self.grpBox31, self.grpBox32, self.grpBox33],
                [self.grpBox14, self.grpBox24, self.grpBox34, self.grpBox41, self.grpBox42, self.grpBox43, self.grpBox44],
                [self.grpBox15, self.grpBox25, self.grpBox35, self.grpBox45, self.grpBox51, self.grpBox52, self.grpBox53, self.grpBox54, self.grpBox55]
               ]

        for i in range(0,int(self.cboOrden.currentIndex()+2)):
            for j in cajas[i]:
                j.setEnabled(True)


        #Probar esta picha
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)

        self.cboMatriz.addItem("B")
        self.cboMatriz.addItem("C")
        #=================

        self.btnDefinirOrden.setEnabled(False)
        self.cboOrden.setEnabled(False)
        self.btnGuardarCambios.setEnabled(True)
        self.cboMatriz.setEnabled(True)
        self.btnCalcularX.setEnabled(True)

        print("Al inicializar las matrices, el orden definido es: ",self.cboOrden.currentIndex()+2)


        # Matriz temporal[i]
        temp = [Fraction("1/1")] * int(self.cboOrden.currentIndex() + 2)
        res = copy.deepcopy([temp]) * int(self.cboOrden.currentIndex() + 2)

        matrizA = np.array(copy.deepcopy(res)).reshape(len(res),len(res[0]))
        matrizB = np.array(copy.deepcopy(res)).reshape(len(res),len(res[0]))
        matrizC = np.array(copy.deepcopy(res)).reshape(len(res),len(res[0]))
        matrizX = np.array(copy.deepcopy(res)).reshape(len(res), len(res[0]))
        print("Current Matrix index: ",self.cboMatriz.currentIndex())
        print("Current Order index: ",self.cboOrden.currentIndex())
        self.mostrarMatriz()

    def resetear(self):

        self.cboMatriz.setCurrentIndex(0)
        self.cboMatriz.setEnabled(False)
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)
        self.cboMatriz.removeItem(1)

        self.cboMatriz.addItem("B")
        self.cboMatriz.addItem("C")

        self.cboOrden.setEnabled(True)
        self.btnDefinirOrden.setEnabled(True)
        self.btnCalcularX.setText("Calcular")
        self.btnCalcularX.clicked.connect(self.calcularMatrizX)
        self.btnCalcularX.setEnabled(False)


    def limpiarCasillas(self):
        vista = [
            [[self.txtNum11, self.txtDen11]],
            [[self.txtNum12, self.txtDen12], [self.txtNum21, self.txtDen21], [self.txtNum22, self.txtDen22]],
            [[self.txtNum13, self.txtDen13], [self.txtNum23, self.txtDen23], [self.txtNum31, self.txtDen31],
             [self.txtNum32, self.txtDen32], [self.txtNum33, self.txtDen33]],
            [[self.txtNum14, self.txtDen14], [self.txtNum24, self.txtDen24], [self.txtNum34, self.txtDen34],
             [self.txtNum41, self.txtDen41], [self.txtNum42, self.txtDen42], [self.txtNum43, self.txtDen43],
             [self.txtNum44, self.txtDen44]],
            [[self.txtNum15, self.txtDen15], [self.txtNum25, self.txtDen25], [self.txtNum35, self.txtDen35],
             [self.txtNum45, self.txtDen45], [self.txtNum51, self.txtDen51], [self.txtNum52, self.txtDen52],
             [self.txtNum53, self.txtDen53], [self.txtNum54, self.txtDen54], [self.txtNum55, self.txtDen55]]
        ]
        for i in vista:
            for j in i:
                for k in j:
                    k.setText("")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanita = QtWidgets.QMainWindow()
    ui = Ui_ventanita()
    ui.setupUi(ventanita)
    ventanita.show()
    sys.exit(app.exec_())



