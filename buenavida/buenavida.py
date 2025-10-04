import reflex as rx
from buenavida.components.navbar import navbar
from buenavida.components.hero import hero
from buenavida.components.services import services
from buenavida.components.testimonials import testimonials
from buenavida.components.cta import cta
from buenavida.components.footer import footer
from buenavida.components.contact import contact_form
from buenavida.states.landing_state import LandingState


def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero(),
        services(),
        testimonials(),
        cta(),
        #contact_form(),
        footer(),
        class_name="font-['Montserrat'] bg-white",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="Buena Vida - Actividades Acuáticas")