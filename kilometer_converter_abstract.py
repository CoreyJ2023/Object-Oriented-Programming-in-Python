#   Programmer:     Corey Jenkins
#   Date:           March 18, 2025
#   filename:       

from abc import ABC, abstractmethod

class KiloMiles(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calc_miles(self):
        pass

class Kilometer(KiloMiles):
    def __init__(self, kilometers):
        self.kilometers = kilometers

    def calc_miles(self):
        return 0.6214 * self.kilometers
    
def main():
    kilo = Kilometer(30)
    print(kilo.calc_miles())
main()
   