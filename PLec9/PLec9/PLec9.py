﻿#list = [1,2,3,4]
#print(dir(list))

data = list(enumerate("greenjoa"))
print(data)

print(eval('1+2'))
print(eval('divmod(4,3)'))


def positive(l):
    return l%2==0
print(list(filter(positive, [1,-3,2,0,-5,6])))
print(l[0](3,4))
print(l[1](3,4))

#eval(str("hi".upper())) #에러 발생
print(list(zip("abc", "def")))


####################################  QUIZ ########################################
t = {"홍길동":[80,70,60,92], "김길동":[24,25,18,10], "고길동":[10,20,8,5]}
x=sorted(t.items(), key=lambda x: x[1])
for i in t.values():
    i.sort()
print(x)
