import reflex as rx
from buenavida.states.landing_state import LandingState

def nav_link(text: str, href:str) -> rx.Component:
    return rx.el.a(
        text,
        href=href
    )

def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.a(
            rx.el.div(
            rx.icon("sun", class_name="text-sky-500", size=32),
            rx.el.h1("Buena Vida", class_name="text-2xl font-bold text-gray-800"),
            class_name="flex items-center gap-2",
            ),
            href="/",
            class_name="flex items-center gap-2",
        ),
        rx.el.div(
            nav_link("Servicios", "#servicios"),
            nav_link("Testimonios", "#testimonios"),
            #nav_link("Contacto", "#contacto"),
            class_name="hidden md:flex items-center gap-8"
        )
           

    )