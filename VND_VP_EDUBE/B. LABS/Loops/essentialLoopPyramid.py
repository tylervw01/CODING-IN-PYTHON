# blocks = int (input("Enter the number of blocks: "))

# height = 0

# in_layer = 1

# while in_layer <= blocks:

#     height += 1

#     in_layer += 2
    
#     print("THE HEIGHT OF THE PYRAMID:", height,"\n")
   
# while True:
    
#     number = input("Enter a next number: ")
    
#     if number == "0":
        
#         print("You've successfully stopped.")

#     else:
    
#         print("Lets keep on building", height)
       
#         continue
blocks = int(input("Enter the number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("THE HEIGHT OF THE PYRAMID:", height, "\n")

while True:
    number = input("Enter a next number: ")
    if number == "0":
        print("You've successfully stopped.")
        break
    else:
        print("Lets keep on building", height)
        continue