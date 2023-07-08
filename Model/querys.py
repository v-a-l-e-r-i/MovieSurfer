DELETECOPY = f"""DELETE FROM own_films WHERE id IN (SELECT MIN(id) FROM own_films
                                GROUP BY title HAVING COUNT(*) > 1);"""
CREATETABLE = """CREATE TABLE IF NOT EXISTS own_films(
                                id serial PRIMARY KEY,
                                title varchar(255) NOT NULL,
                                photo varchar(255) NOT NULL,
                                grade real NOT NULL,
                                year integer NOT NULL,
                                genre text,
                                director varchar(100),
                                description text,
                                runtime varchar(50));"""
SELECTOWNLIST = """select * from own_films order by id"""
SELECTFILMS = """SELECT * FROM films ORDER BY grade DESC LIMIT 10"""
SELECTOWNFILMS = """select * from own_films"""
