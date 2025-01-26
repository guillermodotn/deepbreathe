from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen

from deepbreathe.widgets.progress_circle import ProgressCircle

# Explicitly load the .kv string
# Builder.load_string("""
# <O2Screen>:
#     MDBoxLayout:
#         orientation: "vertical"
# """)


class O2Screen(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        root_layout = MDBoxLayout(orientation='vertical')

        self.progress_circle = ProgressCircle()
        self.progress_circle.size_hint = (None, None)
        self.progress_circle.size = (400, 400)
        self.progress_circle.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        button = MDButton(MDButtonText(text="Update Progress"))
        button.bind(on_release=self.update_progress)
        button.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        root_layout.add_widget(self.progress_circle)
        root_layout.add_widget(button)
        self.add_widget(root_layout)
        # return root

    def update_progress(self, *args):
        from random import randint
        # Randomly set a new progress value
        new_progress = randint(10, 100)
        self.progress_circle.set_progress(new_progress)
