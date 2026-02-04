from kivy.factory import Factory
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.properties import ColorProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

from apno.utils.icons import icon


class MenuButton(ButtonBehavior, Label):
    """Menu button for the app bar."""

    icon_color = ColorProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = icon("menu")
        self.font_name = "Icons"
        self.font_size = "24sp"
        self.size_hint = (None, None)
        self.size = (48, 48)
        self.bind(icon_color=self._update_color)
        self._update_color()

    def _update_color(self, *args):
        self.color = self.icon_color


# Register for use in KV
Factory.register("MenuButton", cls=MenuButton)

Builder.load_string("""
<AppBar>:
    size_hint_y: None
    height: dp(56)
    padding: dp(8), 0

    MenuButton:
        icon_color: root.text_color
        on_release: app.root.ids.nav_drawer.toggle()

    Label:
        id: title
        text: root.title
        font_size: sp(20)
        bold: True
        color: root.text_color
        text_size: self.size
        halign: "left"
        valign: "center"
        padding: dp(8), 0
""")


class AppBar(BoxLayout):
    """A top app bar with menu button and title."""

    title = StringProperty("Apno")
    bg_color = ColorProperty([0.15, 0.40, 0.65, 1])  # Deep Ocean Blue
    text_color = ColorProperty([1, 1, 1, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_canvas, size=self._update_canvas)
        self.bind(bg_color=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            Rectangle(pos=self.pos, size=self.size)
