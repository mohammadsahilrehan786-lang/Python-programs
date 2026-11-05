# Examination Result and Grace-Mark Validation

n = int(input("Enter number of subjects: "))
grace = int(input("Enter grace marks allowed: "))

total = 0
maximum = 100
failed = 0

for i in range(1, n + 1):
    marks = int(input(f"Enter marks for subject {i}: "))

    if marks < 0 or marks > maximum:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    if marks < 35:
        if 35 - marks <= grace:
            marks = min(35, marks + grace)
            print("Grace marks applied to subject", i)
        else:
            failed += 1

    total += marks
    print("Final marks:", marks)

print("\n--- Examination Result ---")
print("Total Marks:", total, "/", n * maximum)
print("Percentage:", round(total / (n * maximum) * 100, 2), "%")

if failed > 0:
    print("Result: FAIL")
elif total >= n * 75:
    print("Classification: DISTINCTION")
elif total >= n * 60:
    print("Classification: FIRST CLASS")
elif total >= n * 50:
    print("Classification: SECOND CLASS")
else:
    print("Classification: PASS")