

if __name__=="__main__":
    print("module1")

##class Orange:
##    def __init__(self, w, c):
##        self.weight = w
##        self.color = c
##        print("Created!")
##
##or1 = Orange(10, "dark orange")
##or1.weight = 100
##or1.color = "light orange"
##
##print(or1.weight, or1.color)

##class Circle:
##    def __init__(self,r):
##        self.radius = r
##    
##    def area(self):
##        return self.radius**2
##
##c = Circle(7)
##print(c.area())

##class Dog:
##    def __init__(self, name, breed, owner):
##        self.name = name
##        self.breed = breed  # 品種 育てる
##        self.owner = owner
##
##class Person:
##    def __init__(self, name):
##        self.name = name
##
##mick = Person("Mick Jagger")
##stan = Dog("Stanley", "Bulldog", mick)
##print(stan.owner.name)

##class Horse:
##    def __init__(self,b,c,r):
##        self.breed = b
##        self.cries = c
##        self.rider = r
##    def cry(self):
##        print(self.cries)
##class Rider:
##    def __init__(self,n):
##        self.name = n
##take = Rider("Take Yutaka")
##hs = Horse("雑種","bイェーーーん",take)
##print(hs.rider.name)
##hs.cry()
##print(Horse)

class Rectangle:
    recs = []  #
    def __init__(self,w,l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))  #
    def print_size(self):
        print("{} by {} ".format(self.wdith, self.len))
    def __repr__(self):  # オーバーライドしてみる
        print("オーバーライド __repr__ ")
r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 100)
print(Rectangle.recs)  #

print(r1)
