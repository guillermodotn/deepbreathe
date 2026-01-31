from kivy.app import App
from kivy.lang import Builder
from kivy.properties import NumericProperty
from kivy.uix.screenmanager import Screen

Builder.load_string("""
#:import StyledCard deepbreathe.widgets.styled_card.StyledCard
#:import StyledButton deepbreathe.widgets.styled_button.StyledButton

<SettingRow@BoxLayout>:
    orientation: "horizontal"
    size_hint_y: None
    height: dp(60)
    padding: dp(16), dp(8)
    spacing: dp(16)
    setting_label: ""
    setting_value: 60
    min_value: 15
    max_value: 300

    BoxLayout:
        orientation: "vertical"
        size_hint_x: 0.5

        Label:
            text: root.setting_label
            font_size: sp(15)
            color: 0.2, 0.2, 0.2, 1
            text_size: self.size
            halign: "left"
            valign: "middle"

    Label:
        text: f"{int(root.setting_value // 60)}:{int(root.setting_value % 60):02d}"
        font_size: sp(16)
        bold: True
        color: 0.3, 0.3, 0.3, 1
        size_hint_x: None
        width: dp(50)

    Slider:
        size_hint_x: 0.4
        min: root.min_value
        max: root.max_value
        step: 15
        value: root.setting_value
        on_value: root.setting_value = self.value


<SettingsScreen>:
    ScrollView:
        BoxLayout:
            orientation: "vertical"
            padding: dp(16)
            spacing: dp(16)
            size_hint_y: None
            height: self.minimum_height

            Label:
                text: "O2 Table Settings"
                font_size: sp(18)
                bold: True
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: None
                height: dp(32)
                text_size: self.size
                halign: "left"
                valign: "middle"

            StyledCard:
                orientation: "vertical"
                size_hint_y: None
                height: dp(200)
                padding: 0

                SettingRow:
                    id: o2_hold
                    setting_label: "Hold Time"
                    setting_value: root.o2_hold_time
                    min_value: 30
                    max_value: 300
                    on_setting_value: root.o2_hold_time = self.setting_value

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0.9, 0.9, 0.9, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                SettingRow:
                    id: o2_rest
                    setting_label: "Initial Rest"
                    setting_value: root.o2_initial_rest
                    min_value: 30
                    max_value: 300
                    on_setting_value: root.o2_initial_rest = self.setting_value

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0.9, 0.9, 0.9, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                SettingRow:
                    id: o2_decrement
                    setting_label: "Rest Decrement"
                    setting_value: root.o2_rest_decrement
                    min_value: 5
                    max_value: 30
                    on_setting_value: root.o2_rest_decrement = self.setting_value

            Label:
                text: "CO2 Table Settings"
                font_size: sp(18)
                bold: True
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: None
                height: dp(40)
                text_size: self.size
                halign: "left"
                valign: "middle"

            StyledCard:
                orientation: "vertical"
                size_hint_y: None
                height: dp(200)
                padding: 0

                SettingRow:
                    id: co2_hold
                    setting_label: "Initial Hold"
                    setting_value: root.co2_initial_hold
                    min_value: 30
                    max_value: 180
                    on_setting_value: root.co2_initial_hold = self.setting_value

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0.9, 0.9, 0.9, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                SettingRow:
                    id: co2_increment
                    setting_label: "Hold Increment"
                    setting_value: root.co2_hold_increment
                    min_value: 5
                    max_value: 30
                    on_setting_value: root.co2_hold_increment = self.setting_value

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas:
                        Color:
                            rgba: 0.9, 0.9, 0.9, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                SettingRow:
                    id: co2_rest
                    setting_label: "Rest Time"
                    setting_value: root.co2_rest_time
                    min_value: 60
                    max_value: 300
                    on_setting_value: root.co2_rest_time = self.setting_value

            Label:
                text: "General Settings"
                font_size: sp(18)
                bold: True
                color: 0.2, 0.2, 0.2, 1
                size_hint_y: None
                height: dp(40)
                text_size: self.size
                halign: "left"
                valign: "middle"

            StyledCard:
                orientation: "horizontal"
                size_hint_y: None
                height: dp(80)
                spacing: dp(16)

                BoxLayout:
                    orientation: "vertical"

                    Label:
                        text: "Number of Rounds"
                        font_size: sp(15)
                        color: 0.2, 0.2, 0.2, 1
                        text_size: self.size
                        halign: "left"
                        valign: "bottom"

                    Label:
                        text: "For both O2 and CO2 tables"
                        font_size: sp(13)
                        color: 0.5, 0.5, 0.5, 1
                        text_size: self.size
                        halign: "left"
                        valign: "top"

                BoxLayout:
                    size_hint_x: None
                    width: dp(120)
                    spacing: dp(8)

                    Button:
                        text: "−"
                        font_size: sp(24)
                        size_hint: None, None
                        size: dp(40), dp(40)
                        pos_hint: {"center_y": 0.5}
                        background_color: 0.9, 0.9, 0.9, 1
                        color: 0.2, 0.2, 0.2, 1
                        on_release: root.decrease_rounds()

                    Label:
                        text: str(root.total_rounds)
                        font_size: sp(20)
                        bold: True
                        color: 0.2, 0.2, 0.2, 1
                        size_hint_x: None
                        width: dp(40)

                    Button:
                        text: "+"
                        font_size: sp(24)
                        size_hint: None, None
                        size: dp(40), dp(40)
                        pos_hint: {"center_y": 0.5}
                        background_color: 0.9, 0.9, 0.9, 1
                        color: 0.2, 0.2, 0.2, 1
                        on_release: root.increase_rounds()

            StyledButton:
                text: "Apply Settings"
                size_hint_y: None
                height: dp(48)
                on_release: root.apply_settings()

            Widget:
                size_hint_y: None
                height: dp(16)
""")


class SettingsScreen(Screen):
    # O2 Table settings
    o2_hold_time = NumericProperty(120)  # 2 minutes
    o2_initial_rest = NumericProperty(120)  # 2 minutes
    o2_rest_decrement = NumericProperty(15)  # 15 seconds

    # CO2 Table settings
    co2_initial_hold = NumericProperty(60)  # 1 minute
    co2_hold_increment = NumericProperty(15)  # 15 seconds
    co2_rest_time = NumericProperty(120)  # 2 minutes

    # General settings
    total_rounds = NumericProperty(8)

    def increase_rounds(self):
        if self.total_rounds < 12:
            self.total_rounds += 1

    def decrease_rounds(self):
        if self.total_rounds > 4:
            self.total_rounds -= 1

    def apply_settings(self):
        """Apply settings to the training screens."""
        app = App.get_running_app()
        screen_manager = app.root.ids.screen_manager

        # Apply O2 settings
        o2_screen = screen_manager.get_screen("o2_screen")
        o2_screen.hold_time = int(self.o2_hold_time)
        o2_screen.initial_rest_time = int(self.o2_initial_rest)
        o2_screen.rest_decrement = int(self.o2_rest_decrement)
        o2_screen.total_rounds = self.total_rounds

        # Apply CO2 settings
        co2_screen = screen_manager.get_screen("co2_screen")
        co2_screen.initial_hold_time = int(self.co2_initial_hold)
        co2_screen.hold_increment = int(self.co2_hold_increment)
        co2_screen.rest_time = int(self.co2_rest_time)
        co2_screen.total_rounds = self.total_rounds

        # Navigate back to home
        app.change_screen("home", "DeepBreathe")
