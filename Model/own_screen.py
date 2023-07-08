import psycopg2
from kivy.core.window import Window

from Model.base_model import BaseScreenModel
from Model.config import host, user, db_name, password, port
from View.OwnScreen.components.customSnackbar.customSnackbar import DeleteCustomSnackbar


class OwnScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.own_screen.OwnScreen.OwnScreenView` class.
    """
    data = []

    def delete_film_from_base(self, title):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""delete from own_films
                               where title = '{title}';""")

        except Exception as _ex:
            print(f"[INFO delete film] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = DeleteCustomSnackbar(
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

    def getInfo(self):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT * 
                               FROM own_films """)
            self.data = cursor.fetchall()

        except Exception as _ex:
            print(f"[INFO get info] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()