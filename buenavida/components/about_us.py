import reflex as rx

def about_us() -> rx.Component:
    return rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.h4(
                            "Sobre Nosotrxs",
                            class_name="text-4xl md:text-4xl font-bold text-gray-900 leading-tight",
                        ),
                        rx.el.p(
                            "Somos el proyecto de reactivación de la histórica pileta del Club Atlético Central Argentino, en Villa Maipú.",
                            class_name="mt-4 text-lg text-gray-600",
                        ),
                        rx.el.p(
                            "Detrás de este sueño, hay un grupo de trabajo formado por nadadores, guardavidas, profes y amigxs de la diversidad LGBTIQ+",
                            class_name="mt-4 text-lg text-gray-600",
                        ),
                        rx.el.p(
                            "El barrio es el inicio de los sueños, es por eso, que este proyecto es, ante todo, un espacio inclusivo y seguro para todas las personas.",
                            class_name="mt-4 text-lg text-gray-600",
                        ),
                        class_name="w-auto md:w-1/2",
                    ),
                    rx.el.div(
                        rx.image(
                            src="images/buenaVida_logo.jpg", #poner logo de buena vida o foto de nosotres
                            alt="Logo de Buena Vida",
                            class_name="rounded-2xl shadow-xl object-cover border border-gray-100",
                            width="auto",
                            height="30em",

                        ),
                        class_name="md:w-1/2 mt-10 md:mt-0",
                        width="auto",

                    ),
                    class_name="flex flex-col md:flex-row items-center gap-8",
                ),
                class_name="bg-white p-8 md:p-16 rounded-3xl shadow-lg border border-gray-100",
                width="100em",

            ),
            class_name="flex justify-center px-4 mt-16 relative",
            id="about_us"
        )