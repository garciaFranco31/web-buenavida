import reflex as rx


def hero() -> rx.Component:
    return rx.el.section(
        rx.el.div(
            rx.el.div(
                rx.el.h1(
                    "Disfruta el Verano al Máximo en ",
                    rx.el.span("Buena Vida", class_name="text-sky-500"),
                    class_name="text-4xl md:text-6xl font-extrabold text-gray-800 leading-tight tracking-tighter",
                ),
                rx.el.p(
                    "Tu oasis de actividades acuáticas, entrenamiento y relax. Todo lo que necesitas para un estilo de vida activo y saludable.",
                    class_name="mt-6 text-lg md:text-xl text-gray-600 max-w-2xl mx-auto",
                ),
                rx.el.div(
                    rx.el.a(
                        rx.el.button(
                            "Ver Actividades",
                            rx.icon("arrow-down", class_name="ml-2"),
                            class_name="bg-sky-500 text-white px-8 py-4 rounded-xl font-bold text-lg hover:bg-sky-600 transition-all shadow-lg hover:shadow-xl transform hover:scale-105",
                        ),
                        href="#servicios",
                    ),
                    class_name="mt-10 flex justify-center",
                ),
                class_name="text-center",
            ),
            class_name="container mx-auto px-6 py-20 md:py-32",
        ),
        class_name="relative bg-amber-50",
    )