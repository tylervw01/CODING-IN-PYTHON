#Question 1
# Write a Python program that asks the user for the number of days and hours, then calculates and prints the total number of minutes.
# If the user enters a negative value, display an error message instead of calculating.#

days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))

if days < 0 or hours < 0:
    print("Error: Please enter non-negative values.")
else:
    total_minutes = (days * 24 * 60) + (hours * 60)
    print("Total minutes:", total_minutes)
    