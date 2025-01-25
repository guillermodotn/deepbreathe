from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# Explicitly load the .kv file
Builder.load_file("deepbreathe/screens/homescreen.kv")


class HomeScreen(MDScreen):
    pass
