import reflex as rx
from typing import TypedDict
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
    time: str
    inscripcion: str

class Testimonial(TypedDict):
    avatar: str
    name: str
    text: str

class LandingState(rx.State):

    is_mobile_menu_open: bool = False
    services: list[Service] = open_file()
    
    testimonials: list[Testimonial] = open_file_testimonials()  


    @rx.event
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open