
from View.OwnScreen.own_screen import OwnScreenView


class OwnScreenController:
    """
    The `OwnScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.own_screen.OwnScreenModel
        self.view = OwnScreenView(controller=self, model=self.model)

    def data_entry(self):
        self.model.getInfo()
        if not self.model.data:
            self.model.show(f"Ваш список порожній", "information", "orange")
        else:
            self.view.filled_widgets()

    def delete_film(self, title, object):
        self.model.delete_film_from_base(title)
        self.view.ids.swiper_md.remove_widget(object)
        self.model.show(f"Фільм видалено!", "check-circle-outline", "green")

    def get_view(self) -> OwnScreenView:
        return self.view
