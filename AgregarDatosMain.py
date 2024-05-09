import sqlite3
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Agenda")
        layout = QVBoxLayout()
        widget = QWidget()

        et1 = QLabel("Nombre")
        et2 = QLabel("Apellido")
        et3 = QLabel("Telefono")
        et4 = QLabel("Email")
        self.le0 = QLineEdit()
        self.le1 = QLineEdit()
        self.le2 = QLineEdit()
        self.le3 = QLineEdit()
        self.le4 = QLineEdit()
        bt0 = QPushButton("Buscar")
        self.bt1 = QPushButton("Agregar")
        bt2 = QPushButton("Modificar")
        bt3 = QPushButton("Borrar")
        bt4 = QPushButton("Nuevo")

        self.le0.setPlaceholderText("Busqueda por id")

        bt0.clicked.connect(self.buscar)
        self.bt1.clicked.connect(self.insertar)
        bt2.clicked.connect(self.modificar)
        bt3.clicked.connect(self.borrar)
        bt4.clicked.connect(self.borrarEdit)

        widget.setLayout(layout)
        layout.addWidget(self.le0)
        layout.addWidget(bt0)
        layout.addWidget(et1)
        layout.addWidget(self.le1)
        layout.addWidget(et2)
        layout.addWidget(self.le2)
        layout.addWidget(et3)
        layout.addWidget(self.le3)
        layout.addWidget(et4)
        layout.addWidget(self.le4)
        layout.addWidget(self.bt1)
        layout.addWidget(bt2)
        layout.addWidget(bt3)
        layout.addWidget(bt4)

        self.setCentralWidget(widget)

    def insertar(self):
        nombre = self.le1.text()
        apellido = self.le2.text()
        telefono = self.le3.text()
        correo = self.le4.text()
        insertarRegistro(nombre, apellido, telefono, correo)

    def modificar(self):
        id = int(self.le0.text())
        nombre = self.le1.text()
        apellido = self.le2.text()
        telefono = self.le3.text()
        correo = self.le4.text()
        modificarRegistro(id, nombre, apellido, telefono, correo)
        self.bt1.setEnabled(True)

    def borrar(self):
        id = self.le0.text()
        borrarRegistro(id)
        self.bt1.setEnabled(True)

    def buscar(self):
        id = self.le0.text()
        datos = busqueda(id)
        self.le1.setText(datos[0])
        self.le2.setText(datos[1])
        self.le3.setText(datos[2])
        self.le4.setText(datos[3])
        self.bt1.setEnabled(False)

    def borrarEdit(self):
        self.le0.setText("")
        self.le1.setText("")
        self.le2.setText("")
        self.le3.setText("")
        self.le4.setText("")
        self.le0.setFocus(True)
        self.bt1.setEnabled(True)


def crearTabla():
    conexion = sqlite3.connect('Agenda.db')
    consulta = conexion.cursor()
    sql = """CREATE TABLE IF NOT EXISTS agenda(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre VARCHAR(20) NOT NULL, 
             apellido VARCHAR(20) NOT NULL, telefono VARCHAR(10) NOT NULL, correo VARCHAR(20) NOT NULL)"""
    if consulta.execute(sql):
        print("Tabla creada")
    else:
        print("No fue creada la tabla")
    conexion.close()

def insertarRegistro(nombre, apellido, telefono, correo):
    conexion = sqlite3.connect('Agenda.db')
    consulta = conexion.cursor()

    datos = (nombre, apellido, telefono, correo)

    sql = """INSERT INTO agenda (nombre, apellido, telefono, correo) VALUES (?,?,?,?)"""

    if consulta.execute(sql, datos):
        print("Registro guardado")
        conexion.commit()
    else:
        print("Registro no guardado")
    conexion.close()

def busqueda(id):
    conexion = sqlite3.connect('Agenda.db')
    consulta = conexion.cursor()
    datos = ("", "", "", "")
    sql = """SELECT nombre, apellido, telefono, correo FROM agenda WHERE (id = ?)"""
    encontro = False
    try:
        consulta.execute(sql, id)
        for i in consulta:
            nombre = (i[0])
            apellido = (i[1])
            telefono = (i[2])
            correo = (i[3])
            datos = (nombre, apellido, telefono, correo)
            encontro = True
        if encontro:
            print("Registro encontrado")
        else:
            print("Registro no encontrado")
        return datos
    except:
        print("Registro no encontrado")
    conexion.close()

def modificarRegistro(id, nombre, apellido, telefono, correo):
    conexion = sqlite3.connect('Agenda.db')
    consulta = conexion.cursor()
    datos = (nombre, apellido, telefono, correo, id)
    sql = """UPDATE agenda SET nombre = ?, apellido = ?, telefono = ?, correo = ? WHERE (id = ?)"""
    if consulta.execute(sql, datos):
        print("Registro fue actualizado")
        conexion.commit()
    else:
        print("El registro no fue actualizado")
    conexion.close()

def borrarRegistro(id):
    conexion = sqlite3.connect('Agenda.db')
    consulta = conexion.cursor()
    sql = """DELETE FROM agenda WHERE (id = ?)""" #Drop
    consulta.execute(sql, id)                     #Se puede poner como if pero se asume que el usuario conoce el registro ya que tiene que buscarlo primero
    print("El registro fue borrado")
    conexion.commit()
    conexion.close()

app = QApplication(sys.argv)
crearTabla()
win = MainWindow()
win.show()
app.exec()