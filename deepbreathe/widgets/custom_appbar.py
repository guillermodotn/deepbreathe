from kivy.lang import Builder
from kivymd.uix.appbar import MDTopAppBar

# Explicitly load the .kv string
Builder.load_string("""
#:import MDActionTopAppBarButton kivymd.uix.topappbar.MDActionTopAppBarButton
#:import MDTopAppBarLeadingButtonContainer kivymd.uix.topappbar.MDTopAppBarLeadingButtonContainer


<CustomAppBar>:
    type: "small"
    MDTopAppBarLeadingButtonContainer:

        MDActionTopAppBarButton:
            icon: "menu"
            on_release: app.root.ids.nav_drawer.set_state("toggle")

    MDTopAppBarTitle:
        id: title
        text: "DeepBreathe"

""")


class CustomAppBar(MDTopAppBar):
    pass
