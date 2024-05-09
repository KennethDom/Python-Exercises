# -*- coding: utf-8 -*-
"""
Created on Mon May  3 17:58:12 2021

@author: Usuario
"""

from kivy.app import App
from kivy.uix.button import Button
class TestApp(App):
    def build(self):
        return Button(text="Hello Word")
    
TestApp().run()
 