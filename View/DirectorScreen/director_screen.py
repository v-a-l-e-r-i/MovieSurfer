from kivymd.uix.label import MDLabel

from View.DirectorScreen.components.item.item import DirectorItemFilm
from View.base_screen import BaseScreenView


class DirectorScreenView(BaseScreenView):
    def on_enter(self):
        self.ids.item_grid.clear_widgets()

    def on_scroll_y(self, instance, value):
        if instance.scroll_y == 0:
            self.model.get_more_data()
            self.add_widgets()

    def message_about_empty_base(self):
        self.ids.box_layout.add_widget(MDLabel(
            text="По вашому запиту не було нічого знайдено!",
            halign='center'
        ))

    def add_widgets(self):
        for i in self.model.data:
            self.ids.item_grid.add_widget(
                DirectorItemFilm(title=i[0], source=i[1], grade=i[2], on_press=self.controller.add_to_base)
            )

    def stream_select(self):
        self.ids.box_stream.md_bg_color = (0, 0, 0, .4)
        self.ids.box_grid.md_bg_color = (0, 0, 0, 0)

        self.ids.stream_icon.text_color = (.522, .71, .765)
        self.ids.grid_icon.text_color = (.706, .776, .796)

        self.ids.item_grid.cols = 1

    def grid_select(self):
        self.ids.box_grid.md_bg_color = (0, 0, 0, .4)
        self.ids.box_stream.md_bg_color = (0, 0, 0, 0)

        self.ids.grid_icon.text_color = (.522, .71, .765)
        self.ids.stream_icon.text_color = (.706, .776, .796)

        self.ids.item_grid.cols = 2