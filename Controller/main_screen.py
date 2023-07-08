
from View.MainScreen.main_screen import MainScreenView


class MainScreenController:
    """
    The `MainScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.main_screen.MainScreenModel
        self.view = MainScreenView(controller=self, model=self.model)

    def get_info(self):
        self.model.take_data_from_base()
        self.model.get_more_data()
        self.view.add_widgets()

    def search_film(self, title):
        self.model.search_limit = 10
        self.model.search_offset = 0
        self.model.search_film_by_title(title)
        self.view.ids.text_.text = "Your search"
        self.view.ids.list.clear_widgets()
        if not self.model.data:
            self.view.message_about_empty_base()
        else:
            self.view.load_data()

    def open_info_screen(self, instance):
        self.model.set_info(instance.title)
        self.view.manager.current = "info screen"

    def get_view(self) -> MainScreenView:
        return self.view
