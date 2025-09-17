#question 2:
password = input("Enter your password: ") # ask user to enter password
length = len(password) # get the length of the password
uppercase = False # initialize variables
lowercase = False # initialize variables
number = False # initialize variables
special = False # initialize variables

for char in password: # loop through each character in the password
    if char.isupper(): # check if the character is uppercase
        uppercase = True # set uppercase to true
    elif char.islower(): # check if the character is lowercase
        lowercase = True # set lowercase to true
    elif char.isdigit(): # check if the character is a digit 
        number = True # set number to true
    elif char in "!@#$": # check if the number is a special character
        special = True # set special to true

if length >= 8 and (uppercase and lowercase and number and special): # check if the password is strong
    print("STRONG") # print strong
elif length >= 8 and (lowercase and (number or special)): # check if the password is medium
    print("MEDIUM") # print medium
else: # if the password is weak
    print("WEAK") # print weak