# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secuenciaInter.ui'
#
# Created by: PyQt5 UI code generator 5.8
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_SecuenciaCambiosInter(object):
    def setupUi(self, SecuenciaCambiosInter):
        SecuenciaCambiosInter.setObjectName("SecuenciaCambiosInter")
        SecuenciaCambiosInter.resize(523, 321)
        self.scrollArea = QtWidgets.QScrollArea(SecuenciaCambiosInter)
        self.scrollArea.setGeometry(QtCore.QRect(10, 10, 501, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 299))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 280, 501, 16))
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(SecuenciaCambiosInter)
        QtCore.QMetaObject.connectSlotsByName(SecuenciaCambiosInter)

    def retranslateUi(self, SecuenciaCambiosInter):
        _translate = QtCore.QCoreApplication.translate
        SecuenciaCambiosInter.setWindowTitle(_translate("SecuenciaCambiosInter", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecuenciaCambiosInter = QtWidgets.QWidget()
    ui = Ui_SecuenciaCambiosInter()
    ui.setupUi(SecuenciaCambiosInter)
    SecuenciaCambiosInter.show()
    sys.exit(app.exec_())

