# -----------------------------------------------------------
# Name: Yuvraj Sharma
# Date: 1st November 2025
# Project Title: GradeBook Analyzer
# -----------------------------------------------------------

import csv

print("Welcome to GradeBook Analyzer!")
print("===================================")
print("Choose Input Method:")
print("1. Manual Entry")
print("2. Load from CSV File")

choice = input("Enter your choice (1 or 2): ")

marks = {}

# ----------------------------
# Task 2: Data Entry or CSV Load
# ----------------------------
if choice == "1":
    print("\nEnter student names and marks. Type 'done' to finish.")
    while True:
        name = input("Enter student name: ")
        if name.lower() == "done":
            break
        marks_str = input("Enter marks for {}: ".format(name))
        try:
            marks[name] = float(marks_str)
        except ValueError:
            print("Please enter valid marks (numbers only).")
elif choice == "2":
    filename = input("Enter CSV filename (example: students.csv): ")
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    try:
                        marks[row[0]] = float(row[1])
                    except:
                        pass
    except FileNotFoundError:
        print("File not found!")
else:
    print("Invalid choice!")

# ----------------------------
# Task 3: Basic Calculations
# ----------------------------
if len(marks) > 0:
    values = list(marks.values())
    average = sum(values) / len(values)
    sorted_values = sorted(values)
    n = len(sorted_values)

    # Median
    if n % 2 == 1:
        median = sorted_values[n // 2]
    else:
        median = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

    maximum = max(values)
    minimum = min(values)

    print("\n===== Analysis Summary =====")
    print("Average Marks:", round(average, 2))
    print("Median Marks:", median)
    print("Highest Marks:", maximum)
    print("Lowest Marks:", minimum)

    # ----------------------------
    # Task 4: Assign Grades
    # ----------------------------
    grades = {}
    for name, score in marks.items():
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        grades[name] = grade

    # Grade Distribution
    grade_count = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for g in grades.values():
        grade_count[g] += 1

    print("\n===== Grade Distribution =====")
    for g, count in grade_count.items():
        print(f"{g}: {count}")

    # ----------------------------
    # Task 5: Pass/Fail Lists
    # ----------------------------
    passed_students = [name for name, score in marks.items() if score >= 40]
    failed_students = [name for name, score in marks.items() if score < 40]

    print("\n===== Pass/Fail Summary =====")
    print("Passed Students ({}): {}".format(len(passed_students), ", ".join(passed_students)))
    print("Failed Students ({}): {}".format(len(failed_students), ", ".join(failed_students)))

    # ----------------------------
    # Task 6: Final Table
    # ----------------------------
    print("\n===== Final Results Table =====")
    print("Name\t\tMarks\tGrade")
    print("----------------------------------")
    for name, score in marks.items():
        print(f"{name}\t\t{score}\t{grades[name]}")

else:
    print("\nNo student data found!")

print("\nThank you for using GradeBook Analyzer!")