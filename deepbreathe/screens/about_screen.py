from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Explicitly load the .kv string
Builder.load_string("""
#:import MDBoxLayout kivymd.uix.boxlayout.MDBoxLayout
#:import MDLabel kivymd.uix.label.MDLabel

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
