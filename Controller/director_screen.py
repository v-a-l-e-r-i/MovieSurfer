
from View.DirectorScreen.director_screen import DirectorScreenView


class DirectorScreenController:
    """
    The `DirectorScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.director_screen.DirectorScreenModel
        self.view = DirectorScreenView(controller=self, model=self.model)

    def search_film_by_director(self, director):
        self.view.ids.item_grid.clear_widgets()
        self.model.search(director)
        if not self.model.data:
            self.view.message_about_empty_base()
        else:
            self.view.add_widgets()

    def add_to_base(self, instance):
        self.model.add_film(instance.title)
        self.model.show(f"Фільм добавлено!", "check-circle-outline", "green")

    def get_view(self) -> DirectorScreenView:
        return self.view
