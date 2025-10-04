#SCENARIO:
# - A Natural number is prime if it is greater than 1 and has no divisors other than 1 and itself.
# #
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
        return True
    
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()