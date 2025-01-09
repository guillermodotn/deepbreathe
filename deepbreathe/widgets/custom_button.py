
from kivymd.uix.button import MDFlatButton
from kivy.lang import Builder

# Explicitly load the .kv file
Builder.load_file('deepbreathe/widgets/custombutton.kv')

class CustomButton(MDFlatButton):
    pass
