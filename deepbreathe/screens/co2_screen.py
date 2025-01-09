from kivymd.uix.screen import MDScreen

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDTextButton

from kivy.lang import Builder

# Explicitly load the .kv string
Builder.load_string("""
<CO2Screen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTextButton:
            pos_hint: {"center_x": .5, "center_y": .5}
            on_release:  app.root.ids.nav_drawer.set_state("toggle")
            text: "Open Drawer"

        MDLabel:
            text: "Co2 Screen"
            halign: "center"
""")

class CO2Screen(MDScreen):
    pass