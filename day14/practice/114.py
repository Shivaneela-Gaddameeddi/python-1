
# Accept number of students
n = int(input("Enter number of students: "))

# Create an empty list
marks = []

# Accept marks of each student
for i in range(n):
    m = float(input(f"Enter marks of Student {i+1}: "))
    marks.append(m)

# Calculate total, average, highest and lowest
total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

# Initialize counters
pass_count = 0
fail_count = 0

# Display individual student results
print("\n========== STUDENT RESULTS ==========")

for i in range(n):

    print(f"\nStudent {i+1}")
    print(f"Marks: {marks[i]}")

    if marks[i] >= 40:
        print("Result: PASS")
        pass_count += 1

    else:
        print("Result: FAIL")
        fail_count += 1

# Display overall analysis
print("\n========== MARKS ANALYSIS ==========")
print(f"Total Marks    : {total:.2f}")
print(f"Average Marks  : {average:.2f}")
print(f"Highest Marks  : {highest}")
print(f"Lowest Marks   : {lowest}")
print(f"Students Passed: {pass_count}")
print(f"Students Failed: {fail_count}")

#