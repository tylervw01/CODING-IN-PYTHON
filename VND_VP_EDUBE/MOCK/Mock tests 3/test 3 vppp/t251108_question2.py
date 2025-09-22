#Question 2

def fibonacci(n): # FUNCTION
    a, b = 0, 1 # VARIABLES
    for _ in range(n): # FOR LOOP
        yield a # YIELD
        a, b = b, a + b # VARIABLES

n = int(input("Enter the number of Fibonacci numbers to generate: ")) # INPUT
result = [str(num) for num in fibonacci(n)] # LIST COMPREHENSION
print(", ".join(result)) # PRINT
print(f"The sum of the first {n} Fibonacci numbers is: {sum(fibonacci(n))}") # PRINT