# Programmer:   Corey Jenkins
# Date:         March 18, 2025
# Filename:     body_mass_index.py
# Purpose:      To create a BMI calculator using object-oriented programming and input validations.

import math # To add pow() or square root to calculate properly!
class BodyMassIndex():
    def __init__(self, formula):
        self.formula = formula

def main():
    weight_formula = BodyMassIndex(703)
    result = body_mass_index_calculation(weight_formula.formula)
    print("The BMI is:" , (result))

def body_mass_index_calculation(num1):
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in feet: "))

    # Input validation
    while(weight < 1 or height < 1):
        print("An error has occurred. Please enter a postive number!")
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in feet: "))
    
    inches = height * 12 # To convert to inches 
    inches_conversion = pow(inches, 2)
    bmi = (num1 * (weight / inches_conversion))
    return "%.2f" % bmi
main()