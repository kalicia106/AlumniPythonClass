print("Enter student score")
grade = int (input())


if grade < 80 and grade >= 70:
    print("Student receives a C")

elif grade < 90 and grade >= 80:
    print("Student receives a B")

elif grade >= 90:
    print("Student receives an A ")

elif grade >=55 and grade < 70:
    print("Student receives a D")

elif grade < 55:
    print("Student receives an F")

else:
    print("Invalid score entry.")
