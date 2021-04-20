class Animal:
    def __init__(self):
        self.age = 0
        self.egg = False 
        
    def getOld(self):
        self.age+=1
        
    def changeEgg(self):
        self.egg = not self.egg 
        
class Human(Animal):
    
    def __init__(self):
        self.moneypower = 11    
#         super().__init__()
        Animal.__init__(self)
        self.moneypower = 11
    def saveMoney(self,earnmoney):
        self.moneypower += earnmoney
     
a = Human()
print(a.age)
print(a.egg)
a.getOld()
print(a.age)
print(a.egg)
a.changeEgg()
print(a.age)
print(a.egg)
print(a.moneypower)
a.saveMoney(100)
print(a.age)
print(a.egg)
print(a.moneypower)
