import reflex as rx

class ConfigWpp:
    phone_number = "+5491160534556"

    @rx.var
    def launch_chat(self) -> str:
        return f"https://wa.me/{self.phone_number}"