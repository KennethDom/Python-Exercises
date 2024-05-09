# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 09:01:58 2021

@author: Usuario
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        #Para conectar la base de datos
        self.tabla = QTableView()
        self.modelo = QSqlTableModel(db = dba)                   #El db no cambia
        self.tabla.setModel(self.modelo)
        self.modelo.setTable("Pista")                            #Nombre de la  tabla de nuestra base de datos
        
        self.modelo.setHeaderData(0,Qt.Horizontal, "Id")         #Cambiar nombre de columnas
        self.modelo.setHeaderData(1,Qt.Horizontal, "Nombre")     #Cambiar nombre de columnas
        
        #self.modelo.removeColumns(4,2)                          #Remover columnas
        
        self.modelo.select()
        
        self.setMinimumSize(QSize(900,600))                      #Adaptando el tamaño de la tabla
        self.setCentralWidget(self.tabla) 
        

app = QApplication(sys.argv)
dba = QSqlDatabase("QSQLITE")
dba.setDatabaseName("album_pistas.db")
dba.open()
win = MainWindow()
win.show()
app.exec_() 