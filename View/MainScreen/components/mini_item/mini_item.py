from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.card import MDCard


class MiniItem(MDCard):
    title = StringProperty()
    source = StringProperty()
    grade = NumericProperty()
    timeline = StringProperty()