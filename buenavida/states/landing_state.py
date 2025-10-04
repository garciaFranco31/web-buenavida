import reflex as rx
from typing import TypedDict
import re


class Service(TypedDict):
    icon: str
    title: str
    description: str


class Testimonial(TypedDict):
    avatar: str
    name: str
    text: str


def is_valid_email(email: str) -> bool:
    pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


class LandingState(rx.State):
    services: list[Service] = [
        {
            "icon": "waves",
            "title": "Clases de Natación",
            "description": "Aprende a nadar con nuestros instructores certificados. Clases para todas las edades y niveles.",
        },
        {
            "icon": "sun",
            "title": "Pileta Libre",
            "description": "Disfruta de nuestra pileta a tu propio ritmo. Ideal para relajarse y entrenar libremente.",
        },
        {
            "icon": "smile",
            "title": "Colonia de Vacaciones",
            "description": "Diversión garantizada para los más chicos con juegos, deportes y actividades acuáticas supervisadas.",
        },
        {
            "icon": "dumbbell",
            "title": "Entrenamiento Funcional",
            "description": "Complementa tu rutina acuática con clases de acondicionamiento físico en nuestro gimnasio.",
        },
        {
            "icon": "utensils-crossed",
            "title": "Servicio de Buffet",
            "description": "Recarga energías con nuestras opciones saludables y deliciosas en el buffet junto a la pileta.",
        },
    ]
    testimonials: list[Testimonial] = [
        {
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Ana",
            "name": "Ana García",
            "text": "¡La mejor colonia de vacaciones! Mis hijos la pasaron genial y aprendieron un montón. El equipo es súper profesional y amable.",
        },
        {
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Carlos",
            "name": "Carlos Martinez",
            "text": "Las clases de natación son excelentes. El instructor fue muy paciente y me ayudó a superar mi miedo al agua. ¡Ahora disfruto nadar!",
        },
        {
            "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Laura",
            "name": "Laura Fernandez",
            "text": "Me encanta venir a la pileta libre para relajarme después del trabajo. El ambiente es tranquilo y las instalaciones están siempre impecables.",
        },
    ]
    toast_message: str = ""
    show_toast: bool = False

    @rx.event
    def handle_submit(self, form_data: dict):
        email = form_data.get("email", "")
        if not is_valid_email(email):
            self.toast_message = "Por favor, introduce un email válido."
            yield rx.toast.error(self.toast_message)
            return
        self.toast_message = "¡Gracias por tu mensaje! Te contactaremos pronto."
        yield rx.toast.success(self.toast_message)