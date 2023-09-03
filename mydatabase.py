import sqlite3
conn=sqlite3.connect("userdata.db",check_same_thread=False)
c=conn.cursor()

def create_usertable():
    c.execute("CREATE TABLE IF NOT EXISTS USERTABLE(username TEXT,password TEXT)")

def add_userdata(username, password):
    c.execute("INSERT INTO USERTABLE (username,password) VALUES (?, ?)", (username,password))
    conn.commit()
def login_user(username, password):
    c.execute("select * from USERTABLE WHERE username=? AND password=?", (username, password))
    data=c.fetchall()
    return data

def view_all():
    c.execute("SELECT * FROM USERTABLE")
    data=c.fetchall()
    return data  