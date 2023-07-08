from kivymd.uix.label import MDLabel

from View.MainScreen.components.item.item import ItemFilm
from View.MainScreen.components.mini_item.mini_item import MiniItem
from View.base_screen import BaseScreenView
import time


class MainScreenView(BaseScreenView):

    def on_enter(self):
        self.model.limit = 10
        self.model.offset = 10
        self.ids.list.clear_widgets()
        self.controller.get_info()
        self.load_data()

    def load_data(self):
        for i in self.model.data:
            self.ids.list.add_widget(
                MiniItem(title=i[0], source=i[1], grade=i[2], timeline=i[3], on_press=self.controller.open_info_screen)
            )

    def message_about_empty_base(self):
        self.ids.list.add_widget(MDLabel(
            text="По вашому запиту не було нічого знайдено!",
            halign='center'
        ))

    def on_scroll_y(self, instance, value):
        if instance.scroll_y == 0:
            self.model.get_more_data()
            self.load_data()

    def add_widgets(self):
        if not self.ids.top_box.children:
            for i in self.model.data_recommend:
                self.ids.top_box.add_widget(ItemFilm(title=i[0],source=i[1],grade=i[2], on_press=self.controller.open_info_screen))

        self.ids.screen_.remove_widget(self.ids.spinner)
        self.ids.contrent.opacity = 1