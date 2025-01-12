import kivy
kivy.require('2.3.1') # replace with your current kivy version !

from kivymd.app import MDApp

from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.uix.navigationdrawer import MDNavigationDrawerItem
from kivymd.uix.navigationdrawer import MDNavigationDrawerDivider
from kivymd.uix.navigationdrawer import MDNavigationDrawerMenu

from deepbreathe.widgets.custom_appbar import CustomAppBar

from deepbreathe.widgets.custom_button import CustomButton
from deepbreathe.screens.home_screen import HomeScreen
from deepbreathe.screens.co2_screen import CO2Screen
from deepbreathe.screens.o2_screen import O2Screen
from deepbreathe.screens.settings_screen import SettingsScreen
from deepbreathe.screens.about_screen import AboutScreen

class DeepBreathe(MDApp):

    def build(self):
        pass
    
    def change_screen(self, screen_name):
        # Switch to the screen passed as the argument
        self.root.ids.screen_manager.current = screen_name
        # Close the navigation drawer when a menu item is clicked
        self.root.ids.nav_drawer.set_state("close")

