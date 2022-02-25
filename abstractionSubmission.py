

from abc import ABC, abstractmethod
 
class Polygon(ABC):
     # defining abstract method
    @abstractmethod
    def noofsides(self):
        pass
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")

R = Triangle()
R.noofsides()
