# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 09:27:19 2021

@author: Usuario
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QLineEdit, QHBoxLayout, QWidget
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel,QSqlQuery,QSqlQueryModel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        widget = QWidget()
        lay1 = QHBoxLayout()
        
        self.pista = QLineEdit()
        self.pista.setPlaceholderText("Nombre de la Pista")
        self.pista.textChanged.connect(self.actualizarQuery)
        
        self.compositor = QLineEdit()
        self.compositor.setPlaceholderText("Nombre del compositor")
        self.compositor.textChanged.connect(self.actualizarQuery)
        
        self.album = QLineEdit()
        self.album.setPlaceholderText("Nombre del Album")
        self.album.textChanged.connect(self.actualizarQuery)
        
        lay1.addWidget(self.pista)
        lay1.addWidget(self.compositor)
        lay1.addWidget(self.album)

        lay2 = QVBoxLayout()
        lay2.addLayout(lay1)
        
        self.table = QTableView()
        
        lay2.addWidget(self.table)

        self.modelo = QSqlQueryModel()
        self.table.setModel(self.modelo)
        
        self.query = QSqlQuery(db=dba)
        
        self.query.prepare(
            "SELECT nombre, compositor, Album.Title FROM Pista "
            "INNER JOIN Album ON Pista.AlbumId = Album.AlbumId WHERE "
            "Pista.nombre LIKE '%' || :Pista_nombre || '%' AND "
            "Pista.compositor LIKE '%' || :Pista_compositor || '%' AND "
            "Album.Title  LIKE '%' || :album_title || '%' "
            )
        
        self.actualizarQuery()
        
        self.setMinimumSize(QSize(900,600))
        self.setCentralWidget(self.widget)

    def actualizarQuery():
        Pista_nombre = self.pista.text()
        Pista_compositor = self.compositor.text()
        album_title = self.album.text()
        
        self.query.bindValue(":Pista_nombre",Pista_nombre)
        self.query.bindValue(":Pista_compositor",Pista_compositor)
        self.query.bindValue(":album_title",album_title)
        
        self.query.exec_()
        self.modelo.setQuery(self.query)


app = QApplication(sys.argv)
dba = QSqlDatabase("QSQLITE")
dba.setDatabaseName("album_pistas.db")
dba.open()
win = MainWindow()
win.show()
sys.exit(app.exec())