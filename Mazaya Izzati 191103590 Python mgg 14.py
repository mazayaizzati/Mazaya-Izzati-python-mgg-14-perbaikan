#!/usr/bin/env python
# coding: utf-8

# In[8]:


class Polygon: 
    def __init__(self, jumlah_sisi): 
        self.n = no_of_sides 
        self.sides = [0 for i in range(jumlah_sisi)] 
        
def inputSides(self):
    self.sides = [float(input("Masukkan sisi "+str(i+1)+" : ")) for i in range(self.n)] 
    
def dispSides(self): 
    for i in range(self.n): 
        print("sisi",i+1,"adalah",self.sides[i]) 
        
class Triangle(Polygon): 
        def __init__(self): 
            Polygon.__init__(self,3) 

def findArea(self): 
    a, b, c = self.sides 
    # Hitung KeLiLing 
    s = (a + b + c) / 2 
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5 
    print('Luas Segitiga adalah %0.2f' %area) 
    
    t = Triangle() 
    t.inputsides()
    t.findArea() 


# In[ ]:


class Person:
    def _init_(self, first, last):
        self.firstname = first
        self.lastname = last
        
    def Name(self):
        return self.firstname + " " + self.lastname
    
class Employee(person)

    def _init_(self, first, last, staffnum):
        Person._init_(self,first, last)
        self.staffnumber = staffnum
    
    def GetEmployee(self):
        return self.Name() + ", " + self.staffnumber
    
x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())


# In[ ]:


class Car:
    def _init_ (self): 
        self. updateSoftware()
        
        def drive(self):
            print('driving')
            
            def _updateSoftware(self):
                print('updating software')
                
redcar = Car()
redcar.drive()


# In[ ]:


class Car: 
    __maxspeed = 0 
    __name = ""
    
def __init__ (self):
    self.__maxspeed = 200 
    self.__name = "Supercar"
    
def drive(self):
    print('driving. maxspeed ' + str(self. maxspeed)) 
    
redcar = Car() 
redcar.drive() 
redcar.__maxspeed = 10 # Tidak akan berubah karena private 
redcar.drive() 


# In[ ]:


class Car:
    __maxspeed = 0
    __name = ""
    
    def init (self):
        self.__maxspeed = 200
        self.__name = "Supercar
        
    def drive(self):
        print('driving. maxspeed + str(self. maxspeed))
    
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
              
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive() 


# In[ ]:


class Shark():
    def swim(self):
        print("Hiu sedang berenang.") 
        
    def swim backwards(self):
        print("Hiu tidak bisa berenang mundur, tetapi bisa tenggelam ke belakang.")
    
    def skeleton(self):
        print("Kerangka hiu terbuat dari tulang rawan.")
    
class Clownfish():
    def swim(self):
        print("Ikan badut sedang berenang.")
    
    def swim backwards(self):
        print("Ikan badut bisa berenang mundur.")
        
    def skeleton(self):
        print("Kerangka ikan badut terbuat dari tulang.") 
        
sammy = Shark()
sammy.skeleton()

casey = Clownfish()
casey.skeleton() 

