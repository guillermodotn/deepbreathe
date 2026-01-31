"""Material Design Icons mapping for the app."""

# Icon codes from Material Design Icons
# Full list: https://pictogrammers.com/library/mdi/
ICONS = {
    # Navigation
    "menu": "\U000F035C",
    "home": "\U000F02DC",
    "cog": "\U000F0493",
    "information": "\U000F02FD",
    "close": "\U000F0156",
    "arrow-left": "\U000F004D",
    # Training
    "lungs": "\U000F1084",
    "weather-windy": "\U000F059D",
    "timer": "\U000F13AB",
    "timer-outline": "\U000F051B",
    "play": "\U000F040A",
    "pause": "\U000F03E4",
    "stop": "\U000F04DB",
    # Actions
    "plus": "\U000F0415",
    "minus": "\U000F0374",
    "check": "\U000F012C",
    # Status
    "alert": "\U000F0026",
    "heart-pulse": "\U000F5F6C",
}


def icon(name: str) -> str:
    """Get the unicode character for an icon name."""
    return ICONS.get(name, "?")
