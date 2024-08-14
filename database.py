import sqlite3
from datetime import *

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
             ,("Location_9","ADD"),("Location_10","ADD"),("Location_11","ADD"),("Location_12","ADD"),
             ("Location_13","ADD"),("Location_14","ADD"),("Location_15","ADD"),("Location_16","ADD"),
             ("Location_17","ADD"),("Location_18","ADD"),("Location_19","ADD"),("Location_20","ADD"),
             ("Location_21","ADD"),("Location_22","ADD"),("Location_23","ADD"),("Location_24","ADD")]
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
             ('28','ADD'),('29','ADD'),('30','ADD'),('31','ADD'),('32','ADD'),('33','ADD'),('34','ADD'),('35','ADD'),('36','ADD'),('37','ADD'),
             ('38','ADD'),('39','ADD'),('40','ADD'),('41','ADD'),('42','ADD'),('43','ADD'),('44','ADD'),('45','ADD'),('46','ADD'),('47','ADD'),('48','ADD'),
             ('49','ADD'),('50','ADD'),('51','ADD'),('52','ADD'),('53','ADD'),('54','ADD'),('55','ADD'),('56','ADD'),('57','ADD'),('58','ADD'),('59','ADD'),
             ('60','ADD'),('61','ADD'),('62','ADD'),('63','ADD'),('64','ADD'),('65','ADD'),('66','ADD'),('67','ADD'),('68','ADD'),('69','ADD'),('70','ADD'),
             ('71','ADD'),('72','ADD'),('73','ADD'),('74','ADD'),('75','ADD'),('76','ADD'),('77','ADD'),('78','ADD'),('79','ADD'),('80','ADD'),('81','ADD'),('82','ADD'),
             ('83','ADD'),('84','ADD'),('85','ADD'),('86','ADD'),('87','ADD'),('88','ADD'),('89','ADD'),('90','ADD')]
        c.execute(f'''CREATE TABLE IF NOT EXISTS {location}(id TEXT PRIMARY KEY NOT NULL,status TEXT NOT NULL,model TEXT,number TEXT,
                  minute INTEGER,hour INTEGER,year INTEGER,month INTEGER,day INTEGER)''')
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

def delete_manager(id):
    conn=makeconnection()
    c=conn.cursor()
    c.execute('''DELETE FROM managers
                WHERE id=?''',(id,))
    conn.commit()
    conn.close()

def fetch_code():
    conn=makeconnection()
    c=conn.cursor()
    try:
        c.execute("SELECT * FROM security_code")

    except:
        c.execute("CREATE TABLE IF NOT EXISTS security_code(passcode TEXT NOT NULL)")
        c.execute("INSERT INTO security_code(passcode) VALUES(?)",("1234",))
        conn.commit()

    c.execute("SELECT passcode from security_code")
    passcode=c.fetchone()
    conn.close()
    return passcode[0]

def update_code(code):
    conn=makeconnection()
    c=conn.cursor()
    current_code=fetch_code()
    c.execute('''UPDATE security_code
                SET passcode=?
                WHERE passcode=?''',(code,current_code))
    conn.commit()
    conn.close()
