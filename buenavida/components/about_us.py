import reflex as rx

def about_us() -> rx.Component:
    return rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "Sobre Nosotrxs",
                            class_name="text-3xl md:text-4xl font-bold text-gray-900 leading-tight",
                        ),
                        rx.el.p(
                            "Somos el proyecto de reactivación de la histórica pileta del Club Atlético Central Argentino, en Villa Maipú." \
                            "Detrás de este sueño, hay un grupo de trabajo formado por nadadores, guardavidas, profes y amigxs de la diversidad LGBTIQ+" \
                            "El barrio es el inicio de los sueños, es por eso, que este proyecto es, ante todo, un espacio inclusivo y seguro para todas las personas.",
                            class_name="mt-4 text-lg text-gray-600",
                        ),
                        class_name="w-full md:w-1/2",
                    ),
                    rx.el.div(
                        rx.image(
                            src="/ocean.jpg", #poner logo de buena vida o foto de nosotres
                            alt="Feature illustration",
                            class_name="rounded-2xl shadow-xl w-full h-auto object-cover border border-gray-100",
                        ),
                        class_name="w-full md:w-1/2 mt-10 md:mt-0",
                    ),
                    class_name="flex flex-col md:flex-row items-center gap-12",
                ),
                class_name="bg-white p-8 md:p-16 rounded-3xl shadow-lg border border-gray-100",
            ),
            class_name="px-4 -mt-16 z-10 relative",
        )