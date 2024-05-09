# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiseñoDiasVentas.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 579)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iconoProducto = QtWidgets.QLabel(self.centralwidget)
        self.iconoProducto.setGeometry(QtCore.QRect(320, -7, 181, 141))
        self.iconoProducto.setStyleSheet("")
        self.iconoProducto.setText("")
        self.iconoProducto.setPixmap(QtGui.QPixmap("IconoFarmacia2.jpg"))
        self.iconoProducto.setScaledContents(True)
        self.iconoProducto.setObjectName("iconoProducto")
        self.verVenta = QtWidgets.QListView(self.centralwidget)
        self.verVenta.setGeometry(QtCore.QRect(100, 138, 629, 359))
        self.verVenta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verVenta.setObjectName("verVenta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 21))
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

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

