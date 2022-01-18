class Person:
    def __init__(x,name,age):
        x.name = name
        x.age = age
    def myFun(self):
        print("Hello i am "+ self.name)

p1 = Person("John",36)
p1.myFun()
p1.age =40
print(p1.age)