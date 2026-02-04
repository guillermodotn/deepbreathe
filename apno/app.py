import os

import kivy
from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window

kivy.require("2.3.1")

# Set a reasonable default window size for desktop
Window.size = (400, 700)

# Register Material Design Icons font
FONTS_DIR = os.path.join(os.path.dirname(__file__), "assets", "fonts")
LabelBase.register(
    name="Icons",
    fn_regular=os.path.join(FONTS_DIR, "materialdesignicons-webfont.ttf"),
)


class Apno(App):
    def build(self):
        # Set window background color (cool white - Ocean Blue theme)
        Window.clearcolor = (0.97, 0.98, 1.0, 1)

    def change_screen(self, screen_name, title):
        """Navigate to a different screen."""
        # Update the app bar title
        self.root.ids.appbar.ids.title.text = title
        # Switch to the screen
        self.root.ids.screen_manager.current = screen_name
        # Close the navigation drawer if open
        if hasattr(self.root.ids, "nav_drawer"):
            self.root.ids.nav_drawer.close()


def main():
    """Entry point for the application."""
    Apno().run()
