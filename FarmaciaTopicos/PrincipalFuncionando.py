import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5.QtSql import *
from PyQt5.QtGui import QPixmap

#Clase para registrar a los empleados
class Registrar(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("RegistrarUsuarios.ui",self)

        #Agregamos el logo a la pantalla
        self.et_logo.setPixmap(QPixmap("IconoFarmacia.jpg"))
        self.et_logo.setScaledContents(True)

        #Conectamos la pantalla a un metodo para que funcione de mejor manera
        self.pbRegistrarse.clicked.connect(self.ingresa)
    #Metodo en el que se agrega lo que el usuario teclee a la tabla de empleado
    def ingresa(self,event):
        identificador = int(self.identi.text())
        nombre = self.leNombreRegister.text()
        apellido = self.leApellidosRegister.text()
        usuario = self.leUsuarioRegister.text()
        contraseña = self.leContraRegister.text()

        query = QSqlQuery(db=dba)
        query.exec_("INSERT INTO Empleado VALUES({0},'{1}','{2}','{3}','{4}')".format(identificador,nombre,apellido,usuario,contraseña))


#Clase del menu principal de la aplicacion
class Opciones(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Menu.ui", self)

        #Definimos lo que hace cada boton mediante metodos
        self.pb_venta.clicked.connect(self.vender)
        self.pb_ver.clicked.connect(self.mostrarVentas)
        self.pb_empleados.clicked.connect(self.mostrarEmpleados)

    def vender(self):
        self.venta = Venta()
        self.venta.show()

    def mostrarVentas(self):
        self.mostrar = Mostrar_ventas()
        self.mostrar.show()

    def mostrarEmpleados(self):
        self.empleado = VerEmpleados()
        self.empleado.show()


#Clase para ver los registros almacenados de los empleados con los que cuenta el negocio
class VerEmpleados(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("VerEmpleados.ui", self)

        #Creamos metodos para los botones de la interfaz
        self.pb_atr.clicked.connect(self.atras)
        self.pb_mod.clicked.connect(self.modificar)

        #A la tabla de la interfaz le asignamos la tabla correspondiente de la base de datos
        self.modelo = QSqlTableModel(db=dba)
        self.tab_emp.setModel(self.modelo)
        self.modelo.setTable("Empleado")
        self.modelo.select()


    def atras(self):
        self.atras = Opciones()
        self.atras.show()

    def modificar(self):
        pass


#Clase para controlar las ventas del negocio
class Venta(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ventas.ui", self)

        #Primero a la tabla de la interfaz le añadimos la tabla productos de la base de datos para que el empleado pueda consultar de mejor manera
        self.modelo = QSqlTableModel(db=dba)
        self.tab_productos.setModel(self.modelo)
        self.modelo.setTable("Productos")
        self.modelo.select()
        self.registrar.clicked.connect(self.agregarVenta)

    def agregarVenta(self,event):
        identificador = int(self.le_num.text())
        nombre = self.le_nombre.text()
        fecha = self.le_fecha.text()
        cantidad= int(self.le_cantidad.text())
        total = float(self.le_total.text())
        idemp = self.le_Empleado.text()
        idprod = self.le_Producto.text()
        query= QSqlQuery(db=dba)
        query.exec_("INSERT INTO Venta VALUES({0},{1},{2},'{3}','{4}',{5},{6})".format(identificador,idprod,idemp,nombre,fecha,cantidad,total))



#Clase para mostrar las ventas que se han echo en el negocio
class Mostrar_ventas(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("MostrarVentas.ui", self)

        #Creamos metodos para el control de la interfaz
        self.vendermas.clicked.connect(self.seguir)
        self.terminar.clicked.connect(self.finalizar)

        #A la tabla de la interfaz le asignamos la tabla ventas de la base de datos
        self.modelo = QSqlTableModel(db=dba)
        self.tab_ventas.setModel(self.modelo)
        self.modelo.setTable("Venta")
        self.modelo.select()

    def seguir(self):
        self.vender = Venta()
        self.vender.show()

    def finalizar(self):
        sys.exit()


#Clase principal, desde aqui se controla toda la interfaz
class Ejemplo(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('DiseñoLogin.ui', self)
        self.et_logo.setPixmap(QPixmap("IconoFarmacia.jpg"))
        self.et_logo.setScaledContents(True)
    #Creamos metodos para que el usuario pueda acceder a las ventas o registrar a algun empleado
        self.pbNoCuenta.clicked.connect(self.conexion)
        self.pb_ingresar.clicked.connect(self.opciones)

    def conexion(self):
        self.registrar = Registrar()
        self.registrar.show()

    def opciones(self):
        usuario = self.leUsuarioLogin.text()
        contraseña = self.leContraLogin.text()
        query = QSqlQuery(db=dba)
        query.exec_("SELECT * FROM Empleado WHERE usuario =? AND contraseña =? ".format(usuario,contraseña))
        if query.result():
            self.opcion = Opciones()
            self.opcion.show()
        else:
            print("Usuario y contraseña incorrectos")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dba= QSqlDatabase("QSQLITE")
    dba.setDatabaseName("farmaciabasededatos.db")
    dba.open()
    GUI = Ejemplo()
    GUI.show()
    sys.exit(app.exec())
        
    