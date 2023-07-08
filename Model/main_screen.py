import psycopg2

from Model.base_model import BaseScreenModel

from Model.config import host, user, db_name, password, port
from Model.info_screen import InfoScreenModel


class MainScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.main_screen.MainScreen.MainScreenView` class.
    """
    data_recommend = []
    data = []
    search_limit = 10
    search_offset = 0
    limit = 10
    offset = 10

    def set_info(self, title):
        InfoScreenModel().setInfo(title)

    def search_film_by_title(self, title):
        self.limit = 10
        self.offset = 10
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT title, photo, grade, runtime 
                               FROM films 
                               WHERE title LIKE '%{title}%'
                               ORDER BY grade  DESC
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
                               ORDER BY grade DESC 
                               LIMIT {self.limit} OFFSET {self.offset}""")
            self.data = cursor.fetchall()
            self.offset += self.limit

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()

    def take_data_from_base(self):
        try:
            connection = psycopg2.connect(host=host, user=user, dbname=db_name, password=password,
                                          port=port)
            connection.autocommit = True
            cursor = connection.cursor()
            cursor.execute(f"""SELECT title, photo, grade FROM films ORDER BY grade DESC LIMIT 10""")
            self.data_recommend = cursor.fetchall()

        except Exception as _ex:
            print(f"[INFO] {_ex}")

        finally:
            if connection:
                cursor.close()
                connection.close()