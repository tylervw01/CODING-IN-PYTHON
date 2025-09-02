#SCENARIO:
# -A car's fuel consumption may be expressed in many different ways. for example, in Europe, it is shown as the amount of fuel consumed per 100 kilometers.
# -In the USA, it is shown as the number of miles traveled by a car using one gallon of fuel.(Task is to write a pair of functions converting 1/100km into mpg, and vice versa)
# #

def liters_100km_to_miles_gallon(litres):
	# Convert liters per 100km to miles per gallon (AMERICAN CONVERTIONS)
	gallons = litres / 3.785411784
	miles = 100 * 1000 / 1609.344 
	return miles / gallons

def miles_gallon_to_liters_100km(miles):
    km100 = miles * 1609.344 / 1000 / 100
    litres = 3.785411784
    return litres / km100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.0))

print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.3))
print(miles_gallon_to_liters_100km(23.5))