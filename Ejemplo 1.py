# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:11:45 2021

@author: Usuario
"""

from kivy.app import App
from kivy.uix import textinput


class Aplicacion(App):
    def build(self):
        return textinput.TextInput(text="Hola mundo")
    
    
app = Aplicacion()
app.run()
        
