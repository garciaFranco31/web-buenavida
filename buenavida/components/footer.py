import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("sun", class_name="text-sky-500", size=28),
                    rx.el.h3(
                        "Buena Vida", class_name="text-xl font-bold text-gray-800"
                    ),
                    class_name="flex items-center space-x-2",
                ),
                rx.el.p(
                    "© 2024 Buena Vida. Todos los derechos reservados.",
                    class_name="text-sm text-gray-500 font-medium",
                ),
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "instagram",
                        class_name="text-gray-500 hover:text-sky-500 transition-colors",
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.icon(
                        "facebook",
                        class_name="text-gray-500 hover:text-sky-500 transition-colors",
                    ),
                    href="#",
                ),
                rx.el.a(
                    rx.icon(
                        "twitter",
                        class_name="text-gray-500 hover:text-sky-500 transition-colors",
                    ),
                    href="#",
                ),
                class_name="flex items-center space-x-6",
            ),
            class_name="container mx-auto flex flex-col md:flex-row items-center justify-between p-8 space-y-4 md:space-y-0",
        ),
        class_name="bg-gray-50",
    )