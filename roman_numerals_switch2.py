# Programmer:       Corey Jenkins
# Date              March 18, 2025
# Filename:         roman_numerals_switch2.py
# Purpose:          Using OoP, input validation and a case/switch in Python to select a roman numeral.

class RomanNumerals():
    def __init__(self, number):
        self.number = number 

def main():
    roman_numeral_1 = RomanNumerals("I")
    roman_numeral_2 = RomanNumerals("II")
    roman_numeral_3 = RomanNumerals("III")
    roman_numeral_4 = RomanNumerals("IV")
    roman_numeral_5 = RomanNumerals("V")
    roman_numeral_6 = RomanNumerals("VI")
    roman_numeral_7 = RomanNumerals("VII")
    roman_numeral_8 = RomanNumerals("VIII")
    roman_numeral_9 = RomanNumerals("IX")
    roman_numeral_10 = RomanNumerals("X")

    number_select = int(input("Please select a number from 1 to 10: "))
    while (number_select < 1 or number_select > 10):
        print("An error has occured!")
        number_select = int(input("Please select a number from 1 to 10: "))

    value = number_select
    match value:
        case 1:
            print(roman_numeral_1.number)
            
        case 2:
            print(roman_numeral_2.number)

        case 3:
            print(roman_numeral_3.number)

        case 4:
            print(roman_numeral_4.number)

        case 5:
            print(roman_numeral_5.number)
            
        case 6:
            print(roman_numeral_6.number)

        case 7:
            print(roman_numeral_7.number)

        case 8:
            print(roman_numeral_8.number)

        case 9:
            print(roman_numeral_9.number)

        case 10:
            print(roman_numeral_10.number)
main()

    