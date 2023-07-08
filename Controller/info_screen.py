
from View.InfoScreen.info_screen import InfoScreenView


class InfoScreenController:
    """
    The `InfoScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.info_screen.InfoScreenModel
        self.view = InfoScreenView(controller=self, model=self.model)

    def back_to_main(self):
        self.model.title.clear()
        self.view.ids.grid_genre.clear_widgets()
        self.view.manager.current = "main screen"

    def add_film_to_base(self, title):
        self.model.add_to_base(title)
        self.model.show(f"Фільм добавлено!", "check-circle-outline", "green")

    def get_view(self) -> InfoScreenView:
        return self.view
