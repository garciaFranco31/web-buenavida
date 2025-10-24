import reflex as rx
from buenavida.states.landing_state import LandingState


def nav_link(text: str, href: str) -> rx.Component:
    return rx.el.a(
        text,
        href=href,
        class_name="font-medium text-gray-600 hover:text-teal-600 transition-colors duration-300",
    )


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.nav(
            rx.el.div(
                rx.el.a(
                    rx.el.div(
                        rx.icon("hexagon", class_name="h-8 w-8 text-teal-600"),
                        rx.el.span(
                            "Materia", class_name="text-xl font-bold text-gray-800"
                        ),
                        class_name="flex items-center gap-2",
                    ),
                    href="/",
                ),
                rx.el.div(
                    nav_link("Servicios", "#servicios"),
                    nav_link("Testimonios", "#testimonios"),
                    nav_link("Contacto", "#contacto"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.div(
                    rx.el.a(
                        "Inscribite",
                        href="#contact",
                        class_name="px-4 py-2 bg-teal-600 text-white font-semibold rounded-md shadow-sm hover:bg-teal-700 focus:outline-none focus:ring-2 focus:ring-teal-500 focus:ring-offset-2 transition-all duration-300 transform hover:scale-105",
                    ),
                    class_name="hidden md:block",
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
                class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center",
            ),
            rx.cond(
                LandingState.is_mobile_menu_open,
                rx.el.div(
                    nav_link("Features", "#features"),
                    nav_link("About", "#about"),
                    nav_link("Testimonials", "#testimonials"),
                    rx.el.a(
                        "Contact Us",
                        href="#contact",
                        class_name="w-full text-center mt-4 px-4 py-2 bg-teal-600 text-white font-semibold rounded-md shadow-sm hover:bg-teal-700",
                    ),
                    class_name="md:hidden flex flex-col items-center gap-4 pt-4 pb-4 border-t border-gray-200",
                ),
                None,
            ),
            class_name="w-full",
        ),
        class_name="sticky top-0 z-50 w-full bg-white/80 backdrop-blur-md border-b border-gray-200 py-4 transition-all duration-300",
    )