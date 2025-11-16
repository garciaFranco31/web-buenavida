import reflex as rx
from buenavida.states.theme_state import ThemeState


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Disfruta el Verano al Máximo en ",
                    rx.el.span("Buena Vida", color=ThemeState.form_button_bg),
                    class_name="text-4xl md:text-6xl font-extrabold  leading-tight tracking-tighter drop-shadow-lg",
                    color=ThemeState.white_color,
                    textShadow = "0 2px 4px rgba(0,0,0,0.5), 0 0 10px rgba(0,0,0,0.7), 0 0 20px rgba(0,0,0,0.5)"

                ),
                rx.el.p(
                    "Bienvenidxs a la playita de Maipú!",
                    class_name="mt-6 text-lg md:text-xl text-white font-bold max-w-2xl mx-auto",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            "Ver Actividades",
                            rx.icon("arrow-down", class_name="ml-2"),
                            class_name="flex items-center justify-center text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-sky-600 transition-all shadow-lg hover:shadow-xl transform hover:scale-105",
                            background_color=ThemeState.icon_bg,
                            #class_name="flex items-center justify-center h-16 w-16 rounded-2xl bg-sky-100"
                        ),
                        href="#servicios",
                    ),
                    class_name="mt-10 flex justify-center",
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto px-6 py-20 md:py-32",
        ),
        class_name="relative",
        background_image="url('/beach.jpg')",
        background_size="cover",
        image_rendering = "-webkit-optimize-contrast"
    )