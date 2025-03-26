# Programmer:       Corey Jenkins
# Date:             March 18, 2025
# Filename:         body_mass_immutable.py

from dataclasses import dataclass
import math # Needs the square root to calculate this program properly!

@dataclass(frozen=True) # This makes it immutable or unchangable!
class BodyMassIndex():
        formula: float = 703

def main():
    number = BodyMassIndex()
    result = body_mass_index_calculation((number.formula))
    print("BMI is:", ("%.2f" % result))

def body_mass_index_calculation(num1):
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("enter your height in feet: "))
    while(weight < 1 or height < 1):
        print("An error has occurred! Please enter a number greater than 0!")
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("enter your height in feet: "))
    inches = height * 12
    inches_converter = pow(inches,2)
    bmi = (num1 * (weight / inches_converter))
    return bmi
main()
