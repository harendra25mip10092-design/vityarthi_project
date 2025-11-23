print("===== Grade Calculator =====")

# Create an empty list to store marks
marks = []

# Input marks of 5 subjects
for i in range(1, 5 + 1):
    m = float(input(f"Enter marks of subject {i}: "))
    marks.append(m)   # Add each mark to the list

# Calculate total and percentage
total = sum(marks)
percentage = total / 5

# Check if any subject is less than 33 → FAIL
failed_subjects = [m for m in marks if m < 33]

# Determine grade and pass/fail status
if failed_subjects:
    grade = "F"
    status = "Fail"
else:
    # Grade calculation using percentage
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "E"
    status = "Pass"

# Display results
print("\n---- Result ----")
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Status:", status)