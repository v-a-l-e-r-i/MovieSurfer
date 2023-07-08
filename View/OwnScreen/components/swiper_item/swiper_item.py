from kivy.properties import NumericProperty, StringProperty, ListProperty, ObjectProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.swiper import MDSwiperItem


class MySwiper(MDSwiperItem):
    title = StringProperty()
    source = StringProperty()
    director = StringProperty()
    description = StringProperty()
    genre = StringProperty()
    timeline = StringProperty()
    year = NumericProperty()
    grade = NumericProperty()
    manager = ObjectProperty()
    dialog = None

    def on_kv_post(self, base_widget):
        self.ids.genre_grid.clear_widgets()
        for i in self.genre.split(" ")[:3:]:
            self.ids.genre_grid.add_widget(
                MDFlatButton(
                    text=i,
                    font_size='13sp',
                    font_name="./assets/fonts/RobotoSlab-Regular.ttf",
                )
            )

    def show_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text=self.description,
                type='custom',
            )
        self.dialog.open()