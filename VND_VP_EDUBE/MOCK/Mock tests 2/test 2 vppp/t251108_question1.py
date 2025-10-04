#question 1:
n = int(input("Enter the number of scores: ")) # ask user to enter the number of scores they want to enter
scores = [] # initialize an empty list
for i in range(n): # loop through 'n' 
    score = int(input(f"Enter score {i+1}: ")) # ask user to enter a score
    scores.append(score) # add the score to the list

average = sum(scores) / n # calculate the average
highest = max(scores) # find the highest score
lowest = min(scores) # find the lowest score
scores.sort(reverse=True) # sort the scores in descending order

print(f"Average: {average:.2f}") # print the average score
print(f"Highest: {highest}") # print the highest score
print(f"Lowest: {lowest}") # print the lowest score
print("All scores in descending order -> ", scores) # print the list of scores
