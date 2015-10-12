import sys
import os
import pickle
import shutil
import glob

#os.system("Python ../../Testpy/Testpy/testpy.py a b c")

#print(sys.path)

#class Student:
#    def __init__(self,name,age):
#        self.name = name
#        self.age = age

#    def show(self):
#        print(self.name," : ",self.age)

#obj = Student("최종윤",13)
#obj.show()

#f = open("test.txt", 'wb')
#pickle.dump(obj, f)
#f.close()

#f = open("test.txt", 'rb')
#data = pickle.load(f)
#print(data)
#data.show()
#f.close()

#print(os.environ)

#print(os.getcwd())
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
        
##########################################################

#print(os.path.dirname('c:/python34/python.exe'))            ## 입력받은 파일이나 디렉토리 경로 반환

#print(os.path.exists('./sample'))                           ## 입력받은 파일이나 디렉토리가 존재하면 True, 존재하지 않으면 false

#print(os.path.expanduser('~\\python.exe'))                 ## ~ 기호대신 홈 디렉토리로 대체

#getatime 엑세스 시간  ///getmtime 수정한 시간 ////getctime 생성한 시간

## 현재 디렉토리에서 !
#print(glob.glob('*.txt'))      ##확장자
#print(glob.glob('????.*'))       ##이름이 두자리
#print(glob.glob('./[0-9].*'))  ##0에서 9인 
import glob, os.path
#ndir = nfile = 0

#def traverse(dir, depth):
#    global ndir, nfile
#    for obj in glob.glob(dir + '/*'):
#        if depth == 0:
#            prefix = '|--'
#        else:
#            prefix = '|' + ' ' * depth + '|--'
#        if os.path.isdir(obj):
#            ndir += 1
#            print(prefix + os.path.basename(obj))
#            traverse(obj, depth+1)
#        elif os.path.isfile(obj) :
#            nfile +=1
#            print(prefix + os.path.basename(obj))
#        else:
#            print(prefix + 'unknown object:',obj)
#if __name__ == '__main__':
#    traverse('../..', 0)
#    print('\n',ndir,'directories,',nfile, 'files')


#import tempfile
#with tempfile.TemporaryFile('w+',delete=False) as fp:
#    fp.write("aaa")
#    fp.seek(0)
#    data = fp.read()
#    print(fp.name)

#with tempfile.TemporaryDirectory() as fp:
#    print('created temporary directory', fp)


#import time

#print(time.strftime("%B %dth %A %I:%M", time.localtime()))#print(time.strftime("%Y-%m-%d %I:%M", time.localtime()))#time1 = time.ctime()
#t = time.strptime(time1)#print(time1)#print(t.tm_year)

#import calendar
##print(calendar.calendar(2000))
##print(calendar.prcal(2000))
#print(calendar.prmonth(2000, 12))

#print(calendar.weekday(2091, 12, 12))import random#numlist = random.sample(range(100),5)#random.shuffle(numlist)#print(random.choice(numlist))mylist = [('Red',3),('Blue',1),('Green',4),('Yellow',2),]datalist = [val for val, cnt in mylist for i in range(cnt)]       ###datalist = []#for val,cnt in mylist:#    for i in range(cnt):#        datalist.append(val)print(datalist)import webbrowser
url = 'http://google.com'
#webbrowser.open_new_tab(url)
#webbrowser.open_new(url)


##시험 범위는 여기 까지이이이이이이잉이이이이이이잉이이이이이이잉이이이이이이잉
