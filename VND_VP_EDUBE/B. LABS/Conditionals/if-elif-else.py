year = int (input("Enter a year: "))

if year < 1582:
    print("Not in Calander")
else:
    if year % 4 != 0:
        print("Common Year")
    elif year % 100 != 0:
        print("Leap Year")
    elif year % 400 != 0:
        print("Common Year")
    else:
        print("Leap Year")
        