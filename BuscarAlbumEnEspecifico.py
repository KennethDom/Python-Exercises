# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:07:45 2021

@author: Usuario
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel,QSqlQuery,QSqlQueryModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.tabla = QTableView()
        self.modelo = QSqlQueryModel()
        self.tabla.setModel(self.modelo)
        
        query = QSqlQuery(db = dba)
        
        query.prepare(
            "SELECT nombre, compositor, Album.Title FROM Pista "
            "INNER JOIN Album ON Pista.albumId = Album.albumId "
            "WHERE Album.Title LIKE '%' || :album_title || '%'"
            )
        
        query.bindValue(":album_title", "Thriller")
        query.exec_()
        self.modelo.setQuery(query)
        
        self.setMinimumSize(QSize(900,600))
        self.setCentralWidget(self.tabla)        
        
app = QApplication(sys.argv)
dba = QSqlDatabase("QSQLITE")
dba.setDatabaseName("album_pistas.db")
dba.open()
win = MainWindow()
win.show()
sys.exit(app.exec())