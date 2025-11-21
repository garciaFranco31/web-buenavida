import reflex as rx
from buenavida.states.theme_state import ThemeState
from buenavida.states.landing_state import LandingState

def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Disfruta el verano al máximo en ",
                    rx.el.span("Buena Vida", class_name="uppercase font-['Mango'] tracking-normal", color=ThemeState.white_color),
                    class_name="text-4xl md:text-6xl font-extrabold  leading-tight tracking-tighter drop-shadow-lg",
                    color=ThemeState.white_color,
                    textShadow = "0 2px 4px rgba(0,0,0,0.5), 0 0 10px rgba(0,0,0,0.7), 0 0 20px rgba(0,0,0,0.5)"

                ),
                rx.el.p(
                    "Bienvenidxs a la playita de Villa Maipú!",
                    class_name="mt-6 text-lg md:text-xl text-white font-bold max-w-2xl mx-auto",
                    textShadow = "0 2px 4px rgba(0,0,0,0.5), 0 0 10px rgba(0,0,0,0.7), 0 0 20px rgba(0,0,0,0.5)"
                ),
                rx.el.div(
                    rx.el.button(
                        "Ver Actividades",
                        rx.icon("arrow-down", class_name="ml-2"),
                        class_name="flex items-center justify-center text-white px-8 py-4 rounded-xl font-bold hover:bg-teal-700 transition-all shadow-lg hover:shadow-xl transform hover:scale-105",
                        background_color=ThemeState.primary_color,
                        _hover={"background_color": ThemeState.header_bg},
                        cursor="pointer",   
                        on_click=rx.call_script(
                            "document.getElementById('servicios').scrollIntoView({ behavior: 'smooth' })"),
                        href="#servicios",
                    ),
                    type="button",
                    class_name="mt-10 flex justify-center",
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto px-6 py-20 md:py-32",
        ),
        class_name="relative 40em",
        background_image="url('images/buenaVida_mar.jpg')",
        background_size="cover",
        #top="50%",
        image_rendering = "-webkit-optimize-contrast"
    )