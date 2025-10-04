import reflex as rx
from buenavida.states.landing_state import LandingState, Service


def service_card(service: Service) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(service["icon"], class_name="text-sky-500", size=36),
            class_name="bg-sky-100/70 p-4 rounded-full mb-5",
        ),
        rx.el.h3(service["title"], class_name="text-xl font-bold text-gray-800 mb-2"),
        rx.el.p(
            service["description"],
            class_name="text-gray-600 leading-relaxed font-medium",
        ),
        class_name="bg-white p-8 rounded-2xl border border-gray-100 shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all duration-300",
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
                    "Descubre todo lo que Buena Vida tiene para ofrecerte a ti y a tu familia.",
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