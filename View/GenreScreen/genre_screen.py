from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.label import MDLabel

from View.GenreScreen.components.item.item import GenreItemFilm
from View.base_screen import BaseScreenView


class GenreScreenView(BaseScreenView):

    def on_enter(self):
        if not self.ids.genre_box.children:
            for genre in self.model.genre_:
                self.ids.genre_box.add_widget(
                    MDFillRoundFlatButton(
                        text=genre,
                        md_bg_color=(.522, .71, .765),
                        theme_text_color="Custom",
                        text_color='black',
                        font_name="./assets/fonts/RobotoSlab-Regular.ttf",
                        on_press=self.controller.search_film_by_genre
                    )
                )

    def on_scroll_y(self, instance, value):
        if instance.scroll_y == 0:
            self.model.get_more_data()
            self.add_widgets()

    def add_widgets(self):
        for i in self.model.data:
            self.ids.item_grid.add_widget(
                GenreItemFilm(title=i[0], source=i[1], grade=i[2], on_press=self.controller.add_to_base)
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