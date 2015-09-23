
from abc import ABCMeta,abstractmethod 

class Terran(metaclass = ABCMeta):
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def attack(self):
        pass
    
class Tank(Terran):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage

    def attack(self):
        print(self.name+"쏩니다.")


class Marine(Terran):
    def __init__(self,name,hp):
        super().__init__(name)
        self.hp = hp

    def attack(self):
        print(self.name+"총쏩니다.")

#객체 지향
#추상화 은닉화 캡슐화 다형성
def Attack(terran):
    terran.attack()



#t1 = Tank("tank",0)
##t1.attack()
#t2 = Marine("marine",100)
##t2.attack()

#tlist = [Tank("tank1",0),Tank("tank2",0),Marine("marine1",100),Marine("marine2",100)]
#for item in tlist:
#    Attack(item)

#Attack(t1)
#Attack(t2)

#추상클래스는 인스턴스 만들수 없어
#꼭 재정의 해야하는것들은 추상메소드로만들어
#class 클래스이름(metaclass = ......):



class MyList(list):
    name = ""
    def __init__(self,name):
        super().__init__([])
        self.name = name
    def __str__(self):
        return self.name+": "+super().__str__()   #연산자 오버로딩    print 함수는 str 함수를 통해 출력한다.   
                                                    #str함수 오버로딩   ---->__str__()
list1 = MyList("greenjoa")
list1.append(10)
list1.append(20)
list1.append(30)
list1.append(40)
list1.append(50)

print(list1)
#print(dir(list1))

#   __radd__  -> 내가만든 클래스가 뒤에   ///// __add__  --> 내가만든 클래스가 앞에