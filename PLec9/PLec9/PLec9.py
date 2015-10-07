#list = [1,2,3,4]
#print(dir(list))

data = list(enumerate("greenjoa"))
print(data)

print(eval('1+2'))
print(eval('divmod(4,3)'))


def positive(l):
    return l%2==0
print(list(filter(positive, [1,-3,2,0,-5,6])))a=3print(id(3))print(id(a))l = [lambda a,b:a+b, lambda a,b:a*b]
print(l[0](3,4))
print(l[1](3,4))print(list(filter(lambda x: x%2==0, [1,-3,2,0,-5,6])))a= [1,2,3]c = a##위 둘은 아이디 같음##아래만 다름b = list(a)print(id(a))print(id(b))print(id(c))print(list(map(lambda a: a*2, [1,2,3,4])))print(eval(repr("hi".upper())))

#eval(str("hi".upper())) #에러 발생temp = [4,6,2,4,6,1,2,4,5,7]temp.sort()print(temp)print(list(zip([1,2,3], [4,5,6], [7,8,9],[1,2])))
print(list(zip("abc", "def")))


####################################  QUIZ ########################################
t = {"홍길동":[80,70,60,92], "김길동":[24,25,18,10], "고길동":[10,20,8,5]}
x=sorted(t.items(), key=lambda x: x[1])
for i in t.values():
    i.sort()
print(x)

