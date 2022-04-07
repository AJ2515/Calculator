import numpy as np
import re
import numexpr as ne
from  kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.textinput import TextInput
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

class some(BoxLayout):
    edit_text = StringProperty("")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #print(root.entry.text)
    def pp(self,widget):
        print(widget.cursor)
    
    def textupdate(self,widget):
        widget.focus = True
    
    def my_eval(self,texts):
        try:
            return round(float(ne.evaluate(texts)),2)
        except:
            texts = "ERROR"
        
        
class KivyTryApp(App):
	pass

KivyTryApp().run()
