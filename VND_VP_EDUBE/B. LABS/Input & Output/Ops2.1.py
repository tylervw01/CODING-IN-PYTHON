hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
hour += dura // 60
mins += dura % 60
if mins >= 60:
    hour += mins // 60
    mins %= 60
print(f"End time: {hour:02d}:{mins:02d}")