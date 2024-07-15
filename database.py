import sqlite3

resul=None
def makeconnection():
    conn = sqlite3.connect('database.db')
    return conn


def create_table():
    conn = makeconnection()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text PRIMARY KEY NOT NULL,name text NOT NULL , phone text NOT NULL, email TEXT NOT NULL, password text NOT NULL)")
    conn.commit()
    conn.close()


def get_user(username,password):
    global result
    conn = makeconnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? And password =? ",(username,password))
    result = cursor.fetchall()
    return result

def add_user(username,name,phone,email,password):
    conn = makeconnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES(?,?,?,?,?)",(username,name,phone,email,password))

    conn.commit()
    conn.close()

