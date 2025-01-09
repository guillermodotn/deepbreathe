import kivy
kivy.require('2.3.1') # replace with your current kivy version !

from kivymd.app import MDApp

from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationdrawer import MDNavigationDrawerLabel

from deepbreathe.widgets.custom_button import CustomButton
from deepbreathe.screens.home_screen import HomeScreen

class DeepBreathe(MDApp):

    def build(self):
        pass

