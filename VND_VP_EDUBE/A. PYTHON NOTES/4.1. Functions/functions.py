def hi(name):
    print("Hi,", name)

hi("Greg")
####
def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")
#######
def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")

address(s, c, p_c)
######
#Ex. 1
def subtra(a, b):
    print(a - b)
subtra(5, 2)    # outputs: 3
subtra(2, 5)    # outputs: -3
#Ex. 2
def subtra(a, b):
    print(a - b)
subtra(a=5, b=2)    # outputs: 3
subtra(b=2, a=5)    # outputs: 3
#Ex. 3
def subtra(a, b):
    print(a - b)

subtra(5, b=2)    # outputs: 3
subtra(5, 2)    # outputs: 3
######
def name(first_name, last_name="Smith"):
    print(first_name, last_name)

name("Andy")    # outputs: Andy Smith
name("Betty", "Johnson")    # outputs: Betty Johnson (the keyword argument replaced by "Johnson")
##########


#Exercise 1
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro()
####

#Exercise 2
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")
####

#Exercise 3
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
#####

#Exercise 4
def add_numbers(a, b=2, c): #switch b=2 with c, so that the order is correct like -> def add_numbers(a, c, b=2):
    print(a + b + c)

add_numbers(a=1, c=3)
