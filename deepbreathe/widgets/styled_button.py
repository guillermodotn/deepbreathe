from kivy.graphics import Color, Line, RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ColorProperty, NumericProperty, StringProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

from deepbreathe.utils.icons import icon

Builder.load_string("""
<StyledButton>:
    size_hint_y: None
    height: dp(48)
    font_size: sp(16)
    bold: True
    color: root.text_color

<OutlinedButton>:
    size_hint_y: None
    height: dp(48)
    font_size: sp(16)
    bold: True
    color: root.border_color

<IconButton>:
    font_name: "Icons"
    font_size: root.icon_size
    color: root.icon_color
    size_hint: None, None
    size: dp(48), dp(48)
""")


class StyledButton(ButtonBehavior, Label):
    """A styled filled button."""

    bg_color = ColorProperty([0.2, 0.5, 0.9, 1])
    text_color = ColorProperty([1, 1, 1, 1])
    radius = [8]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_canvas, size=self._update_canvas)
        self.bind(bg_color=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)

    def on_press(self):
        # Darken on press
        self._original_color = self.bg_color[:]
        self.bg_color = [c * 0.8 for c in self.bg_color[:3]] + [1]

    def on_release(self):
        if hasattr(self, "_original_color"):
            self.bg_color = self._original_color


class OutlinedButton(ButtonBehavior, Label):
    """A styled outlined button."""

    border_color = ColorProperty([0.2, 0.5, 0.9, 1])
    bg_color = ColorProperty([1, 1, 1, 1])
    radius = [8]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_canvas, size=self._update_canvas)
        self.bind(border_color=self._update_canvas, bg_color=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Background
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)
            # Border
            Color(*self.border_color)
            Line(
                rounded_rectangle=(
                    self.x,
                    self.y,
                    self.width,
                    self.height,
                    self.radius[0],
                ),
                width=1.2,
            )

    def on_press(self):
        self._original_bg = self.bg_color[:]
        self.bg_color = [0.95, 0.95, 0.95, 1]

    def on_release(self):
        if hasattr(self, "_original_bg"):
            self.bg_color = self._original_bg


class IconButton(ButtonBehavior, Label):
    """A button that displays a Material Design Icon."""

    icon_name = StringProperty("home")
    icon_size = NumericProperty(24)
    icon_color = ColorProperty([0.3, 0.3, 0.3, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(icon_name=self._update_icon)
        self._update_icon()

    def _update_icon(self, *args):
        self.text = icon(self.icon_name)

    def on_press(self):
        self._original_color = self.icon_color[:]
        self.icon_color = [c * 0.7 for c in self.icon_color[:3]] + [1]
        self.color = self.icon_color

    def on_release(self):
        if hasattr(self, "_original_color"):
            self.icon_color = self._original_color
            self.color = self.icon_color
