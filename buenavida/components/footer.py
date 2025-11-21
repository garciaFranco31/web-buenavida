import reflex as rx
from buenavida.states.theme_state import ThemeState

def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                    "© 2024 Buena Vida. Todos los derechos reservados.",
                    class_name="text-center text-gray-500 font-2xs",
                ),
            class_name="py-8",
            background_color=ThemeState.white_color,
        ),
        background_color=ThemeState.white_color,
    )