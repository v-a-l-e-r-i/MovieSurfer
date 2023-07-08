from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.snackbar import BaseSnackbar


class AddCustomSnackbar(BaseSnackbar):
    """The class that is responsible for the notification button"""
    text = StringProperty(None)
    icon = StringProperty(None)
    font_size = NumericProperty("15sp")