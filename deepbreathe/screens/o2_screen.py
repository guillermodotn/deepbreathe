from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivymd.uix.screen import MDScreen

from deepbreathe.widgets.progress_circle import ProgressCircle  # noqa: F401

# Explicitly load the .kv string
Builder.load_string("""
<O2Screen>:
    MDBoxLayout:
        id: root_layout
        orientation: "vertical"
        md_bg_color: "white"

        MDFloatLayout:
            ProgressCircle:
                id: progress_circle
                size_hint: None, None
                size: 400, 400
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

            # Timer
            MDLabel:
                id: timer_label
                text: root.time_text  # Binds to the time_text property
                size_hint: None, None
                width: 500
                height: 100
                font_size: 40  # Increase font size if needed
                halign: "center"
                valign: "middle"
                color: 0, 0, 0, 1
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

        MDButton:
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            on_release: root.update_progress()

            MDButtonText:
                text: "Update Progress"
""")


class O2Screen(MDScreen):
    time_text = StringProperty("00:00")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Start a timer to update every second
        Clock.schedule_interval(self.update_timer, 1)
        self.total_time = 60  # Set your total time in seconds (for example, 60 seconds)
        self.time_left = self.total_time

    def update_progress(self):
        new_progress = (100 / self.total_time) * (self.total_time - self.time_left)
        self.ids.progress_circle.set_progress(new_progress)

    def update_timer(self, dt):
        """Updates the timer and the time_left."""
        if self.time_left > 0:
            self.time_left -= 1
            self.update_progress()
            mins, secs = divmod(self.time_left, 60)
            self.time_text = f"{mins:02}:{secs:02}"  # Format as MM:SS
        else:
            self.time_text = "00:00"  # Timer reaches zero
            Clock.unschedule(self.update_timer)  # Stop the timer

        # Change the color dynamically when the timer reaches a certain value
        if self.time_left <= 55:
            self.ids.timer_label.color = (1, 0, 0, 1)
        if self.time_left == 0:  # When the timer reaches zero, change color to green
            self.ids.timer_label.color = (0, 1, 0, 1)  # Green
