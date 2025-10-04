import reflex as rx
from buenavida.states.landing_state import LandingState


def contact_form() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Ponte en Contacto con Nosotros",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "¿Tienes alguna pregunta o deseas inscribirte en nuestras actividades? Completa el formulario y te responderemos a la brevedad.",
                    class_name="mt-4 text-lg text-gray-600 max-w-2xl mx-auto",
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.form(
                    rx.el.div(
                        rx.el.input(
                            placeholder="Tu Nombre",
                            name="name",
                            required=True,
                            class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-500 focus:border-sky-500 transition-colors bg-white",
                        ),
                        rx.el.input(
                            type="email",
                            placeholder="Tu Email",
                            name="email",
                            required=True,
                            class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-500 focus:border-sky-500 transition-colors bg-white",
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 gap-4",
                    ),
                    rx.el.textarea(
                        placeholder="Tu Mensaje...",
                        name="message",
                        rows=4,
                        class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-500 focus:border-sky-500 transition-colors bg-white",
                    ),
                    rx.el.button(
                        "Enviar Mensaje",
                        type="submit",
                        class_name="w-full bg-sky-500 text-white px-8 py-3 rounded-xl font-bold text-lg hover:bg-sky-600 transition-all shadow-md hover:shadow-lg",
                    ),
                    on_submit=LandingState.handle_submit,
                    reset_on_submit=True,
                    class_name="space-y-4",
                ),
                class_name="mt-12 max-w-xl mx-auto bg-white p-8 sm:p-10 rounded-2xl border border-gray-200 shadow-sm",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        id="contacto",
        class_name="bg-gray-50",
    )