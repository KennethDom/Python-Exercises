# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:23:55 2021

@author: Usuario
"""

from kivy.app import App
from kivy.uix import textinput, button, boxlayout


class Aplicacion(App):
    contador = 0
    def boton_click(self):
        Aplicacion.contador +=1
        print("Boton presionado", Aplicacion.contador, "veces")
        
        
    def build(self):
        boton = button.Button(text="Ok")
        texto = textinput.TextInput(text="Area para escribir")
        gestor = boxlayout.BoxLayout(orientation="vertical")
        
        boton.bind(on_press = Aplicacion.boton_click)
        
        gestor.add_widget(widget=boton)
        gestor.add_widget(widget=texto)
        
        return gestor
    
    
app = Aplicacion(title = "Ejemplo 2 de Kivy")
app.run()
        


