from kivy.lang import Builder
from kivymd.uix.appbar import (
    MDActionTopAppBarButton,
    MDTopAppBar,
    MDTopAppBarLeadingButtonContainer,
)

# Explicitly load the .kv string
Builder.load_string("""
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
