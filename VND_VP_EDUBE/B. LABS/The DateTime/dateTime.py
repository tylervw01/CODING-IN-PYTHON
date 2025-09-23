#LINK TOO PYTHON LIBRARIES
#  https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes 


from datetime import datetime

my_date = datetime(2025, 9, 23, 14, 53)

print(my_date.strftime("%Y/%m/%d %H:%M:%S"))
print(my_date.strftime("%y/%B/%d %H:%S: %p"))
print(my_date.strftime("%a, %Y %b %d"))
print(my_date.strftime("%A, %Y %B %d"))
print(my_date.strftime("Weekday: %w"))
print(my_date.strftime("Day of the year: %j"))
print(my_date.strftime("Week number of the year: %W"))