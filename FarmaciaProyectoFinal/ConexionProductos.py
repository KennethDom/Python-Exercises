# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 14:44:59 2021

@author: Usuario
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QLabel,QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel,QSqlQuery


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        lay = QVBoxLayout()
        busqueda = QLabel("Busqueda")
        self.busqueda = QLineEdit()
        self.busqueda.textChanged.connect(self.actualizarFiltro)

        self.tabla = QTableView()
        self.modelo = QSqlTableModel(db=dba)
        self.tabla.setModel(self.modelo)
        self.modelo.setTable("Productos")

        lay.addWidget(busqueda)
        lay.addWidget(self.busqueda)
        lay.addWidget(self.tabla)
        widget.setLayout(lay)
        
        self.modelo.select()

        self.setMinimumSize(QSize(900,600))
        self.setCentralWidget(widget)

    def actualizarFiltro(self,s):
        filtro_str = 'nombre LIKE"%{}%"'.format(s)
        self.modelo.setFilter(filtro_str)

    def consultar(self,s):
        query = QSqlQuery(s,db = dba)
        self.modelo.setQuery(query)

app = QApplication(sys.argv)
dba = QSqlDatabase("QSQLITE")
dba.setDatabaseName("farmaciabasededatos.db")
dba.open()
win = MainWindow()
win.show()
sys.exit(app.exec())