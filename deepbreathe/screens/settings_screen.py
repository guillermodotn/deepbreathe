from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

# Explicitly load the .kv string
Builder.load_string("""
<SettingsScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDLabel:
            text: "Settings Screen"
            halign: "center"
            text_color: "white"
""")


class SettingsScreen(MDScreen):
    pass
