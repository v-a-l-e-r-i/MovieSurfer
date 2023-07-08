from kivymd.uix.label import MDLabel

from View.OwnScreen.components.swiper_item.swiper_item import MySwiper
from View.base_screen import BaseScreenView


class OwnScreenView(BaseScreenView):

    def on_enter(self):
        self.ids.swiper_md.clear_widgets()
        self.controller.data_entry()

    def filled_widgets(self):
        for i in self.ids.swiper_md.children:
            i.clear_widgets()

        for i in self.model.data:
            self.ids.swiper_md.add_widget(
                MySwiper(
                    title=i[1],
                    source=i[2],
                    director=i[6],
                    description=i[7],
                    genre=i[5],
                    timeline=i[8],
                    year=i[4],
                    grade=i[3],
                    manager=self
                )
            )
