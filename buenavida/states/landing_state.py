import reflex as rx
from typing import TypedDict
import re
import json

def open_file() -> list[dict]:
    with open("adicionales/services.json", "r") as f:
        return json.load(f)

def open_file_testimonials() -> list[dict]:
    with open("adicionales/testimonials.json", "r") as f:
        return json.load(f)

class Service(TypedDict):
    icon: str
    title: str
    description: str
    inscripcion: str


class Testimonial(TypedDict):
    avatar: str
    name: str
    text: str


def is_valid_email(email: str) -> bool:
    pattern = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


class LandingState(rx.State):
    is_mobile_menu_open: bool = False
    services: list[Service] = open_file()
    
    testimonials: list[Testimonial] = open_file_testimonials()  

    

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

    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open