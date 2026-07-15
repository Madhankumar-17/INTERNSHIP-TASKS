def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 45:
        return "D"
    else:
        return "F"

print("----- Grade Calculator -----")

for i in range(5):
    marks = float(input(f"Enter marks of Student {i+1} (0-100): "))
    grade = get_grade(marks)
    print(f"Student {i+1}: Grade = {grade}")