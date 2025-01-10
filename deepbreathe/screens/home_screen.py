from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


from kivy.lang import Builder

# Explicitly load the .kv file
Builder.load_file('deepbreathe/screens/homescreen.kv')

class HomeScreen(MDScreen):
    pass