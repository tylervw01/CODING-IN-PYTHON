


students = ("Alice", "Bob", "Charlie")
student_scores = {"Alice": 85, "Bob": 90, "Charlie": 78}
for name in students:
    print(f"{name}: {student_scores[name]}")
highest_student = max(student_scores, key=student_scores.get)
print("Student with highest score:", highest_student)