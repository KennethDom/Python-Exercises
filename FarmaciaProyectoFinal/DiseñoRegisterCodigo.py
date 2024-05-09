# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiseñoRegister.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(507, 596)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leContraRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.leContraRegister.setGeometry(QtCore.QRect(130, 420, 231, 20))
        self.leContraRegister.setStyleSheet("color: rgb(255, 255, 255);")
        self.leContraRegister.setText("")
        self.leContraRegister.setEchoMode(QtWidgets.QLineEdit.Password)
        self.leContraRegister.setObjectName("leContraRegister")
        self.leUsuarioRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.leUsuarioRegister.setGeometry(QtCore.QRect(130, 210, 231, 20))
        self.leUsuarioRegister.setStyleSheet("color: rgb(255, 255, 255);")
        self.leUsuarioRegister.setObjectName("leUsuarioRegister")
        self.iconoRegister = QtWidgets.QLabel(self.centralwidget)
        self.iconoRegister.setGeometry(QtCore.QRect(180, 0, 161, 161))
        self.iconoRegister.setStyleSheet("")
        self.iconoRegister.setText("")
        self.iconoRegister.setPixmap(QtGui.QPixmap("IconoFarmacia.jpg"))
        self.iconoRegister.setScaledContents(True)
        self.iconoRegister.setObjectName("iconoRegister")
        self.lbUsuarioRegister = QtWidgets.QLabel(self.centralwidget)
        self.lbUsuarioRegister.setGeometry(QtCore.QRect(120, 180, 101, 20))
        self.lbUsuarioRegister.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.lbUsuarioRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.lbUsuarioRegister.setObjectName("lbUsuarioRegister")
        self.pbRegistrarse = QtWidgets.QPushButton(self.centralwidget)
        self.pbRegistrarse.setGeometry(QtCore.QRect(150, 490, 191, 61))
        self.pbRegistrarse.setStyleSheet("border-color: rgb(170, 0, 255);\n"
"font: 75 14pt \"Arial\";\n"
"background-color: rgb(170, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"")
        self.pbRegistrarse.setObjectName("pbRegistrarse")
        self.lbContraRegister = QtWidgets.QLabel(self.centralwidget)
        self.lbContraRegister.setGeometry(QtCore.QRect(130, 390, 101, 20))
        self.lbContraRegister.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.lbContraRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.lbContraRegister.setObjectName("lbContraRegister")
        self.lbNombreRegister = QtWidgets.QLabel(self.centralwidget)
        self.lbNombreRegister.setGeometry(QtCore.QRect(120, 250, 101, 20))
        self.lbNombreRegister.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.lbNombreRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.lbNombreRegister.setObjectName("lbNombreRegister")
        self.leNombreRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.leNombreRegister.setGeometry(QtCore.QRect(130, 280, 231, 20))
        self.leNombreRegister.setStyleSheet("color: rgb(255, 255, 255);")
        self.leNombreRegister.setObjectName("leNombreRegister")
        self.lbApellidoRegister = QtWidgets.QLabel(self.centralwidget)
        self.lbApellidoRegister.setGeometry(QtCore.QRect(120, 320, 101, 20))
        self.lbApellidoRegister.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial\";")
        self.lbApellidoRegister.setAlignment(QtCore.Qt.AlignCenter)
        self.lbApellidoRegister.setObjectName("lbApellidoRegister")
        self.leApellidosRegister = QtWidgets.QLineEdit(self.centralwidget)
        self.leApellidosRegister.setGeometry(QtCore.QRect(130, 350, 231, 20))
        self.leApellidosRegister.setStyleSheet("color: rgb(255, 255, 255);")
        self.leApellidosRegister.setObjectName("leApellidosRegister")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 507, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbUsuarioRegister.setText(_translate("MainWindow", "Usuario"))
        self.pbRegistrarse.setText(_translate("MainWindow", "Registrarse"))
        self.lbContraRegister.setText(_translate("MainWindow", "Contraseña"))
        self.lbNombreRegister.setText(_translate("MainWindow", "Nombre"))
        self.lbApellidoRegister.setText(_translate("MainWindow", "Apellidos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

