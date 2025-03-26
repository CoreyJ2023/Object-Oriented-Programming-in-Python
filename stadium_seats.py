#   Programmer:     Corey Jenkins
#   Date:           March 18, 2025
#   Filename:       stadium_seats.py
#

class StadiumSeats():
    def __init__(self, ticket_seat, price):
        self.ticket_seat = ticket_seat
        self.price = price 

def main():
    ticket_seat1 = StadiumSeats("Class A", 13)
    ticket_seat2 = StadiumSeats("Class B", 12)
    ticket_seat3 = StadiumSeats('Class C', 9)

    buyer_class_a = int(input("Input the amount of buyers for Class A seats: "))
    while(buyer_class_a < 0):
        print("An error has occurred.")
        buyer_class_a = int(input("Input the amount of buyers for Class A seats: "))
    class_a_total = buyer_class_a * ticket_seat1.price
    
    buyer_class_b = int(input("Input the amount of buyers for Class B seats: "))
    while(buyer_class_b < 0):
        print("An error has occurred.")
        buyer_class_b = int(input("Input the amount of buyers for Class B seats: "))
    class_b_total = buyer_class_b * ticket_seat2.price 

    buyer_class_c = int(input("Input the amount of buyers for Class C seats: "))
    while(buyer_class_c < 0):
        print("An error has occurred.")
        buyer_class_c = int(input("Input the amount of buyers for Class C seats: "))
    class_c_total = buyer_class_c * ticket_seat3.price 

    buyer_total = buyer_class_a + buyer_class_b + buyer_class_c
    total_cash = class_a_total + class_b_total + class_c_total

    class_a_result = ticket_class_a(buyer_class_a, class_a_total)
    print(ticket_seat1.ticket_seat, class_a_result)
    
    class_b_result = ticket_class_b(buyer_class_b, class_b_total)
    print(ticket_seat2.ticket_seat, (class_b_result))

    class_c_result = ticket_class_c(buyer_class_c, class_c_total)
    print(ticket_seat3.ticket_seat, class_c_result)

    total_result = total_tickets_and_cash(buyer_total, total_cash)
    print(total_result)


def ticket_class_a(num1, num2):
    return f"{num1} of tickets were sold. The total was: ${num2}."

def ticket_class_b(num1, num2):
    return f"{num1} of tickets were sold. The total was: ${num2}."

def ticket_class_c(num1, num2):
    return f"{num1} of tickets were sold. The total was: ${num2}."

def total_tickets_and_cash(num1, num2):
    return f"{num1} of tickets were sold in total. The grand total of cash is ${num2}."
  
main()
