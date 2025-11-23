# vityarthi_project
A simple Python program that takes marks for five subjects, calculates total, percentage, grade, and pass/fail status. It checks if any subject is below 33 and marks the student as failed. Ideal for beginners learning loops, lists, and conditional logic in Python.


Here is a clean and professional **README.md** file you can use for GitHub for your Grade Calculator project:

---

# 📘 Grade Calculator (Python)

A simple Python program that takes marks of five subjects, calculates the total, percentage, grade, and determines whether the student has passed or failed.
This program also checks if the student has failed any individual subject (marks < 33).

---

## 🚀 Features

* Takes input for 5 subjects
* Calculates:

  * Total Marks
  * Percentage
  * Grade
  * Pass/Fail status
* Automatically marks **Fail** if any subject is below **33**
* Supports clean and readable output formatting

---

## 📂 Code

```python
print("===== Grade Calculator =====")

# Create an empty list to store marks
marks = []

# Input marks for subjects (e.g., 5 subjects in this case)
num_subjects = 5
for i in range(1, num_subjects + 1):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)  # Add each mark to the list

# Calculate total and percentage
total = sum(marks)
percentage = total / num_subjects

# Check if any subject is less than 33 → FAIL
failed_subjects = [m for m in marks if m < 33]

# Determine grade and pass/fail status
if failed_subjects:
    grade = "F"
    status = "Fail"
else:
    # Grade calculation based on percentage
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

# Display results with formatting
print("\n---- Result ----")
print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")
```

---

## 🧮 Grade Criteria

| Percentage      | Grade    |
| --------------- | -------- |
| 90+             | A+       |
| 80–89           | A        |
| 70–79           | B        |
| 60–69           | C        |
| 50–59           | D        |
| <50             | E        |
| Any subject <33 | F (Fail) |

---

## 📌 How to Run

1. Install Python (3.x recommended)
2. Save the script as `grade_calculator.py`
3. Run in terminal:

```bash
python grade_calculator.py
```

4. Enter marks when prompted.

---

## 📄 License

This project is open-source. Feel free to modify and improve it.
