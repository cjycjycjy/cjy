import sqlite3
########################create database & create table ##########

con = sqlite3.connect("test.db")
cur = con.cursor()

#sql2 = "drop table if exists phonebook;"
#cur.execute(sql2)
#sql = "create table phonebook(name text, phoneNum text);"
#cur.execute(sql)
#cur.execute("create table user(name text, age int);")
#con.commit()

###############################insert###########################

#insertsql ="insert into phonebook values('G7','010-1111-5222');"
#cur.execute(insertsql)


#insertsql2 = "insert into phonebook values(?,?);"
#name = 'g2'
#phoneNum = '010-3333-5555'
#cur.execute(insertsql2,(name,phoneNum))

#insertsql3 = "insert into phonebook values(:inputName,:inputNum);"
#n = 'g3'
#pN = '010-4444-7777'
#cur.execute(insertsql3,{"inputNum":pN,"inputName":n})

#datalist = (('g4','010-7894-4561'),('g5','010-5644-4561'))
#cur.executemany(insertsql2,datalist)

#def dataGenerator():
#    datalist2 = (('g4','010-7894-4561'),('g5','010-5644-4561'))
#    for item in datalist:
#        yield item
#cur.executemany(insertsql2,dataGenerator())

#cur.execute("insert into phonebook(phoneNum) values('010-7894-1234')")

#cur.execute("insert into user values('최종윤',25)")
#cur.execute("insert into user values('이철헌',30)")
#cur.execute("insert into user values('김종빈',27)")
#cur.execute("insert into user values('곽민기',20)")
#con.commit()    # commit을 해야 database에 영구히 저장이 된다!!
################################################################

#def OrderFunc(str1,str2):
#    s1 = str1.upper()
#    s2 = str2.upper()
#    return (s1 > s2) - (s1 < s2)
#con.create_collation('myordering', OrderFunc)

#selectsql = "select * from phonebook order by name collate myordering;"
#cur.execute(selectsql)
#selectsql2 = "select count(*) from phonebook"
#cur.execute(selectsql2)
#print(cur.fetchone()[0])
#cur.execute("select count(name) from phonebook")
#print(cur.fetchone()[0])

#print(cur.fetchone())
#print(cur.fetchmany(2))
#print(cur.fetchall())

#for row in cur:
#    print(row)

#cur.execute("select * from user order by age desc")
#print(cur.fetchone())

#cur.execute("select max(age) from user")
#print(cur.fetchone()[0])

##############사용자 정의 집계함수   -step과 finalize 함수가 꼭 필요!
#class Average:
#    def __init__(self):
#        self.sum = 0
#        self.cnt = 0

#    def step(self,value):           ##step 에서 뭘 할지
#        self.sum += value
#        self.cnt += 1

#    def finalize(self):             ##마지막에 뭘 반환할지
#        return self.sum/self.cnt

#con.create_aggregate("avg",1,Average)
#con.commit()

#cur.execute("select avg(Age) from user;")
#print(cur.fetchone()[0])






