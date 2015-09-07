﻿#List
data = ['a','b','c',['abcd','efg']]
print(data[0])
print(data[-1])
print(data[-1][-1])
print(data)
 
guest = [] #타입자체가 없음---> 데이터가 변경이 될 시 리스트로 초기화 시키고 사용할것.
a = []
b = [1,2,3]
c = ['Life','is','too','short']
d = [1,2,'life','is']
e = [1,2,['life','is']]
f = b * 3
 
#리스트 수정
guest = ['a','b','c','d']
print(guest)
guest[0] = 'greenjoa'
guest[1] = ['greenjoa1','greenjoa2']
guest[2:3] = ['greenjoa1','greenjoa2']
print(guest)
 
guest.insert(5,"ㅎㅎ")
guest.append("맨뒤에 붙지~")
print(guest)
 
guest.remove("ㅎㅎ")#맨처음 만나는ㅎㅎ를 지우지
guest[1:2] = []#범위를 지워버리지
del guest[0]#인덱스로 지우지
print(guest)
print(guest.index("greenjoa2"))#value가 있는 인덱스를 반환하지요
 
#리스트 값 삽입
data = ['dlcjfgjs321','cjy12120','kjv9004']
data.insert(3,1234)
data.insert(2,1234)
data.insert(1,1234)
data.insert(6,['김종빈','01093340811'])
data.insert(4,['최종윤','01098929802'])
data.insert(2,['이철헌','01012345678'])
print(data)
 
#리스트 엑세스
for step in range(4) : #for문 안에 할려면밑에 들여쓰기를 꼭해야대 파이썬엔 괄호가 없어요 들여쓰기 되어있는 문들이 다 반복되요
    print(guest[step])
print()
length = len(guest)
for step in range(length) : #for list in list 구조임 range(length)도 하나의 리스트이다.
    print(guest[step])
print()
for value in guest :
        print(value)
print()
 

data = ['a','b','c',['abcd','efg']]
for steps in data :
    print(steps)
    
len = len(data)
for steps in range(len) :
        print(data[steps])


for steps in range(len) :
    if isinstance(steps,list) :         # isInstance(object, type)   ---> 리스트 안에 리스트를 뽑아낼 수 있다.
        for step in steps:
            print(step)
    else :
        print(data[steps])

for data in data :
    print(data)

scores = [64,73,52,36,788,456,245]
scores.sort()
print(scores)
scores.reverse();
print(scores)

top5 = scores[0:5]
print(top5)

scores.extend([52,69])
print(scores)

scores.append([123,44])
print(scores)


#튜플은 ()로 이용함 , 튜플은 그 값을 변화 시킬수 없다. 갱신 불가능!!!! (리스트와 차이점)

t1 = ()
t2 = (1,)
t3 = (1)
t4 = (1,2,3)
t5 = 1,2,3
t6 = ('a','b',('ab','cd'))

print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
print(t6)
#튜플도 인덱싱 가능 t[1]      슬라이싱, 연산 가능  !!   BUT!!  변경 연산 하면 에러난다잉
