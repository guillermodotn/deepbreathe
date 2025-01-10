
from kivymd.uix.button import MDButton
from kivy.lang import Builder

# Explicitly load the .kv file
Builder.load_file('deepbreathe/widgets/custombutton.kv')

class CustomButton(MDButton):
    pass
