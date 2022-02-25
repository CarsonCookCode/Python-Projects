

from abc import ABC, abstractmethod
 
class Polygon(ABC):
    
    # regular method
    def shape(self):
        print("I am a shape")
        
     # defining abstract method
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

R = Triangle()
R.shape()
R.noofsides()
