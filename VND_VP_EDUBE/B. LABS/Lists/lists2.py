# beatles = []
# # print(beatles)

# beatles.append("JOHN LENON")
# beatles.append("PAUL McCARTHY")
# beatles.append("GEORGE HARRISON")
# print(beatles)

# for member in range(2): 
#         beatles.append(input("New Band member: "))
# # ["STU SUTCLIFFE", "PETE BEST"]:
# print("beatles")
    
# del beatles[-1]
# del beatles[-1]
# print(beatles)

# beatles.insert(0, "RINGO STARR")
# print(beatles)

# print("THE FINAL BEATLES LINEUP:", beatles)
#########################################################

# # step 1:
# Beatles = []
# print("Step 1:", Beatles)

# # step 2:

# Beatles.append("John Lennon")
# Beatles.append("Paul McCartney")
# Beatles.append("George Harrison")
# print("Step 2:", Beatles)

# # step 3:
# for members in range(2):
#     Beatles.append(input("New band member: "))
# print("Step 3:", Beatles)

# # step 4:
# del Beatles[-1]
# del Beatles[-1]
# print("Step 4:", Beatles)

# # step 5:
# Beatles.insert(0, "RingoStarr")
# print("Step 5:", Beatles)
# print("The Fab:",len(Beatles))
#####################################

# Step 1: Create an empty list named beatles
beatles = []
print("Step 1:", beatles)

# Step 2: Add John Lennon, Paul McCartney, and George Harrison
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3: Prompt user to add Stu Sutcliffe and Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    name = input(f"Add {member} to the list: ")
    beatles.append(name)
print("Step 3:", beatles)

# Step 4: Remove Stu Sutcliffe and Pete Best
del beatles[-2]  # Assuming they were added in order
del beatles[-1]
print("Step 4:", beatles)

# Step 5: Add Ringo Starr to the beginning of the list
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Final output
print("The Fab", len(beatles))
