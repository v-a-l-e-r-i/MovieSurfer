from View.base_screen import BaseScreenView


class RegisterScreenView(BaseScreenView):

    def on_enter(self):
        self.ids.username.text = ""
        self.ids.username.text_color_normal = [.486, .482, .486]
        self.ids.email.text = ""
        self.ids.email.text_color_normal = [.486, .482, .486]
        self.ids.passw.text = ""
        self.ids.passw.text_color_normal = [.486, .482, .486]

    def change_text_color(self):
        self.ids.username.text_color_normal = [.486, .482, .486]
        self.ids.email.text_color_normal = [.486, .482, .486]
        self.ids.passw.text_color_normal = [.486, .482, .486]