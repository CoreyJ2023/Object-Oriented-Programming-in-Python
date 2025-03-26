#   Programmer:     Corey Jenkins
#   Date:           March 18, 2025
#   Filename:       kilometer_converter.py
#   Purpose:        To convert kilometers to miles using Objecct-Oriented Programming

class KiloMiles:
    def __init__(self, formula):
        self.formula = formula

def main():
    kilometer = KiloMiles(0.6214)
    result = kilo_converter(kilometer.formula)
    print("The amount of miles:", ("%.2f" % result))

def kilo_converter(num1):
    kilometers = float(input("Enter the amount of kilometers: "))
    miles = num1 * kilometers
    return miles
main()