import sqlite3
import datetime
result=None
def makeconnection():
    conn = sqlite3.connect('database.db')
    return conn

def user_table():
    conn = makeconnection()
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (username text PRIMARY KEY NOT NULL,name text NOT NULL , phone text NOT NULL, email TEXT NOT NULL, password text NOT NULL)")
    conn.commit()
    conn.close()

def manager_table():
    conn=makeconnection()
    c=conn.cursor()
    try:
        c.execute("SELECT * FROM managers")

    except:
        c.execute('''CREATE TABLE IF NOT EXISTS managers(
                id TEXT NOT NULL,
                password TEXT NOT NULL)''')

        c.execute('''INSERT INTO managers(id,password) VALUES(?,?)
                  ''',("admin","admin@123"))
    conn.commit()
    conn.close()

def location_map():
    conn=makeconnection()
    c=conn.cursor()

    try:
        c.execute("SELECT * FROM location_map")

    except:
        c.execute(f"CREATE TABLE IF NOT EXISTS location_map(id TEXT NOT NULL,name TEXT)")
        lst=[("Location_1","ADD"),("Location_2","ADD"),("Location_3","ADD"),("Location_4","ADD")
             ,("Location_5","ADD"),("Location_6","ADD"),("Location_7","ADD"),("Location_8","ADD")
             ,("Location_9","ADD"),("Location_10","ADD"),("Location_11","ADD"),("Location_12","ADD")]
        c.executemany(f"INSERT INTO location_map(id,name) VALUES(?,?)",lst)
        conn.commit()
        conn.close()


def location_table(location):
    conn=makeconnection()
    c=conn.cursor()

    try:

        c.execute(f"SELECT * FROM {location}")

    except :
        lst=[('1','ADD'),('2','ADD'),('3','ADD'),('4','ADD'),('5','ADD'),('6','ADD'),('7','ADD'),('8','ADD'),('9','ADD'),
             ('10','ADD'),('11','ADD'),('12','ADD'),('13','ADD'),('14','ADD'),('15','ADD'),('16','ADD'),('17','ADD'),('18','ADD'),
             ('19','ADD'),('20','ADD'),('21','ADD'),('22','ADD'),('23','ADD'),('24','ADD'),('25','ADD'),('26','ADD'),('27','ADD'),
             ('28','ADD'),('29','ADD'),('30','ADD'),('31','ADD'),('32','ADD')]
        c.execute(f"CREATE TABLE IF NOT EXISTS {location}(id TEXT PRIMARY KEY NOT NULL,status TEXT NOT NULL,model TEXT,number TEXT)")
        c.executemany(f"INSERT INTO {location}(id,status) VALUES(?,?)",lst)
        conn.commit()
    conn.close()

def get_user(username,password):
    global result
    conn = makeconnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? And password =? ",(username,password))
    result = cursor.fetchall()
    return result

def get_manager(id,password):
    conn = makeconnection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM managers WHERE id=? and password=?",(id,password))
    result=cursor.fetchall()
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

