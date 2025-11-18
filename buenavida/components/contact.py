import reflex as rx
from buenavida.states.theme_state import ThemeState


def contact() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    "Seguinos en nuestras redes sociales y enterate de todas las novedades",
                    class_name="text-2xl md:text-3xl font-bold text-gray-900 text-center"
                ),

            ),
            rx.el.div(
                rx.el.a(
                    rx.el.i(
                        class_name="fa-brands fa-instagram text-6xl transition-colors",
                        color= {ThemeState.icon_color},
                        _hover= {"color": ThemeState.form_button_bg}
                    ),
                    href="https://www.instagram.com/buenavida.clubsocial?igsh=Z2dueGE0ZmVwemV6",
                ),
                rx.el.a(
                    rx.el.i(
                        class_name=f"fa-brands fa-square-facebook text-6xl text-teal-500 hover:ThemeState.primary_color transition-colors",
                        color= {ThemeState.icon_color},
                        _hover= {"color": ThemeState.form_button_bg}
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.el.i(
                        class_name=f"fa-brands fa-whatsapp text-6xl text-gray-500 transition-colors",
                        color= {ThemeState.icon_color},
                        _hover= {"color": ThemeState.form_button_bg},
                    ),
                    href="#",
                ),
                class_name="flex items-center space-x-20"
            ),
            class_name="flex flex-col items-center gap-12 p-8 mx-0 md:p-25  shadow-lg flex justify-center py-16 md:py-24 px-4 bg-gray-50/70",
        ),
        id="redes_sociales"
    )