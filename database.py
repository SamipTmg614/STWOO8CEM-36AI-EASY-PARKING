import sqlite3
import datetime
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

def add_manager(id,password):
    conn = makeconnection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO managers VALUES(?,?)",(id,password))

    conn.commit()
    conn.close()

def calculate_time(id,location):
    conn=makeconnection()
    c=conn.cursor()
    c.execute(f"SELECT year FROM {location} WHERE id=?",(id,))
    year=c.fetchone()
    c.execute(f"SELECT month FROM {location} WHERE id=?",(id,))
    month=c.fetchone()
    c.execute(f"SELECT day FROM {location} WHERE id=?",(id,))
    day=c.fetchone()
    c.execute(f"SELECT hour FROM {location} WHERE id=?",(id,))
    hour=c.fetchone()
    c.execute(f"SELECT minute FROM {location} WHERE id=?",(id,))
    minute=c.fetchone()
    current_time=datetime.now()
    entry_time=datetime(year[0],month[0],day[0],hour[0],minute[0])
    difference=current_time-entry_time
    total_minutes=int(difference.total_seconds()/60)
    conn.close()
    return total_minutes

