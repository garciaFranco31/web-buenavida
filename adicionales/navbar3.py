import reflex as rx
from buenavida.states.landing_state import LandingState

def navbar() -> rx.Component:
    return rx.el.header(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("sun", class_name="h-8 w-8 text-sky-500"),
                        rx.el.span(
                            "Buena Vida", class_name="text-xl font-bold text-gray-800"
                        ),
                        style={"display": "flex", "alignItems": "center", "gap": "0.5rem"}
                    ),
                    href="/",
                ),
        rx.el.div(
            rx.el.nav(
                rx.el.button(
                    "Sobre Nosotrxs",
                    href="#about_us",
                    on_click=rx.call_script("document.getElementById('about_us').scrollIntoView({ behavior: 'smooth' })"),
                    type="button",
                    cursor="pointer"
                ),
                rx.el.button(
                    "Actividades",
                    href="#servicios",
                    on_click=rx.call_script("document.getElementById('servicios').scrollIntoView({ behavior: 'smooth' })"),
                    type="button",
                    cursor="pointer"
                ),
                rx.el.button(
                    "Nuestras Redes",
                    href="#redes_sociales",
                    on_click=rx.call_script("document.getElementById('redes_sociales').scrollIntoView({ behavior: 'smooth' })"),
                    type="button",
                    cursor="pointer"
                ),
                class_name="flex items-center gap-8",
            ),
            
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        rx.cond(LandingState.is_mobile_menu_open, "x", "menu"),
                        class_name="h-6 w-6 text-gray-700",
                        ),
                    on_click=LandingState.toggle_mobile_menu,
                    class_name="p-2 rounded-md hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-teal-500",
                    ),
                class_name="md:hidden",
                ),
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16",
            ),
            rx.cond(
                LandingState.is_mobile_menu_open,
                rx.el.div(
                    rx.el.button(
                        "Sobre Nosotrxs",
                        href="#about_us",
                        on_click=rx.call_script("document.getElementById('about_us').scrollIntoView({ behavior: 'smooth' })"),
                        type="button",
                        cursor="pointer"
                    ),
                    rx.el.button(
                        "Actividades",
                        href="#servicios",
                        on_click=rx.call_script("document.getElementById('servicios').scrollIntoView({ behavior: 'smooth' })"),
                        type="button",
                        cursor="pointer"
                    ),
                    # rx.el.button(
                    #     "Nuestros Servicios",
                    #     href="#servicios",
                    #     class_name="w-full text-center mt-4 px-4 py-2 bg-teal-600 text-white font-semibold rounded-md shadow-sm hover:bg-teal-700",
                    #     on_click=rx.call_script(
                    #     "document.getElementById('services').scrollIntoView({ behavior: 'smooth' })"
                    # ),
                    # type="button",
                    # ),
                    class_name="md:hidden flex flex-col items-center gap-4 pt-4 pb-4 border-t border-gray-200 text-black font-medium",
                ),
                None,
            ),
            class_name="w-full",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200 py-4 transition-all duration-300",
    )