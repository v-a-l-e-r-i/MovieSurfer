from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.button import MDFillRoundFlatButton

from View.base_screen import BaseScreenView


class InfoScreenView(BaseScreenView):
    title = StringProperty()
    source = StringProperty()
    grade = NumericProperty()
    timeline = StringProperty()
    description = StringProperty()

    def on_enter(self):
        self.model.getInfo()
        self.title = self.model.data[0][0]
        self.source = self.model.data[0][1]
        self.grade = self.model.data[0][2]
        self.timeline = self.model.data[0][5]
        self.description = self.model.data[0][4]
        for i in self.model.data[0][3].split(" ")[:3:]:
            self.ids.grid_genre.add_widget(
                MDFillRoundFlatButton(
                    text=i,
                    font_name="./assets/fonts/RobotoSlab-Regular.ttf",
                    md_bg_color=(.161, .161, .161, .5)
                )
            )