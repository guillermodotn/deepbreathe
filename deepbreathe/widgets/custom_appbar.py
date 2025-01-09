
from kivymd.uix.toolbar import MDTopAppBar
from kivy.lang import Builder

# Explicitly load the .kv string
Builder.load_string("""
<CustomAppBar>:
    type: "top"
    title: "DeepBreathe"
    left_action_items: [["menu", lambda x:  app.root.ids.nav_drawer.set_state("toggle")]]
    right_action_items: [["git"]]
    
""")

class CustomAppBar(MDTopAppBar):
    pass
