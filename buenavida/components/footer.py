import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.p(
                    "© 2024 Buena Vida. Todos los derechos reservados.",
                    class_name="text-center text-gray-500 font-2xs",
                ),
            class_name="py-8 bg-gray-50"
        ),
        class_name="bg-gray-50",
    )