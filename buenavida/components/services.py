import reflex as rx
from buenavida.states.landing_state import LandingState, Service
from buenavida.states.theme_state import ThemeState

# @rx.var
# def format(service: Service) -> tuple[str, str]:
#     if ":" in service["time"]:
#         part = service["time"].split(":", 1)
#         return (f"{part[0]}:", part[1].strip())
#     return ("", service["time"])

def service_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(service["icon"], class_name="text-sky-500", size=36, color=ThemeState.icon_color),
            class_name="flex items-center justify-center h-16 w-16 rounded-2xl",
            background_color=ThemeState.icon_bg
        ),
        rx.el.h3(service["title"], class_name="text-xl font-bold text-gray-800 mb-2"),
        rx.el.p(
            service["description"],
            class_name="text-gray-600 leading-relaxed font-medium",
        ),
        rx.el.p(
            rx.el.span(
                service["time"],
                class_name="text-gray-600 leading-relaxed font-bold mt-2",
            ),
        ),
        rx.el.div(
            rx.el.a(
                "Inscribite",
                rx.icon("square-mouse-pointer", class_name="m-1"),
                href=service["inscripcion"],
                class_name="mt-6 inline-flex items-center px-6 py-2 text-white font-semibold rounded-lg shadow-md hover:bg-teal-700 transition-all duration-300",
                background_color=ThemeState.primary_color,
                _hover={"background_color": ThemeState.header_bg},
            ),
            class_name="flex justify-center"
        ),
        class_name="bg-white p-8 rounded-4xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
    )


def services() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Nuestras Actividades",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "Descubrí todo lo que tiene Buena Vida para ofrecerte.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(LandingState.services, service_card),
                class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        id="servicios",
        class_name="bg-gray-50/70",
    )