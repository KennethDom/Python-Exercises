# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:17:22 2021

@author: Usuario
"""

from kivy.app import App
from kivy.uix import textinput, button, boxlayout


class Aplicacion(App):
    def build(self):
        boton = button.Button(text="Ok")
        texto = textinput.TextInput(text="Area para escribir")
        gestor = boxlayout.BoxLayout(orientation="vertical")
        
        gestor.add_widget(widget = boton)
        gestor.add_widget(widget = texto)
        
        return gestor
    
    
app = Aplicacion(title = "Ejemplo 2 de Kivy")
app.run()
        
