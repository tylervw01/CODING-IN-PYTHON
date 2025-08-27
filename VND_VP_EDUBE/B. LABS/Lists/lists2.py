# Step 1: Create an empty list
beatles = []

# Step 2: Add initial members
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# Step 3: Prompt user to add Stu Sutcliffe and Pete Best
for member in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(input(f"Add {member}: "))

# Step 4: Remove Stu Sutcliffe and Pete Best
del beatles[-1]  # Remove Pete Best
del beatles[-1]  # Remove Stu Sutcliffe

# Step 5: Add Ringo Starr to the beginning
beatles.insert(0, "Ringo Starr")

print("Final Beatles lineup:", beatles)