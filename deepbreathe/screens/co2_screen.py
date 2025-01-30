from kivy.lang import Builder
from kivymd.uix.screen import MDScreen

# Explicitly load the .kv string
Builder.load_string("""
#:import MDBoxLayout kivymd.uix.boxlayout.MDBoxLayout
#:import MDLabel kivymd.uix.label.MDLabel

<CO2Screen>:
    MDBoxLayout:
        orientation: "vertical"

        MDLabel:
            text: "Co2 Screen"
            halign: "center"
            text_color: "white"
""")


class CO2Screen(MDScreen):
    pass
