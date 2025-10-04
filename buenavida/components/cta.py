import reflex as rx
from buenavida.states.landing_state import LandingState


def cta() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "¿Listo para empezar?",
                    class_name="text-3xl md:text-4xl font-bold text-white",
                ),
                rx.el.p(
                    "Contáctanos para más información o para inscribirte en nuestras actividades. ¡Te esperamos!",
                    class_name="mt-4 text-lg text-sky-100 max-w-2xl mx-auto",
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
                            class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-300 focus:border-sky-300 transition-colors",
                        ),
                        rx.el.input(
                            type="email",
                            placeholder="Tu Email",
                            name="email",
                            required=True,
                            class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-300 focus:border-sky-300 transition-colors",
                        ),
                        class_name="grid grid-cols-1 sm:grid-cols-2 gap-4",
                    ),
                    rx.el.textarea(
                        placeholder="Tu Mensaje...",
                        name="message",
                        rows=4,
                        class_name="w-full px-5 py-3 rounded-xl border-gray-300 focus:ring-sky-300 focus:border-sky-300 transition-colors",
                    ),
                    rx.el.button(
                        "Enviar Mensaje",
                        type="submit",
                        class_name="w-full bg-white text-sky-600 px-8 py-3 rounded-xl font-bold text-lg hover:bg-sky-50 transition-all shadow-lg hover:shadow-xl",
                    ),
                    on_submit=LandingState.handle_submit,
                    reset_on_submit=True,
                    class_name="space-y-4",
                ),
                class_name="mt-12 max-w-xl mx-auto bg-white/20 backdrop-blur-sm p-8 rounded-2xl border border-white/30",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        id="contacto",
        class_name="bg-gradient-to-r from-sky-500 to-cyan-500",
    )