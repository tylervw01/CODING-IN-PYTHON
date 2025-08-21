## Task is to write a tax calculator
income = float(input("Enter the annual income: "))
if income < 85528:
    tax = income * 0.18 - 556.02
## CODE HERE
tax = round(tax, 0)
print("The tax is:", tax, "thalers")