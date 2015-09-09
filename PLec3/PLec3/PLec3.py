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
score = {"È«±æµ¿":{"º£Å×¶û": 5.0, "¾Ï»ì" : 4.5 },"°í±æµ¿":{"º£Å×¶û": 1.0, "¾Ï»ì" : 2.0 },"±è±æµ¿":{"º£Å×¶û": 3.0, "¾Ï»ì" : 4.0 }}
 
print(score.get("È«±æµ¿"));
print(score.get("°í±æµ¿"));
print(score.get("±è±æµ¿"));
print(score.get("È«±æµ¿").get("¾Ï»ì"));
 
for dan in range(2,10): 
    print("%d´Ü" %(dan),end=" ");
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
 