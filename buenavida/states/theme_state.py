import reflex as rx

class ThemeState(rx.State):
    """State for managing the theme of the application."""
    primary_color: str = "#e36849"
    header_bg: str = "#f79621"
    form_button_bg: str = "#ffbe2f"
    primary_complementary: str = "#33b3b2"
    icon_bg: str = "#8ad0ce"
    icon_color: str = "#137c78"

