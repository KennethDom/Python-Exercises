
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QLabel,QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel,QSqlQuery
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 603)
        MainWindow.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.iconoVentaProductos = QtWidgets.QLabel(self.centralwidget)
        self.iconoVentaProductos.setGeometry(QtCore.QRect(250, -20, 171, 151))
        self.iconoVentaProductos.setStyleSheet("")
        self.iconoVentaProductos.setText("")
        self.iconoVentaProductos.setPixmap(QtGui.QPixmap("IconoFarmacia2.jpg"))
        self.iconoVentaProductos.setScaledContents(True)
        self.iconoVentaProductos.setObjectName("iconoVentaProductos")
        self.verProductos = QtWidgets.QListView(self.centralwidget)
        self.verProductos.setGeometry(QtCore.QRect(22, 159, 629, 359))
        self.verProductos.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verProductos.setObjectName("verProductos")
        self.registraVenta = QtWidgets.QPushButton(self.centralwidget)
        self.registraVenta.setGeometry(QtCore.QRect(340, 524, 311, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.registraVenta.setFont(font)
        self.registraVenta.setStyleSheet("background-color: rgb(255, 255, 255);\n""\n""")
        self.registraVenta.setObjectName("registraVenta")
        self.borrarVenta = QtWidgets.QPushButton(self.centralwidget)
        self.borrarVenta.setGeometry(QtCore.QRect(22, 524, 312, 26))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.borrarVenta.setFont(font)
        self.borrarVenta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.borrarVenta.setObjectName("borrarVenta")
        self.buscarProducto = QtWidgets.QLineEdit(self.centralwidget)
        self.buscarProducto.setGeometry(QtCore.QRect(22, 131, 631, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.buscarProducto.setFont(font)
        self.buscarProducto.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 75 10pt \"Arial\";\n""")
        self.buscarProducto.setAlignment(QtCore.Qt.AlignCenter)
        self.buscarProducto.setObjectName("buscarProducto")
        self.lbCantidadMostrar = QtWidgets.QLineEdit(self.centralwidget)
        self.lbCantidadMostrar.setGeometry(QtCore.QRect(662, 159, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbCantidadMostrar.setFont(font)
        self.lbCantidadMostrar.setStyleSheet("background-color: rgb(255, 255, 255);\n""font: 75 10pt \"Arial\";\n""")
        self.lbCantidadMostrar.setAlignment(QtCore.Qt.AlignCenter)
        self.lbCantidadMostrar.setObjectName("lbCantidadMostrar")
        self.leCantidad = QtWidgets.QLabel(self.centralwidget)
        self.leCantidad.setGeometry(QtCore.QRect(680, 130, 91, 20))
        self.leCantidad.setStyleSheet("font: 75 12pt \"Arial\";\n""")
        self.leCantidad.setObjectName("leCantidad")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 21))
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
        self.registraVenta.setText(_translate("MainWindow", "Registrar Venta"))
        self.borrarVenta.setText(_translate("MainWindow", "Borrar Venta"))
        self.leCantidad.setText(_translate("MainWindow", "CANTIDAD"))

    def conexionbasedatos(self, MainWindow):
        self.tabla = QTableView()
        self.modelo = QSqlTableModel(db=dba)
        self.tabla.setModel(self.modelo)
        self.modelo.setTable("Productos")

    def actualizarFiltro(self,s):
        filtro_str = 'nombre LIKE"%{}%"'.format(s)
        self.modelo.setFilter(filtro_str)

    def consultar(self,s):
        query = QSqlQuery(s,db = dba)
        self.modelo.setQuery(query)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dba = QSqlDatabase("QSQLITE")
    dba.setDatabaseName("farmaciabasededatos.db")
    dba.open()
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

