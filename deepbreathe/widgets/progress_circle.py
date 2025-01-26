from kivy.animation import Animation
from kivy.app import App
from kivy.graphics import Color, Line
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class ProgressCircle(Widget):
    progress = NumericProperty(0)  # Progress percentage (0 to 100)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(progress=self.update_canvas)

    def update_canvas(self, *args):
        # Clear the canvas before redrawing
        self.canvas.clear()

        # Define circle properties
        with self.canvas:
            # Background circle
            Color(0.9, 0.9, 0.9, 1)  # RGBA
            Line(circle=(self.center_x, self.center_y, min(self.width, self.height) / 2 - 10), width=3)

            # Progress arc
            Color(0.1, 0.5, 1, 1)  # Material blue
            Line(circle=(self.center_x, self.center_y, min(self.width, self.height) / 2 - 10, 0, 360 * self.progress / 100), width=6, cap='round')

    def on_size(self, *args):
        # Redraw the canvas when the widget size changes
        self.update_canvas()


    def set_progress(self, value, duration=0.5):
        """Smoothly animate progress to the desired value."""
        Animation(progress=value, duration=duration, t='out_quad').start(self)