import reflex as rx
from buenavida.states.landing_state import LandingState, Testimonial


def testimonial_card(testimonial: Testimonial) -> rx.Component:
    return rx.el.div(
        rx.icon("quote", class_name="h-10 w-10 text-teal-200"),
        rx.el.p(testimonial["quote"], class_name="mt-4 text-lg text-gray-700 italic"),
        rx.el.div(
            rx.image(
                src=f"https://api.dicebear.com/9.x/initials/svg?seed={testimonial['avatar']}",
                class_name="h-12 w-12 rounded-full",
            ),
            rx.el.div(
                rx.el.p(testimonial["name"], class_name="font-bold text-gray-800"),
                rx.el.p(testimonial["role"], class_name="text-sm text-gray-500"),
            ),
            class_name="mt-6 flex items-center gap-4",
        ),
        class_name="bg-white p-8 rounded-2xl shadow-[0_1px_3px_rgba(0,0,0,0.12)] hover:shadow-[0_8px_16px_rgba(0,0,0,0.2)] transition-shadow duration-300",
    )


def testimonials_section() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "Loved by Teams Worldwide",
                    class_name="text-3xl md:text-4xl font-bold text-center text-gray-800",
                ),
                rx.el.p(
                    "Don't just take our word for it. Here's what our customers have to say.",
                    class_name="mt-4 max-w-2xl mx-auto text-lg text-center text-gray-600",
                ),
                class_name="mb-16",
            ),
            rx.el.div(
                rx.foreach(LandingState.testimonials, testimonial_card),
                class_name="grid md:grid-cols-2 lg:grid-cols-3 gap-8",
            ),
            class_name="container mx-auto px-4 sm:px-6 lg:px-8 py-24",
        ),
        id="testimonials",
        class_name="bg-gray-50",
    )