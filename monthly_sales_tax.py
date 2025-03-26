#   Programmer:     Corey Jenkins
#   Date:           March 20, 2025
#   Filename:       monthly_sales_tax.py

class Tax():
    def __init__(self, state, county):
        self.state = state
        self.county = county


def main():
    tax1 = Tax(0.04, 0.02)
    sales = int(input("Enter the amount of sales for the month: "))

    # Formulas
    sales_with_state = sales * tax1.state 
    sales_with_county = sales * tax1.county
    total_sales = sales_with_state + sales_with_county

    sales_state_result = sales_and_state(sales, sales_with_state)
    print(sales_state_result)

    sales_county_result = sales_and_county(sales, sales_with_county)
    print(sales_county_result)

    all_sales_result = all_sales(total_sales)
    print(all_sales_result)

def sales_and_state(num1, num2):
    return f"The amount of sales for the month: {num1}. Total amount in state taxes: " "%.2f" % num2

def sales_and_county(num1, num2):
    return f"The amount of sales for the month: {num1}. Total amount in county taxes: " "%.2f" % num2

def all_sales(num):
    return f"The total amount: ""%.2f" % num

main()
