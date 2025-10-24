import reflex as rx
from buenavida.states.landing_state import LandingState, Testimonial
from buenavida.states.theme_state import ThemeState

def testimonial_card(testimonial: Testimonial) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=testimonial["avatar"],
                alt=f"Avatar of {testimonial['name']}",
                class_name="w-16 h-16 rounded-full",
            ),
            class_name="flex-shrink-0",
        ),
        rx.el.div(
            rx.el.blockquote(
                f'''"{testimonial['text']}"''',
                class_name="text-gray-600 font-medium italic",
            ),
            rx.el.cite(
                f"- {testimonial['name']}",
                class_name="mt-4 block text-right font-semibold text-gray-800",
            ),
        ),
        class_name="bg-white p-8 rounded-2xl shadow-sm border border-gray-100 flex flex-col md:flex-row items-center gap-8",
    )


def testimonials() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Lo que dicen nuestros clientes",
                    class_name="text-3xl md:text-4xl font-bold text-gray-800",
                ),
                rx.el.p(
                    "Estamos orgullosos de la comunidad que hemos construido.",
                    class_name="mt-4 text-lg text-gray-600",
                ),
                class_name="text-center mb-12",
            ),
            rx.el.div(
                rx.foreach(LandingState.testimonials, testimonial_card),
                class_name="space-y-8",
            ),
            class_name="container mx-auto px-6 py-20",
        ),
        id="testimonios",
        background_color=ThemeState.form_button_bg,
    )