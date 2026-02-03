from kivy.graphics import Color, RoundedRectangle
from kivy.lang import Builder
from kivy.properties import ColorProperty, ListProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout

Builder.load_string("""
<StyledCard>:
    padding: dp(16)
    spacing: dp(8)
""")


class StyledCard(BoxLayout):
    """A card widget with rounded corners and subtle shadow."""

    bg_color = ColorProperty([1, 1, 1, 1])
    radius = ListProperty([12])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(pos=self._update_canvas, size=self._update_canvas)
        self.bind(bg_color=self._update_canvas)
        self._update_canvas()

    def _update_canvas(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            # Shadow (slight offset)
            Color(0, 0, 0, 0.08)
            RoundedRectangle(
                pos=(self.x + 2, self.y - 2), size=self.size, radius=self.radius
            )
            # Card background
            Color(*self.bg_color)
            RoundedRectangle(pos=self.pos, size=self.size, radius=self.radius)


class ClickableCard(ButtonBehavior, StyledCard):
    """A card that can be clicked."""

    def on_press(self):
        self._original_color = self.bg_color[:]
        self.bg_color = [0.95, 0.95, 0.95, 1]

    def on_release(self):
        if hasattr(self, "_original_color"):
            self.bg_color = self._original_color
