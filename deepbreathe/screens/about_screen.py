from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from kivy.lang import Builder

# Explicitly load the .kv string
Builder.load_string("""
<AboutScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDLabel:
            text: "About Screen"
            halign: "center"
            text_color: "white"
""")


class AboutScreen(MDScreen):
    pass