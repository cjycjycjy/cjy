import turtle;
dic1 ={};
dic2= dict();
dic={'name':'pey','phone':'01093340811','birth':'911217'};
print(dic['name']);
b=list(dic.keys());
print(b);
for step in range(len(b)) :   
    print(b[step]);
 
b=dic.items()
score={};
score = {"ȫ�浿":{"���׶�": 5.0, "�ϻ�" : 4.5 },"��浿":{"���׶�": 1.0, "�ϻ�" : 2.0 },"��浿":{"���׶�": 3.0, "�ϻ�" : 4.0 }}
 
print(score.get("ȫ�浿"));
print(score.get("��浿"));
print(score.get("��浿"));
print(score.get("ȫ�浿").get("�ϻ�"));
 
for dan in range(2,10): 
    print("%d��" %(dan),end=" ");
    for j in range(1,10):
        print("%d x %d = %d" %(dan,j,dan*j),end=" ");
    print("");
 
for steps in range(4) : 
    turtle.forward(100);
    turtle.right(90);
    for moresteps in range(4):
        turtle.forward(50);
        turtle.right(90);
 
nSide=20;
 
for steps in range(nSide) : 
    turtle.forward(100);
    turtle.right(360/nSide);
    for moresteps in range(nSide):
        turtle.forward(50);
        turtle.right(360/nSide);
 