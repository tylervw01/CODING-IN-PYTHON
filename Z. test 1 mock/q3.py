
#Question 3
#length converter:
m = float(input("Enter the length in meters: "))
cm = m * 100 
km = m / 1000

print("Length in centimeters:", cm)
print("Length in kilometers:", km)

cm = float(input("Enter the length in centimeters: "))
m = cm / 100
km = cm / 100000

print("Length in meters:", m)
print("Length in kilometers:", km)

km = float(input("Enter the length in kilometers: "))
m = km * 1000
cm = km * 100000

print("Length in meters:", m)
print("Length in centimeters:", cm)
