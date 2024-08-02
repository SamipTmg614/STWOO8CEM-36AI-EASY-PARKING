import sqlite3

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
    c.execute('''CREATE TABLE IF NOT EXISTS managers(
              id TEXT PRIMARY KEY NOT NULL,
              password TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def availability_table():
    conn=makeconnection()
    c=conn.cursor()
    try:
        c.execute("SELECT * FROM availability")

    except :
        lst=[('1','TRUE'),('2','TRUE'),('3','TRUE'),('4','TRUE'),('5','TRUE'),('6','TRUE'),('7','TRUE'),('8','TRUE'),('9','TRUE'),
             ('10','TRUE'),('11','TRUE'),('12','TRUE'),('13','TRUE'),('14','TRUE'),('15','TRUE'),('16','TRUE'),('17','TRUE'),('18','TRUE'),
             ('19','TRUE'),('20','TRUE'),('21','TRUE'),('22','TRUE'),('23','TRUE'),('24','TRUE'),('25','TRUE'),('26','TRUE'),('27','TRUE'),
             ('28','TRUE'),('29','TRUE'),('30','TRUE'),('31','TRUE'),('32','TRUE')]
        c.execute("CREATE TABLE availability(id TEXT PRIMARY KEY NOT NULL,status TEXT NOT NULL,model TEXT,number TEXT)")
        print("A")
        c.executemany("INSERT INTO availability(id,status) VALUES(?,?)",lst)

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

