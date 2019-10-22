import sqlite3


def db_check():
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    cursor.execute("""SELECT * FROM statistics""")
    row = cursor.fetchone()
    # выводим список пользователей в цикле
    while row is not None:
        print(
            f"| id: {str(row[0])} |/| dt_cr_us: {str(row[1])} |/| dt_ls_vs: {str(row[2])} "
            f"|/| win: {str(row[3])} |/| lose: {str(row[4])} |/| draw: {str(row[5])} |/| username: {str(row[6])} "
            f"|/| first_name: {str(row[7])} |/| last_name: {str(row[8])} |\n")
        row = cursor.fetchone()

    cursor.close()
    conn.close()


# Удоление поля по id
def db_delete_field(user_id):
    conn = sqlite3.connect("db_rps.db")
    cursor = conn.cursor()

    sql = f"""DELETE FROM statistics WHERE id = {user_id}"""

    cursor.execute(sql)
    conn.commit()

    cursor.close()
    conn.close()


# db_delete_field(user_id)
db_check()
