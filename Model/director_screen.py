import psycopg2
from kivy.core.window import Window

from Model.base_model import BaseScreenModel

from Model.config import host, user, db_name, password, port
from Model.querys import CREATETABLE, DELETECOPY
from View.InfoScreen.components.customSnackbar.customSnackbar import AddCustomSnackbar


class DirectorScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.director_screen.DirectorScreen.DirectorScreenView` class.
    """
    data = []

    limit = 10
    offset = 10
    search_limit = 10
    search_offset = 0
    director = ""

    def add_film(self, title):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(CREATETABLE)
            cursor.execute(
                f"""INSERT INTO own_films (title, photo, grade, year, genre, director, description, runtime)
                        SELECT title, photo, grade, year, genre, director, description, runtime
                        FROM films
                        WHERE title = '{title}';"""
            )

            cursor.execute(DELETECOPY)

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = AddCustomSnackbar(
            text=f"{text}",
            icon=f"{icon}",
            snackbar_x="10dp",
            snackbar_y="10dp",
            bg_color=(.91, .91, .91, 1),
        )
        snackbar.size_hint_x = (
                                       Window.width - (snackbar.snackbar_x * 2)
                               ) / Window.width
        snackbar.ids.icon.icon_color = f"{color}"
        snackbar.open()

    def search(self, director):
        self.director = director
        self.limit = 10
        self.offset = 10
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT title, photo, grade, runtime 
                                           FROM films 
                                           WHERE director LIKE '%{director}%'
                                           LIMIT {self.search_limit} OFFSET {self.search_offset}""")
            self.data = cursor.fetchall()
            self.search_offset += self.search_limit

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def get_more_data(self):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT title, photo, grade, runtime 
                                   FROM films 
                                   WHERE director LIKE '%{self.director}%'
                                   LIMIT {self.limit} OFFSET {self.offset}""")
            self.data = cursor.fetchall()
            self.offset += self.limit

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()