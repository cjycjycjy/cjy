import sqlite3 as sqlite
from werkzeug import check_password_hash,generate_password_hash

def initDB():
    db = sqlite.connect("test.db")
    with open('schema.sql') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()

def get_DB():
    db = sqlite.connect("test.db")
    return db

def insertDB():
    db = get_DB()
    print("****register****")
    print("user id : ", end="")
    u_id = input()
    cur = db.cursor()
    cur.execute("select userid from user where userid =?",[u_id])
    if cur.fetchone() != None:
        print("exist")
        return
    print("user name : ", end="")
    u_name = input()
    print("user passwd : ", end="")
    u_passwd = input()
    passwd_hash = generate_password_hash(u_passwd)
    sql = "insert into user values(?,?,?,?)"
    cur.execute(sql,(None,u_id,u_name,passwd_hash))
    db.commit()
    db.close()

def selectDB():
    db = get_DB()
    cur = db.cursor()
    cur.execute("select * from user")
    print(cur.fetchall())
#initDB()
#insertDB()
#selectDB()

def login():
    db = get_DB()
    cur = db.cursor()

    print("****login****")
    print("ID : ", end = "")
    inputID = input()
    print("PASSWD : ",end = "")
    inputPASSWD = input()

    cur.execute("select * from user where userid =?",[inputID])
    r = cur.fetchone()
    if r == None:
        print("Not exist")
        return
    elif check_password_hash(r[3],inputPASSWD):
        print("login success")
        return
    else:
        print("check passwd")
        return
login()
    