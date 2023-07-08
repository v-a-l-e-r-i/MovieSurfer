import psycopg2 as psycopg2
from kivy.core.window import Window

from Model.base_model import BaseScreenModel

from Model.config import host, user, db_name, password, port
from View.LoginScreen.components.customSnackbar.customSnackbar import ErrorCustomSnackbar


class RegisterScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.register_screen.RegisterScreen.RegisterScreenView` class.
    """

    def isHaveCopyUsername(self, username):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT * FROM users WHERE username = '{username}' """)
            self.data = cursor.fetchall()
            if not self.data:
                return True
            else:
                return False

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def insert_into_base(self, username, email, passw):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(
                f"""INSERT INTO users (username, email, password) values ('{username}', '{email}', '{passw}');"""
            )

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def show(self, text, icon, color):
        """Pop-up message"""
        snackbar = ErrorCustomSnackbar(
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