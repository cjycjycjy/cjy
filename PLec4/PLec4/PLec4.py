
#from printData import printData     #모듈이름 귀찮을때 namespace 지정

#def sum_mul(choice, *args):  #입력 개수 모를때 입력값을 tuple형태로 만들어준다
#    if choice == "sum":
#        result =0
#        for i in args:
#            result = result+i      
#    elif choice == "mul":
#        result = 1
#        for i in args:
#            result = result*i
#    return result

#result = sum_mul('sum',1,2,3,4,5,6,7) 
#print(result)


#def sum_and_mul(a,b):
#    return a+b, a*b         #tuple 반환

#print(sum_and_mul(1,5))


#def say_myself(name, old, man=True):    #매개변수 초기화는 맨뒤 부터
#    print("name = %s" %name)
#    print("age = %d" %old)
#    if man:
#        print("man")
#    else:
#        print("woman")

#say_myself("cjy",25)


#data = ["홍길동",["베테랑",["류승완","황정민","유아인"],"암살"],"고길동",["암살"],"김길동",["베테랑","암살"]]

#printData(data)

import os

print(os.getcwd())
#os.mkdir("sample")
os.chdir(".//sample")
print(os.getcwd())
#os.system("python setup.py sdist")
os.system("python setup.py install")