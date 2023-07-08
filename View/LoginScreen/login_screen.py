from kivymd.uix.boxlayout import MDBoxLayout

from View.base_screen import BaseScreenView


class TextFieldNew(MDBoxLayout):
    pass


class LoginScreenView(BaseScreenView):

    def on_enter(self):
        self.ids.username.text_color_normal = [.486, .482, .486]
        self.ids.username.text = ""
        self.ids.passw.text_color_normal = [.486, .482, .486]
        self.ids.passw.text = ""
