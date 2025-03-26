#   Programmer:     Corey Jenkins
#   Date:           March 18, 2025
#   Filename:       kilometer_converter_immutable.py
#   Purpose:        Object-oriented with an immutable added.

from dataclasses import dataclass

@dataclass(frozen=True) # This class is immutable. Can't be changed whatsoever.
class KiloMiles():
    formula: float = 0.6214

def main():
    converter = KiloMiles() 
    result = kilo_to_miles(converter.formula)
    print("The amount of kilometer(s) to mile(s): ", ("%.2f" % result))

def kilo_to_miles(num1):
    kilometers = float(input("Please enter the amount of kilometer(s): "))
    miles = num1 * kilometers 
    return miles

main()

