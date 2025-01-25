from kivy.lang import Builder
from kivymd.uix.button import MDButton

# Explicitly load the .kv file
Builder.load_file("deepbreathe/widgets/custombutton.kv")


class CustomButton(MDButton):
    pass
