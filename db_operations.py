import sqlite3
from datetime import datetime


def db_all_id():
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT id FROM statistics""")
    rez = cursor.fetchall()
    all_id = []
    for id_user in rez:
        all_id.append(id_user[0])

    cursor.close()
    conn.close()
    return all_id


def db_add_user(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(
        f"""INSERT INTO statistics (id, date_create_user, date_last_visit,
                                  win, lose, draw, username, first_name, last_name)
        VALUES (
                '{message.from_user.id}',
                '{datetime.now().strftime('%d.%m.%Y_%H:%M')}',
                '{datetime.now().strftime('%d.%m.%Y_%H:%M')}',
                0,
                0,
                0,
                '{message.from_user.username}',
                '{message.from_user.first_name}',
                '{message.from_user.last_name}'
                )""")
    conn.commit()

    cursor.close()
    conn.close()


def db_date_last_visit(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
    old = cursor.fetchone()
    cursor.execute(f"""
        UPDATE statistics SET date_last_visit = '{datetime.now().strftime('%d.%m.%Y_%H:%M')}'
        WHERE date_last_visit = '{old[2]}'""")
    conn.commit()

    cursor.close()
    conn.close()


def db_update_win(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
    win_all = cursor.fetchone()
    win = win_all[3] + 1
    cursor.execute(f"""UPDATE statistics SET win = '{win}' WHERE win = '{win_all[3]}'""")
    conn.commit()

    cursor.close()
    conn.close()


def db_update_lose(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
    lose_all = cursor.fetchone()
    lose = lose_all[4] + 1
    cursor.execute(f"""UPDATE statistics SET lose = '{lose}' WHERE lose = '{lose_all[4]}'""")
    conn.commit()

    cursor.close()
    conn.close()


def db_update_draw(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
    draw_all = cursor.fetchone()
    draw = draw_all[5] + 1
    cursor.execute(f"""UPDATE statistics SET draw = '{draw}' WHERE draw = '{draw_all[5]}'""")
    conn.commit()

    cursor.close()
    conn.close()


def db_read(user_id):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={user_id}""")
    old = cursor.fetchone()
    win = old[3]
    lose = old[4]
    draw = old[5]

    cursor.close()
    conn.close()
    return win, lose, draw


def db_reset_results(message):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
    results_all = cursor.fetchone()
    cursor.execute(f"""UPDATE statistics SET win = 0 WHERE win = '{results_all[3]}'""")
    cursor.execute(f"""UPDATE statistics SET lose = 0 WHERE lose = '{results_all[4]}'""")
    cursor.execute(f"""UPDATE statistics SET draw = 0 WHERE draw = '{results_all[5]}'""")
    conn.commit()

    cursor.close()
    conn.close()


# def db_reset_results(message):
#     conn = sqlite3.connect("db_rps.db")
#     cursor = conn.cursor()
#
#     cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
#     results_all = cursor.fetchone()
#     cursor.execute(f"""UPDATE statistics SET win = 0 WHERE win = '{results_all[3]}'""")
#     conn.commit()
#
#     cursor.close()
#     conn.close()
#
#     conn = sqlite3.connect("db_rps.db")
#     cursor = conn.cursor()
#
#     cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
#     results_all = cursor.fetchone()
#     cursor.execute(f"""UPDATE statistics SET win = 0 WHERE win = '{results_all[4]}'""")
#     conn.commit()
#
#     cursor.close()
#     conn.close()
#
#     conn = sqlite3.connect("db_rps.db")
#     cursor = conn.cursor()
#
#     cursor.execute(f"""SELECT * FROM statistics WHERE id={message.from_user.id}""")
#     results_all = cursor.fetchone()
#     cursor.execute(f"""UPDATE statistics SET win = 0 WHERE win = '{results_all[5]}'""")
#     conn.commit()
#
#     cursor.close()
#     conn.close()
