import reflex as rx
from buenavida.components.navbar import navbar
from buenavida.components.hero import hero
from buenavida.components.about_us import about_us
from buenavida.components.services import services
from buenavida.components.footer import footer
from buenavida.components.contact import contact
from buenavida.states.theme_state import ThemeState

def index() -> rx.Component:
    return rx.el.main(
        navbar(),
        hero(),
        about_us(),
        services(),
        contact(),
        footer(),
        class_name="font-['Montserrat']",
        background_color=ThemeState.white_color
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    stylesheets=["styles/styles.css", "styles/fonts.css"],
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap",
            rel="stylesheet",
        ),
        rx.el.link(
            rel="stylesheet",
            href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
        ),
    ],
)
app.add_page(index, title="Buena Vida")