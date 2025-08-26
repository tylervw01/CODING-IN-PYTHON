user_word = input("Enter your word: ")
user_word = user_word.upper()

for letter in user_word:
   
    if letter in "A, E, I, O, U":
   
        continue
   
    else:
   
        print(letter)

while True:
    
    word = input("Enter a word: ")
    
    if word == "Leave":
        
        print("You've successfully left the loop.")
        
        break