from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard


class GenreItemFilm(MDCard):
    title = StringProperty()
    source = StringProperty()
    grade = NumericProperty()