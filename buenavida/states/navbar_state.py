import reflex as rx


class NavbarState(rx.State):
    """State for the navigation bar."""

    nav_links: list[dict[str, str]] = [
        {"name": "Sobre Nosotrxs", "href": "#about_us"},
        {"name": "Nuestras actividades", "href": "#servicios"},
        {"name": "Contacto", "href": "#redes_sociales"},
    ]
    show_menu: bool = False

    @rx.event
    def toggle_menu(self):
        """Toggle the mobile menu."""
        self.show_menu = not self.show_menu