# Kenneth Gerardo Aguirre Dominguez 19410251
# Oscar Giovanni FIgueroa Talamantes 19410262

import sys
import random
import time
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QObject, QRunnable, QThreadPool, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox


class WorkerSignals(QObject):
    progress = pyqtSignal(int)


class WorkerLiebre(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals= WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        total = 100
        for i in range(total):
            variable = random.randint(1, 5)
            if variable == 1:
                progress = int((100 *float(i+1)/total)+5)
            if variable == 2:
                progress = int((100 *float(i+1)/total)+2)
            if variable == 3:
                progress = int((100 *float(i+1)/total)-1)
            if variable == 4:
                progress = int((100 *float(i+1)/total)-4)
            if variable == 5:
                progress = int((100 *float(i+1)/total)-7)
            self.signals.progress.emit(progress)
            #Imprimimos cuanto esta avanzando la liebre
            print("la liebre esta avanzando",progress)
            time.sleep(1)


class WorkerTortuga(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = WorkerSignals()
        
    @pyqtSlot()
    def run(self):
        total = 100
        for i in range(total):
            #Creamos numeros aleatorios del 1 al 5 
            variable = random.randint(1, 5)
            if variable == 1:
                progress = int((100 *float(i+1)/total)+2) 
            if variable == 2:
                progress = int((100 *float(i+1)/total)+1)
            if variable == 3:
                progress = int(100 *float(i+1)/total)
            if variable == 4:
                progress = int((100 *float(i+1)/total)-2)
            if variable == 5:
                progress = int((100 *float(i+1)/total)-3)
            self.signals.progress.emit(progress)
            #Imprimimos cuanto esta avanzando la tortuga
            print("la tortuga esta avanzando",progress)
            time.sleep(1)
            

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Unimos la ventana a la aplicacion
        self.resize(1350, 600)
        self.prin = uic.loadUi("PantallaPrincipal.ui", self)
        
        # Conectamos el boton con el metodo insertar
        self.btnStart.clicked.connect(self.iniciarJuego)
        
    
    def iniciarJuego(self):
        self.prin.close()
        self.inicia = Juego()
        self.inicia.show()
        

class Juego(QWidget):
    def __init__(self):
        super().__init__()
        # Unimos la ventana donde sucedera todo a la aplicacion
        self.juegoCarrera = uic.loadUi("Juego.ui", self)
        
        # Iniciamos el reloj para la aplicacion 
        self.counter = 0

        self.threadpool = QThreadPool()
        self.prueba.clicked.connect(self.ejecutar)
        self.prueba.clicked.connect(self.timer)
        self.timer = QTimer()
        
    #Metodo del timer    
    def timer(self):
        
        # Con un lapzo de un segundo
        self.timer.setInterval(1000)
        # Creamos un hilo para el reloj
        self.timer.timeout.connect(self.recorrerTimer)
        self.timer.start()
        
    def recorrerTimer(self):
        self.counter += 1
        self.Reloj.setText("Tiempo transcurrido:\n %d" %self.counter)
        
    def ejecutar(self):
        worke = WorkerLiebre()
        worke.signals.progress.connect(self.actualizarProgresoLiebre)
        worke2 = WorkerTortuga()
        worke2.signals.progress.connect(self.actualizarProgresotortuga)
        self.threadpool.start(worke)
        self.threadpool.start(worke2)
    
    def actualizarProgresotortuga(self, progress):
         self.bpTortuga.setValue(progress)
         if progress >= 100:
            self.bpTortuga.setValue(100)
            self.timer.stop()
            self.Reloj.setText("Tiempo finalizado en:\n%d" %self.counter+"\nGano la tortuga")
            print("Tiempo finalizado en:\n%d" %self.counter+"\nGano la tortuga")
            self.juegoCarrera.close()
            self.ganotortuga = uic.loadUi("ganadorTortuga.ui")
            self.ganotortuga.show()
            
        
    def actualizarProgresoLiebre(self, progress):
        self.bpLiebre.setValue(progress)
        if progress >= 100:
            self.bpLiebre.setValue(100)
            self.timer.stop()
            self.Reloj.setText("Tiempo finalizado en:\n%d" %self.counter+"\nGano la liebre")
            print("Tiempo finalizado en:\n%d" %self.counter+"\nGano la liebre")
            self.juegoCarrera.close()
            self.ganoliebre = uic.loadUi("ganadorLiebre.ui")
            self.ganoliebre.show()
            

app = QApplication(sys.argv)
juego = MainWindow()
juego.show()
sys.exit(app.exec())