from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, NumericProperty, StringProperty
from kivy.uix.screenmanager import Screen

Builder.load_string("""
#:import ProgressCircle deepbreathe.widgets.progress_circle.ProgressCircle
#:import StyledButton deepbreathe.widgets.styled_button.StyledButton
#:import OutlinedButton deepbreathe.widgets.styled_button.OutlinedButton

<O2Screen>:
    BoxLayout:
        orientation: "vertical"
        padding: dp(16)
        spacing: dp(8)

        # Round indicator
        Label:
            text: f"Round {root.current_round} of {root.total_rounds}"
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

        FloatLayout:
            size_hint_y: 1

            ProgressCircle:
                id: progress_circle
                size_hint: None, None
                size: self.parent.width * 0.7, self.parent.width * 0.7
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                progress_color: root.phase_color

            # Timer display
            Label:
                text: root.time_text
                font_size: sp(56)
                bold: True
                color: 0.1, 0.1, 0.1, 1
                size_hint: None, None
                size: dp(200), dp(80)
                pos_hint: {"center_x": 0.5, "center_y": 0.5}

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
                text: "Stop"
                size_hint_x: 0.5
                on_release: root.stop_training()

            StyledButton:
                text: "Pause" if root.is_running else "Start"
                size_hint_x: 0.5
                on_release: root.toggle_pause()
""")


class O2Screen(Screen):
    """O2 Table Training: Fixed hold time with decreasing rest periods."""

    time_text = StringProperty("00:00")
    phase_text = StringProperty("Ready")
    instruction_text = StringProperty("Press Start to begin training")
    phase_color = [0.2, 0.7, 0.4, 1]

    current_round = NumericProperty(1)
    total_rounds = NumericProperty(8)
    is_running = BooleanProperty(False)

    # Training parameters (in seconds)
    hold_time = NumericProperty(120)  # 2 minutes hold (fixed for O2)
    initial_rest_time = NumericProperty(120)  # Starting rest time
    rest_decrement = NumericProperty(15)  # Decrease rest by 15 sec each round

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time_left = 0
        self.current_phase_duration = 0
        self.phase = "ready"  # ready, breathe, hold, rest, complete
        self.timer_event = None
        self._update_phase_color()

    def on_enter(self):
        """Called when screen is entered."""
        self.reset_training()

    def on_leave(self):
        """Called when leaving the screen."""
        self.stop_training()

    def reset_training(self):
        """Reset training to initial state."""
        self.current_round = 1
        self.phase = "ready"
        self.is_running = False
        self.time_left = 0
        self.time_text = "00:00"
        self.phase_text = "Ready"
        self.instruction_text = "Press Start to begin O2 table training"
        self._update_phase_color()
        if hasattr(self, "ids") and "progress_circle" in self.ids:
            self.ids.progress_circle.set_progress(0, duration=0.3)

    def toggle_pause(self):
        """Start or pause the training."""
        if self.phase == "complete":
            self.reset_training()
            return

        if self.is_running:
            self.pause_training()
        else:
            self.start_training()

    def start_training(self):
        """Start or resume training."""
        self.is_running = True
        if self.phase == "ready":
            self._start_breathe_phase()
        if self.timer_event is None:
            self.timer_event = Clock.schedule_interval(self._update_timer, 1)

    def pause_training(self):
        """Pause the training."""
        self.is_running = False
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None

    def stop_training(self):
        """Stop and reset training."""
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None
        self.reset_training()

    def _start_breathe_phase(self):
        """Start the breathe-up phase (15 seconds to prepare)."""
        self.phase = "breathe"
        self.time_left = 15
        self.current_phase_duration = 15
        self.phase_text = "Breathe"
        self.instruction_text = "Take deep, relaxed breaths to prepare"
        self._update_phase_color()
        self._update_display()

    def _start_hold_phase(self):
        """Start the breath-hold phase."""
        self.phase = "hold"
        self.time_left = self.hold_time
        self.current_phase_duration = self.hold_time
        self.phase_text = "Hold"
        self.instruction_text = "Hold your breath - stay relaxed"
        self._update_phase_color()
        self._update_display()

    def _start_rest_phase(self):
        """Start the rest/recovery phase."""
        self.phase = "rest"
        # Calculate rest time for current round (decreases each round)
        decrement = (self.current_round - 1) * self.rest_decrement
        rest_time = self.initial_rest_time - decrement
        rest_time = max(rest_time, 15)  # Minimum 15 seconds rest
        self.time_left = rest_time
        self.current_phase_duration = rest_time
        self.phase_text = "Recover"
        self.instruction_text = "Breathe and recover for next round"
        self._update_phase_color()
        self._update_display()

    def _complete_training(self):
        """Training session complete."""
        self.phase = "complete"
        self.is_running = False
        self.phase_text = "Complete!"
        self.instruction_text = "Great job! Training session finished."
        self.time_text = "--:--"
        self._update_phase_color()
        if self.timer_event:
            Clock.unschedule(self.timer_event)
            self.timer_event = None
        if hasattr(self, "ids") and "progress_circle" in self.ids:
            self.ids.progress_circle.set_progress(100, duration=0.5)

    def _update_timer(self, dt):
        """Update the timer each second."""
        if not self.is_running:
            return

        if self.time_left > 0:
            self.time_left -= 1
            self._update_display()
        else:
            self._next_phase()

    def _next_phase(self):
        """Transition to the next phase."""
        if self.phase == "breathe":
            self._start_hold_phase()
        elif self.phase == "hold":
            if self.current_round >= self.total_rounds:
                self._complete_training()
            else:
                self._start_rest_phase()
        elif self.phase == "rest":
            self.current_round += 1
            self._start_breathe_phase()

    def _update_display(self):
        """Update the timer display and progress."""
        mins, secs = divmod(self.time_left, 60)
        self.time_text = f"{mins:02}:{secs:02}"

        # Update progress circle
        if self.current_phase_duration > 0 and hasattr(self, "ids"):
            progress = (
                (self.current_phase_duration - self.time_left)
                / self.current_phase_duration
                * 100
            )
            if "progress_circle" in self.ids:
                self.ids.progress_circle.set_progress(progress, duration=0.3)

    def _update_phase_color(self):
        """Update the color based on current phase."""
        colors = {
            "ready": [0.5, 0.5, 0.5, 1],
            "breathe": [0.2, 0.6, 0.9, 1],  # Blue
            "hold": [0.9, 0.3, 0.3, 1],  # Red
            "rest": [0.2, 0.7, 0.4, 1],  # Green
            "complete": [0.9, 0.7, 0.2, 1],  # Gold
        }
        self.phase_color = colors.get(self.phase, [0.5, 0.5, 0.5, 1])
