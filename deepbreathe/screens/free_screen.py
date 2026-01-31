from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen

Builder.load_string("""
#:import ProgressCircle deepbreathe.widgets.progress_circle.ProgressCircle
#:import StyledButton deepbreathe.widgets.styled_button.StyledButton
#:import OutlinedButton deepbreathe.widgets.styled_button.OutlinedButton

<FreeScreen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(8)

        # Session info
        Label:
            text: f"Hold #{root.hold_count}" if root.hold_count > 0 else "Free Training"
            font_size: sp(16)
            color: 0.5, 0.5, 0.5, 1
            size_hint_y: None
            height: dp(28)

        # Phase indicator
        Label:
            text: root.phase_text
            font_size: sp(28)
            bold: True
            color: root.phase_color
            size_hint_y: None
            height: dp(44)

        RelativeLayout:
            size_hint_y: 1

            ProgressCircle:
                id: progress_circle
                size_hint: None, None
                size: min(self.parent.width, self.parent.height) * 0.7, min(self.parent.width, self.parent.height) * 0.7
                pos: (self.parent.width - self.width) / 2, (self.parent.height - self.height) / 2
                progress_color: root.phase_color

            Label:
                text: root.time_text
                font_size: sp(56)
                bold: True
                color: 0.1, 0.1, 0.1, 1
                size_hint: None, None
                size: dp(200), dp(80)
                pos: (self.parent.width - self.width) / 2, (self.parent.height - self.height) / 2

        # Best time display
        Label:
            text: root.best_time_text
            font_size: sp(16)
            bold: True
            color: 0.3, 0.3, 0.3, 1
            size_hint_y: None
            height: dp(24)

        # Instruction text
        Label:
            text: root.instruction_text
            font_size: sp(15)
            color: 0.5, 0.5, 0.5, 1
            size_hint_y: None
            height: dp(36)
            text_size: self.width, None
            halign: "center"

        # Control buttons
        BoxLayout:
            orientation: "horizontal"
            size_hint_y: None
            height: dp(56)
            spacing: dp(16)
            padding: dp(16), 0

            OutlinedButton:
                text: "Reset"
                size_hint_x: 0.5
                on_release: root.reset_session()

            StyledButton:
                text: root.button_text
                size_hint_x: 0.5
                on_release: root.toggle_hold()
""")  # noqa E501


class FreeScreen(Screen):
    """Free Training: Practice breath holds at your own pace with a timer."""

    time_text = StringProperty("00:00")
    phase_text = StringProperty("Ready")
    instruction_text = StringProperty("Tap Start when you're ready to hold")
    best_time_text = StringProperty("Best: --:--")
    button_text = StringProperty("Start Hold")
    phase_color = [0.4, 0.4, 0.8, 1]

    hold_count = NumericProperty(0)
    is_holding = BooleanProperty(False)
    elapsed_time = NumericProperty(0)
    best_time = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.timer_event = None
        self.phase = "ready"  # ready, hold
        self._update_phase_color()

    def on_enter(self):
        """Called when screen is entered."""
        self._reset_display()

    def on_leave(self):
        """Called when leaving the screen."""
        self._stop_timer()

    def _reset_display(self):
        """Reset display without clearing best time."""
        self.phase = "ready"
        self.is_holding = False
        self.elapsed_time = 0
        self.time_text = "00:00"
        self.phase_text = "Ready"
        self.instruction_text = "Tap Start when you're ready to hold"
        self.button_text = "Start Hold"
        self._update_phase_color()
        if hasattr(self, "ids") and "progress_circle" in self.ids:
            self.ids.progress_circle.set_progress(0, duration=0.3)

    def reset_session(self):
        """Full reset including hold count and best time."""
        self._stop_timer()
        self.hold_count = 0
        self.best_time = 0
        self.best_time_text = "Best: --:--"
        self._reset_display()

    def toggle_hold(self):
        """Start or stop a breath hold."""
        if self.is_holding:
            self._end_hold()
        else:
            self._start_hold()

    def _start_hold(self):
        """Begin a breath hold."""
        self.phase = "hold"
        self.is_holding = True
        self.elapsed_time = 0
        self.hold_count += 1
        self.phase_text = "Holding..."
        self.instruction_text = "Stay relaxed - tap Stop when you need to breathe"
        self.button_text = "Stop"
        self._update_phase_color()
        self.timer_event = Clock.schedule_interval(self._update_timer, 0.1)

    def _end_hold(self):
        """End the current breath hold."""
        self._stop_timer()
        self.phase = "ready"
        self.is_holding = False

        # Check for new best time
        if self.elapsed_time > self.best_time:
            self.best_time = self.elapsed_time
            self._update_best_time_display()
            self.phase_text = "New Best!"
            self.instruction_text = "Great job! Take recovery breaths"
        else:
            self.phase_text = "Done"
            self.instruction_text = "Good effort! Recover and try again"

        self.button_text = "Start Hold"
        self._update_phase_color()

        # Keep progress at 100% briefly to show completion
        if hasattr(self, "ids") and "progress_circle" in self.ids:
            self.ids.progress_circle.set_progress(100, duration=0.3)

    def _stop_timer(self):
        """Stop the timer if running."""
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None

    def _update_timer(self, dt):
        """Update the timer display."""
        self.elapsed_time += dt
        self._update_time_display()
        self._update_progress()
        self._update_phase_color()

    def _update_time_display(self):
        """Update the time display."""
        total_seconds = int(self.elapsed_time)
        mins, secs = divmod(total_seconds, 60)
        # Show tenths of a second for more precise timing
        tenths = int((self.elapsed_time - total_seconds) * 10)
        if mins > 0:
            self.time_text = f"{mins:02}:{secs:02}"
        else:
            self.time_text = f"{secs:02}.{tenths}"

    def _update_best_time_display(self):
        """Update the best time display."""
        total_seconds = int(self.best_time)
        mins, secs = divmod(total_seconds, 60)
        self.best_time_text = f"Best: {mins:02}:{secs:02}"

    def _update_progress(self):
        """Update progress circle based on elapsed time."""
        if not hasattr(self, "ids") or "progress_circle" not in self.ids:
            return

        # Progress based on a 3-minute target (180 seconds)
        target_time = 180
        progress = min(100, (self.elapsed_time / target_time) * 100)
        self.ids.progress_circle.set_progress(progress, duration=0.1)

    def _update_phase_color(self):
        """Update the color based on current phase."""
        if self.phase == "hold":
            # Change color based on elapsed time
            if self.elapsed_time < 30:
                self.phase_color = [0.2, 0.7, 0.4, 1]  # Green - easy
            elif self.elapsed_time < 60:
                self.phase_color = [0.9, 0.7, 0.2, 1]  # Yellow - moderate
            elif self.elapsed_time < 90:
                self.phase_color = [0.9, 0.5, 0.2, 1]  # Orange - challenging
            else:
                self.phase_color = [0.9, 0.3, 0.3, 1]  # Red - intense
        else:
            self.phase_color = [0.4, 0.4, 0.8, 1]  # Purple - ready
