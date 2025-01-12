from kivymd.uix.appbar import MDTopAppBar
from kivy.lang import Builder

from kivymd.uix.appbar import MDTopAppBarLeadingButtonContainer, MDActionTopAppBarButton

# Explicitly load the .kv string
Builder.load_string("""
<CustomAppBar>:
    type: "small"
    MDTopAppBarLeadingButtonContainer:

        MDActionTopAppBarButton:
            icon: "menu"
            on_release: app.root.ids.nav_drawer.set_state("toggle")
        
    MDTopAppBarTitle:
        text: "DeepBreathe"
    
""")


class CustomAppBar(MDTopAppBar):
    pass
