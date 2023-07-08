from datetime import date

import psycopg2
from kivy.core.window import Window

from Model.base_model import BaseScreenModel

from Model.config import host, user, db_name, password, port
from Model.querys import CREATETABLE, DELETECOPY
from View.InfoScreen.components.customSnackbar.customSnackbar import AddCustomSnackbar


class YearScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.year_screen.YearScreen.YearScreenView` class.
    """
    data = []

    limit = 10
    offset = 10
    search_limit = 10
    search_offset = 0
    year = ""
    year_interval = ["1930-1970", "1970-1990", "1990-2000", "2000-2010", "2010-2020", f"2020-{date.today().year}"]

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

    def search(self, year):
        self.year = year
        self.limit = 10
        self.search_limit = 10
        self.search_offset = 0
        self.offset = 10
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT title, photo, grade, runtime 
                               FROM films 
                               WHERE year >= {self.year[:4]} AND year <= {self.year[-4:]}
                               ORDER BY grade DESC
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
                               WHERE year >= {self.year[:4]} AND year <= {self.year[-4:]}
                               LIMIT {self.limit} OFFSET {self.offset}""")
            self.data = cursor.fetchall()
            self.offset += self.limit

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()