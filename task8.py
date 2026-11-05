# Student Marks Matrix Analysis

marks = [
    [80, 75, 90],
    [60, 85, 70],
    [95, 90, 88],
    [40, 50, 45]
]

subjects = ["Maths", "Science", "English"]
students = ["Student 1", "Student 2", "Student 3", "Student 4"]

# Row-wise analysis
print("--- Student Averages ---")
averages = []

for i in range(len(marks)):
    avg = sum(marks[i]) / len(marks[i])
    averages.append(avg)
    print(students[i], "Average:", round(avg, 2))

# Identify top performer
top = averages.index(max(averages))
print("\nTop Performer:", students[top])

# Column-wise analysis
print("\n--- Subject Averages ---")

for j in range(len(subjects)):
    total = 0
    for i in range(len(marks)):
        total += marks[i][j]

    avg = total / len(marks)
    print(subjects[j], "Average:", round(avg, 2))

    if avg < 60:
        print("Low performance in", subjects[j])