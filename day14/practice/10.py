
# Employee Attendance and Payroll Validation System

# Accept number of employees
n = int(input("Enter number of employees: "))

# Create an empty list
employees = []

# Accumulator variables
total_salary = 0
valid_count = 0
invalid_count = 0

# Process each employee
for i in range(n):

    print(f"\nEnter Details of Employee {i+1}")

    try:
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        salary = float(input("Enter Monthly Salary: "))
        working_days = int(input("Enter Working Days: "))
        present_days = int(input("Enter Days Present: "))

        # Validate employee data
        assert salary > 0, "Salary must be greater than zero"
        assert working_days > 0, "Working days must be greater than zero"
        assert present_days >= 0, "Present days cannot be negative"
        assert present_days <= working_days, "Present days cannot exceed working days"

        # Calculate attendance percentage
        attendance = (present_days / working_days) * 100

        # Calculate payable salary
        daily_salary = salary / working_days
        payable_salary = daily_salary * present_days

        # Store valid employee details in dictionary
        employee = {
            "ID": emp_id,
            "Name": emp_name,
            "Salary": salary,
            "Working Days": working_days,
            "Present Days": present_days,
            "Attendance": attendance,
            "Payable Salary": payable_salary
        }

        # Add dictionary to list
        employees.append(employee)

        # Update accumulator variables
        total_salary += payable_salary
        valid_count += 1

    except AssertionError as e:
        print(f"Invalid Employee Data: {e}")
        invalid_count += 1
        continue

# Display payroll report
print("\n========== EMPLOYEE PAYROLL REPORT ==========")

for emp in employees:
    print(f"\nEmployee ID       : {emp['ID']}")
    print(f"Employee Name     : {emp['Name']}")
    print(f"Monthly Salary    : Rs. {emp['Salary']:.2f}")
    print(f"Working Days      : {emp['Working Days']}")
    print(f"Days Present      : {emp['Present Days']}")
    print(f"Attendance        : {emp['Attendance']:.2f}%")
    print(f"Payable Salary    : Rs. {emp['Payable Salary']:.2f}")

print("\n============== SUMMARY ==============")
print(f"Total Employees   : {n}")
print(f"Valid Employees   : {valid_count}")
print(f"Invalid Employees : {invalid_count}")
print(f"Total Payroll     : Rs. {total_salary:.2f}")
print("=====================================")
