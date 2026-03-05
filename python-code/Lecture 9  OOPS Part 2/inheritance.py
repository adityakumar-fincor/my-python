"""
Inheritance = when one class (child/derived) drivers the properties & method of another class (parents/base)
"""

class car:
    color = "back"
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped...")
    
class toyotacar(car):
    def __init__(self, name):
        self.name = name

car1 = toyotacar("fortuner")
print(car1.name)
print(car1.start())
print(car1.stop())
print(car1.color)

"""
Inheritance is three type 
Single inheritance
multi-level inheritance
multiple inheritance
"""

#multi-level inheritance

class fortuner(toyotacar):
    def __init__(self, type):
        self.type = type


car2 = fortuner("diesel")
print(car2.type)
car2.start()
print (car2.color)


### multiple inheritance

class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A, B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)