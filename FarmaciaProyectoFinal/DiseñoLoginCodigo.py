# -*- coding: utf-8 -*-

import sys
from PyQt5.Qt import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QLineEdit, QPushButton, QWidget, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
import DiseñoRegisterCodigo

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(509, 526)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbUsuarioLogin = QtWidgets.QLabel(self.centralwidget)
        self.lbUsuarioLogin.setGeometry(QtCore.QRect(140, 180, 101, 20))
        self.lbUsuarioLogin.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 14pt \"Arial\";")
        self.lbUsuarioLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lbUsuarioLogin.setObjectName("lbUsuarioLogin")
        self.leUsuarioLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leUsuarioLogin.setGeometry(QtCore.QRect(150, 210, 231, 20))
        self.leUsuarioLogin.setStyleSheet("color: rgb(255, 255, 255);")
        self.leUsuarioLogin.setObjectName("leUsuarioLogin")
        self.leContraLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.leContraLogin.setGeometry(QtCore.QRect(150, 300, 231, 20))
        self.leContraLogin.setStyleSheet("color: rgb(255, 255, 255);")
        self.leContraLogin.setText("")
        self.leContraLogin.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leContraLogin.setObjectName("leContraLogin")
        self.lbContraLogin = QtWidgets.QLabel(self.centralwidget)
        self.lbContraLogin.setGeometry(QtCore.QRect(150, 270, 101, 20))
        self.lbContraLogin.setStyleSheet("color: rgb(255, 255, 255);\n""font: 87 14pt \"Arial\";")
        self.lbContraLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.lbContraLogin.setObjectName("lbContraLogin")
        self.pbRegistrarse = QtWidgets.QPushButton(self.centralwidget)
        self.pbRegistrarse.setGeometry(QtCore.QRect(170, 360, 191, 61))
        self.pbRegistrarse.setStyleSheet("border-color: rgb(170, 0, 255);\n""background-color: rgb(170, 0, 255);\n""color: rgb(255, 255, 255);\n""font: 75 16pt \"Arial\";\n""")
        self.pbRegistrarse.setObjectName("pbRegistrarse")
        self.pbNoCuenta = QtWidgets.QPushButton(self.centralwidget)
        self.pbNoCuenta.setGeometry(QtCore.QRect(20, 460, 131, 21))
        self.pbNoCuenta.setStyleSheet("border-color: rgb(170, 0, 255);\n""background-color: rgb(170, 0, 255);\n""color: rgb(255, 255, 255);\n""font: 75 8pt \"Arial\";\n""")
        self.pbNoCuenta.setObjectName("pbNoCuenta")
        self.iconoLogin = QtWidgets.QLabel(self.centralwidget)
        self.iconoLogin.setGeometry(QtCore.QRect(190, 20, 141, 131))
        self.iconoLogin.setText("")
        self.iconoLogin.setPixmap(QtGui.QPixmap("IconoFarmacia.jpg"))
        self.iconoLogin.setScaledContents(True)
        self.iconoLogin.setObjectName("iconoLogin")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 509, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Llamando a la ventana Register con el boton de no tienes una cuenta
        self.pbNoCuenta.clicked.connect(self.conectarRegister)
        
    def conectarRegister(self):
        self.DiseñoRegisterCodigo.show()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbUsuarioLogin.setText(_translate("MainWindow", "Usuario"))
        self.lbContraLogin.setText(_translate("MainWindow", "Contraseña"))
        self.pbRegistrarse.setText(_translate("MainWindow", "Registrarse"))
        self.pbNoCuenta.setText(_translate("MainWindow", "¿No tienes una cuenta?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

