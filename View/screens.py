# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.register_screen import RegisterScreenModel
from Controller.register_screen import RegisterScreenController
from Model.main_screen import MainScreenModel
from Controller.main_screen import MainScreenController
from Model.info_screen import InfoScreenModel
from Controller.info_screen import InfoScreenController
from Model.genre_screen import GenreScreenModel
from Controller.genre_screen import GenreScreenController
from Model.year_screen import YearScreenModel
from Controller.year_screen import YearScreenController
from Model.director_screen import DirectorScreenModel
from Controller.director_screen import DirectorScreenController
from Model.own_screen import OwnScreenModel
from Controller.own_screen import OwnScreenController

screens = {
    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
    },

    "register screen": {
        "model": RegisterScreenModel,
        "controller": RegisterScreenController,
    },

    "main screen": {
        "model": MainScreenModel,
        "controller": MainScreenController,
    },

    "info screen": {
        "model": InfoScreenModel,
        "controller": InfoScreenController,
    },

    "genre screen": {
        "model": GenreScreenModel,
        "controller": GenreScreenController,
    },

    "year screen": {
        "model": YearScreenModel,
        "controller": YearScreenController,
    },

    "director screen": {
        "model": DirectorScreenModel,
        "controller": DirectorScreenController,
    },

    "own screen": {
        "model": OwnScreenModel,
        "controller": OwnScreenController,
    },
}