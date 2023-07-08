
from View.LoginScreen.login_screen import LoginScreenView


class LoginScreenController:
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.login_screen.LoginScreenModel
        self.view = LoginScreenView(controller=self, model=self.model)

    def loginToSystem(self, username, password):
        if username != "" and password != "":
            if self.model.isTrueUsername(username) and self.model.isTruePassword(password):
                self.view.manager.current = "main screen"
            else:
                if not self.model.isTrueUsername(username) and not self.model.isTruePassword(password):
                    self.view.ids.username.text_color_normal = "red"
                    self.view.ids.passw.text_color_normal = "red"
                    self.model.show(f"Не вірно введені дані", "alert-circle", "red")
                elif not self.model.isTrueUsername(username):
                    self.view.ids.passw.text_color_normal = [.486, .482, .486]
                    self.view.ids.username.text_color_normal = "red"
                    self.model.show(f"Не вірний username", "alert-circle", "red")
                else:
                    self.view.ids.username.text_color_normal = [.486, .482, .486]
                    self.view.ids.passw.text_color_normal = "red"
                    self.model.show(f"Не вірний пароль", "alert-circle", "red")

    def get_view(self) -> LoginScreenView:
        return self.view
