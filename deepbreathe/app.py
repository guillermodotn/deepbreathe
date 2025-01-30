import kivy
from kivymd.app import MDApp

kivy.require("2.3.1")  # replace with your current kivy version !


class DeepBreathe(MDApp):
    def build(self):
        pass

    def change_screen(self, screen_name, title, color = (1, 0, 1, 1)):
        self.root.ids.appbar.md_bg_color = color
        # Change title of the appbar
        self.root.ids.appbar.ids.title.text = title
        # Switch to the screen passed as the argument
        self.root.ids.screen_manager.current = screen_name
        # Close the navigation drawer when a menu item is clicked
        self.root.ids.nav_drawer.set_state("close")
