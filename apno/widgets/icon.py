from kivy.lang import Builder
from kivy.properties import ColorProperty, NumericProperty, StringProperty
from kivy.uix.label import Label

from apno.utils.icons import icon

Builder.load_string("""
<Icon>:
    font_name: "Icons"
    font_size: self.icon_size
    color: self.icon_color
    size_hint: None, None
    size: self.icon_size, self.icon_size
    text_size: self.size
    halign: "center"
    valign: "middle"
""")


class Icon(Label):
    """A widget that displays a Material Design Icon."""

    icon_name = StringProperty("")
    icon_size = NumericProperty(24)
    icon_color = ColorProperty([0.2, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(icon_name=self._update_icon)
        self._update_icon()

    def _update_icon(self, *args):
        self.text = icon(self.icon_name)
