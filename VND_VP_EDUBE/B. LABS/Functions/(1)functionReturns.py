# OBJECTIVES:
#-projecting and writing parameterizeed functions:
#-utilizing the return statement
# -testing the function
# SCENARIO:
# -Your task is to write and test a function which takes one argument (a year) and returns TRUE if the year is LEAP year, or FALSE otherwise.
# #
def leap_year(year):    
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True 
    elif year % 400 !=0:
        return False
    else:
        return True
#
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]

for i in range (len(test_data)):
    yr = test_data[i]
    print(yr,"-> ",end="")
    result = leap_year(yr)
    
    if result == test_results[i]:
					print("OKAY")
  
else:
      print("Failed")
