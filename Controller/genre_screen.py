
from View.GenreScreen.genre_screen import GenreScreenView


class GenreScreenController:
    """
    The `GenreScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.genre_screen.GenreScreenModel
        self.view = GenreScreenView(controller=self, model=self.model)

    def search_film_by_genre(self, instance):
        self.view.ids.item_grid.clear_widgets()
        self.model.search(instance.text)
        if not self.model.data:
            self.model.show(f"По вашому запиту нічого не знайдено", "information", "orange")
        else:
            self.view.add_widgets()

    def add_to_base(self, instance):
        self.model.add_film(instance.title)
        self.model.show(f"Фільм добавлено!", "check-circle-outline", "green")

    def get_view(self) -> GenreScreenView:
        return self.view
