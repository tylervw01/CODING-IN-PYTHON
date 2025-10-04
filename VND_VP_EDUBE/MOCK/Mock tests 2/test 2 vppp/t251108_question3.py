#question 3:
m = int(input("Enter a number: ")) # ask user to enter a number
if m < 2: # check if the number is less than 2
    print("Number must be two or more.") # print error message
else: # if the number is greater than 2
    primes = [] # initialize an empty list
    for num in range(2, m + 1): # loop through the numbers
        if num == 2: # check if the number is 2
            primes.append(num) # add the number to the list
        elif num % 2 != 0: # check if the number is odd
            is_prime = True # initialize a variable
            for i in range(3, int(num**0.5) + 1, 2): # loop through the numbers
                if num % i == 0: # check if the number is divisible
                    is_prime = False # set is_prime to false
                    break # break the loop
            if is_prime: # check if the number is prime
                primes.append(num) # add the number to the list

    print(" ".join(map(str, primes))) # print the list of primes
