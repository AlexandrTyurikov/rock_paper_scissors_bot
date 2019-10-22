import sqlite3


def db_create():
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    # Создание таблицы
    cursor.execute("""CREATE TABLE statistics
                      (id INTEGER NOT NULL, date_create_user TEXT, date_last_visit TEXT,
                      win INTEGER, lose INTEGER, draw INTEGER, username TEXT, first_name TEXT, last_name TEXT)
                   """)

    cursor.close()
    conn.close()


db_create()
