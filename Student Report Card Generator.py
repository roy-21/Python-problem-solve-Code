# -----------------------------
# Student Report Card Generator
# -----------------------------

# Step 1: Function to calculate grade based on average marks
def calculate_grade(avg):
    """
    Return grade based on average marks.
    - A+ : 90 and above
    - A  : 80–89
    - B  : 70–79
    - C  : 60–69
    - F  : below 60
    """
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

# Step 2: Dictionary to store student data
# Key = student name, Value = dict of marks, total, average, grade
students = {}

# Step 3: Main loop to input multiple students
while True:
    name = input("Enter student name: ").strip()
    
    # Input number of subjects
    num_subjects = int(input("How many subjects? "))

    # Step 3a: Input marks for each subject
    marks = []
    for i in range(num_subjects):
        mark = int(input(f"Enter mark for subject {i+1}: "))
        marks.append(mark)

    # Step 3b: Calculate total, average, and grade
    total = sum(marks)
    average = total / num_subjects
    grade = calculate_grade(average)

    # Step 3c: Store student info in dictionary
    students[name] = {
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    # Step 3d: Check if user wants to add another student
    more = input("Add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

# Step 4: Display all students report cards
print("\n STUDENT REPORT CARD \n")
for name, info in students.items():
    print("Student:", name)
    print("Marks:", info["marks"])
    print("Total:", info["total"])
    print("Average:", info["average"])
    print("Grade:", info["grade"])
    print("-" * 30)