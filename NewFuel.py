#   Programmer:     Corey Jenkins
#   Date:           March 17, 2025
#   Filename:       newFuel.py
#   Purpose:        

class Fuel:
    def __init__(self, fuel_grade, price):
        self.fuel_grade = fuel_grade
        self.price = price
        

    def __str__(self):
        return f"You have selected: {self.fuel_grade}. Price is: {self.price}."

def main():
    regular = Fuel("Regular", 3.99)
    plus = Fuel("Plus", 4.99)
    supreme = Fuel("Supreme", 5.99)

    fuel_select = int(input("Please enter your fuel grade: "))
    while(fuel_select < 1 or fuel_select > 3):
        print("An error occurred!")
        print("Please enter your fuel grade.")
        print("1 - Regular")
        print("2 - Plus")
        print("3 - Supreme")
        fuel_select = int(input())
    
    if(fuel_select == 1):
        print("You have entered: ", regular.fuel_grade)
        gallons = int(input("Enter the amount of gallons: "))
        while(gallons < 0):
            print("An error has occurred.")
            print("Enter a non-negative number:")
            gallons = int(input())
        total = gallons * regular.price
        print(regular)
        print("Your total is:", ("%.2f" % total))

    elif(fuel_select == 2):
        print('You have entered:', plus.fuel_grade)
        gallons = int(input("Enter the amount of gallons: "))
        while(gallons < 0):
            print("An error has occurred.")
            print("Enter a non-negative number")
            gallons = int(input())

        total = gallons * plus.price
        print(plus)
        print("Your total is:", ("%.2f" % total))

    elif(fuel_select == 3):
        print('You have entered: ', supreme.fuel_grade)
        gallons = int(input("Enter the amount of gallons: "))
        while(gallons < 0):
            print("An error has occurred.")
            print("Enter a non-negative number:")
            gallons = int(input(gallons))

        total  = gallons * supreme.price
        print(plus)
        print("Your total is:", ("%.2f" % total))

main()
  
