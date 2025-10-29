import reflex as rx


def navbar() -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.icon("sun", class_name="text-sky-500", size=32),
                rx.el.h1("Buena Vida", class_name="text-2xl font-bold text-gray-800"),
                class_name="flex items-center space-x-2",
            ),
            rx.el.nav(
                rx.el.a(
                    "Servicios",
                    href="#servicios",
                    class_name="text-gray-600 font-medium hover:text-sky-500 transition-colors",
                ),
                rx.el.a(
                    "Testimonios",
                    href="#testimonios",
                    class_name="text-gray-600 font-medium hover:text-sky-500 transition-colors",
                ),
                rx.el.a(
                    "Contacto",
                    href="#contacto",
                    class_name="text-gray-600 font-medium hover:text-sky-500 transition-colors",
                ),
                class_name="hidden md:flex items-center space-x-8",
            ),
            rx.el.a(
                rx.el.button(
                    "Inscríbete Ahora",
                    class_name="bg-sky-500 text-white px-5 py-2 rounded-xl font-semibold hover:bg-sky-600 transition-all shadow-sm hover:shadow-md",
                ),
                href="#contacto",
            ),
            cclass_name="container mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center",
        ),
        class_name="sticky top-0 z-50 bg-white/80 backdrop-blur-lg border-b border-gray-100",
    )