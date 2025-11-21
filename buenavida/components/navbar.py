import reflex as rx
from buenavida.states.navbar_state import NavbarState
from buenavida.states.theme_state import ThemeState


def navbar_link(name:str, dir:str) -> rx.Component:
    """A navigation link component."""
    return rx.el.a(
        name,
        href=dir,
        class_name="font-semibold transition-all transform hover:scale-110",
        color=ThemeState.letter,
        _hover= {"color": ThemeState.icon_bg},
        cursor="pointer",
        on_click=rx.scroll_to(dir),
        type="button",
    )


def mobile_menu() -> rx.Component:
    """The mobile menu component, displayed when the hamburger icon is clicked."""
    return rx.el.div(
        rx.el.div(
            rx.foreach(
                NavbarState.nav_links,
                lambda link: rx.el.a(
                    link["name"],
                    href=link["href"],
                    class_name="font-semibold block py-2 px-4 text-sm transition-all transform hover:scale-100",
                    _hover= {"background_color": ThemeState.icon_bg},
                    color=ThemeState.letter,
                    on_click=NavbarState.toggle_menu,
                ),
            ),
            class_name="py-1",
        ),
        class_name=rx.cond(
            NavbarState.show_menu,
            "absolute top-16 right-4 mt-2 w-48 bg-white rounded-md shadow-lg z-20",
            "hidden",
        ),
    )


def navbar() -> rx.Component:
    """The main navigation bar component."""
    return rx.el.header(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.avatar(
                        src="/images/logo_celesteOscuro.jpg",
                        width="3.25em",
                        height="auto",
                        ),
                    rx.el.div(
                        rx.el.span("BUENA VIDA",class_name=f"font-['Mango'] pt-2 leading-none text-2xl font-bold",
                            color=ThemeState.icon_color,
                        ),
                        rx.el.p(
                            "Club Social",
                            class_name="leading-none font-semibold tracking-wider",
                            color=ThemeState.icon_color,
                        ),    
                        class_name="flex flex-col justify-center ml-3",
                    ),
                    class_name="flex items-center ",
                ),
                href="/",
            ),
            rx.el.div(
                rx.el.nav(
                    navbar_link("Sobre Nosotrxs", "#about_us"),
                    navbar_link("Nuestras actividades", "#servicios"),
                    navbar_link("Contacto", "#redes_sociales"),
                    class_name="hidden md:flex items-center gap-8",
                ),
                rx.el.button(
                    rx.icon("menu", class_name="text-black h-6 w-6  ", cursor="pointer"),
                    on_click=NavbarState.toggle_menu,
                    class_name="md:hidden",
                ),
                class_name="flex items-center gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16",
        ),
        mobile_menu(),
        class_name="sticky top-0 z-10 bg-white/80 backdrop-blur-md border-b border-gray-200",
       # background_color=ThemeState.white_color
    )