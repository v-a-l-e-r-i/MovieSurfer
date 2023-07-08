from kivymd.uix.button import MDFillRoundFlatButton

from View.YearScreen.components.item.item import YearItemFilm
from View.base_screen import BaseScreenView


class YearScreenView(BaseScreenView):

    def on_enter(self):
        if not self.ids.year_box.children:
            for year in self.model.year_interval:
                self.ids.year_box.add_widget(
                    MDFillRoundFlatButton(
                        text=year,
                        md_bg_color=(.522, .71, .765),
                        theme_text_color="Custom",
                        text_color='black',
                        font_name="./assets/fonts/RobotoSlab-Regular.ttf",
                        on_press=self.controller.search_by_year
                    )
                )

    def on_scroll_y(self, instance, value):
        if instance.scroll_y == 0:
            self.model.get_more_data()
            self.add_widgets()

    def add_widgets(self):
        for i in self.model.data:
            self.ids.item_grid.add_widget(
                YearItemFilm(title=i[0], source=i[1], grade=i[2], on_press=self.controller.add_to_base)
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