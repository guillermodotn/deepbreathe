from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.lang import Builder

Builder.load_string("""
<CustomNavDrawer>:
    MDNavigationDrawerMenu:
        MDNavigationDrawerItem:
            on_release: app.change_screen("home", "Home")
            MDNavigationDrawerItemLeadingIcon:
                icon: "home"

            MDNavigationDrawerItemText:
                text: "Home"

        MDNavigationDrawerDivider:
        MDNavigationDrawerItem:
            on_release: app.change_screen("o2_screen", "O2 Tables")
            MDNavigationDrawerItemText:
                text: "O2"

            MDNavigationDrawerItemTrailingText:
                text: "streak 24"
        
        MDNavigationDrawerItem:
            on_release: app.change_screen("co2_screen", "CO2 Tables")
            MDNavigationDrawerItemText:
                text: "CO2"

            MDNavigationDrawerItemTrailingText:
                text: "streak 13"
        
        MDNavigationDrawerDivider:
        MDNavigationDrawerItem:
            on_release: app.change_screen("settings_screen", "Settings")
            MDNavigationDrawerItemLeadingIcon:
                icon: "cog"

            MDNavigationDrawerItemText:
                text: "Settings"
            
        MDNavigationDrawerItem:
            on_release: app.change_screen("about_screen", "About")
            MDNavigationDrawerItemLeadingIcon:
                icon: "information"

            MDNavigationDrawerItemText:
                text: "About"

            MDNavigationDrawerItemTrailingText:
                text: "1.0.0"
""")

class CustomNavDrawer(MDNavigationDrawer):
    pass
    