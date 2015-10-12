import sys
import os
import pickle
import shutil

os.system("Python ../../Testpy/Testpy/testpy.py a b c")

print(sys.path)

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name," : ",self.age)

obj = Student("최종윤",13)
obj.show()

f = open("test.txt", 'wb')
pickle.dump(obj, f)
f.close()

f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
data.show()
f.close()

#print(os.environ)

print(os.getcwd())
#os.chdir('../')
#print(os.getcwd())

#os.system("test.txt")
#os.startfile("test.txt")
#file = os.popen("test.txt")
#print(file.read())

####################################### 현재위치에서 txt파일을 찾아서 sample dir로 복사하기
#os.mkdir("sample")
#mylist = list(os.walk("."))
#print(mylist)

#for (a,b,c) in mylist:
#    for file in c:
#        if file[-4:] == ".txt":
#            print(file)
#            shutil.copy(file,"./sample/t.txt")
        
#########################################################

print(os.path.dirname('c:/python34/python.exe'))            ## 입력받은 파일이나 디렉토리 경로 반환

print(os.path.exists('./sample'))                           ## 입력받은 파일이나 디렉토리가 존재하면 True, 존재하지 않으면 false

#print(os.path.expanduser('~\\python.exe'))                 ## ~ 기호대신 홈 디렉토리로 대체

#getatime 엑세스 시간  ///getmtime 수정한 시간 ////getctime 생성한 시간

