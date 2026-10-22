# Student Report Card Generator
# Made by - Class 10th Student
# Date - 22 Oct 2026
# This program makes report card for students

print("===== STUDENT REPORT CARD GENERATOR =====")
print("Welcome to my project\n")

# Taking student details
student_name = input("Enter Student Name: ")
student_class = input("Enter Class: ")
roll_no = input("Enter Roll No: ")

print("\n--- Enter Marks Out of 100 ---")
# Taking marks for 5 subjects
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
english = int(input("Enter English Marks: "))
sst = int(input("Enter SST Marks: "))
hindi = int(input("Enter Hindi Marks: "))

# Calculation part
total_marks = maths + science + english + sst + hindi
percentage = total_marks / 5

print("\n===== YOUR REPORT CARD =====")
print(f"Name: {student_name}")
print(f"Class: {student_class}")
print(f"Roll No: {roll_no}")
print("---------------------------")
print(f"Maths: {maths}/100")
print(f"Science: {science}/100")
print(f"English: {english}/100")
print(f"SST: {sst}/100")
print(f"Hindi: {hindi}/100")
print("---------------------------")
print(f"Total Marks: {total_marks}/500")
print(f"Percentage: {percentage}%")

# Grade system - simple if else like 10th student does
if percentage >= 90:
    grade = "A+"
    print("Grade: A+ - Excellent! Keep it up")
elif percentage >= 80:
    grade = "A"
    print("Grade: A - Very Good")
elif percentage >= 70:
    grade = "B"
    print("Grade: B - Good")
elif percentage >= 60:
    grade = "C"
    print("Grade: C - Need to work hard")
elif percentage >= 33:
    grade = "D"
    print("Grade: D - Just Passed")
else:
    grade = "F"
    print("Grade: F - Failed, Try again")

# Extra feature - pass/fail
if percentage >= 33:
    print("\nResult: PASS :)")
else:
    print("\nResult: FAIL :(")

print("\nThank you for using my report card project!")
print("Made with Python - Class 10")
