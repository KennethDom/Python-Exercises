# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 11:45:24 2021

@author: Usuario
"""

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5.QtWidgets import QApplication,QMainWindow,QTableView, QVBoxLayout, QLineEdit, QHBoxLayout,QWidget
from PyQt5.QtCore import QSize, Qt


class Main(QMainWindow):
    def _init_(self):
        super()._init_()

        widget = QWidget()
        lay1 = QHBoxLayout()

        self.pista = QLineEdit()
        self.pista.setPlaceholderText("Escriba la pista a buscar")
        self.pista.textChanged.connect(self.actualizar)

        self.compositor = QLineEdit()
        self.compositor.setPlaceholderText("Escriba el compositor a buscar")
        self.compositor.textChanged.connect(self.actualizar)

        self.album = QLineEdit()
        self.album.setPlaceholderText("Escriba el album a buscar")
        self.album.textChanged.connect(self.actualizar)

        lay1.addWidget(self.pista)
        lay1.addWidget(self.compositor)
        lay1.addWidget(self.album)

        lay2 = QVBoxLayout()
        lay2.addLayout(lay1)

        self.tabla = QTableView()
        lay2.addWidget(self.tabla)
        widget.setLayout(lay2)

        self.modelo = QSqlQueryModel()
        self.tabla.setModel(self.modelo)

        self.query = QSqlQuery(db=dba)

        self.query.prepare("SELECT * FROM Pista "
                           "INNER JOIN Album ON Pista.AlbumId = Album.AlbumId WHERE "
                           "Pista.nombre LIKE '%' || :pista_nombre || '%' AND "
                           "Pista.compositor LIKE '%' || :pista_compositor || '%' AND "
                           "Album.nombre LIKE '%' || :album_nombre || '%' ")
        self.actualizar()
        
        self.setMinimumSize(QSize(900,600))
        self.setCentralWidget(widget)

    def actualizar(self):
        pista_nombre = self.pista.text()
        pista_compositor = self.compositor.text()
        album_nombre = self.album.text()
        
        self.query.bindValue(":pista_nombre", pista_nombre)
        self.query.bindValue(":pista_compositor", pista_compositor)
        self.query.bindValue(":album_nombre", album_nombre)

        self.query.exec_()
        self.modelo.setQuery(self.query)


app = QApplication(sys.argv)
dba = QSqlDatabase("QSQLITE")
dba.setDatabaseName("album_pistas.db")
dba.open()
win = Main()
win.show()
sys.exit(app.exec())