
from View.RegisterScreen.register_screen import RegisterScreenView


class RegisterScreenController:
    """
    The `RegisterScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.register_screen.RegisterScreenModel
        self.view = RegisterScreenView(controller=self, model=self.model)

    def create_account(self, username, email, password):
        if username != "" and email != "" and password != "":
            if self.model.isHaveCopyUsername(username):
                self.model.insert_into_base(username, email, password)
                self.view.manager.current = "login screen"
            else:
                self.view.ids.username.text_color_normal = "red"
                self.view.ids.email.text_color_normal = "red"
                self.view.ids.passw.text_color_normal = "red"
                self.model.show(f"Користувач з таким ім'ям уже існує", "alert-circle", "red")
        else:
            self.model.show(f"Введіть усі дані", "information", "orange")

    def get_view(self) -> RegisterScreenView:
        return self.view
