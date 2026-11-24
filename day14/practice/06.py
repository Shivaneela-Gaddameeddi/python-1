# Employee Bonus Eligibility System
emp_name = input("Enter Employee Name: ")
salary = float(input("Enter Employee Salary: "))
experience = int(input("Enter Years of Experience: "))
rating = int(input("Enter Performance Rating (1-5): "))

# Calculate bonus percentage
if experience >= 5 and (rating == 4 or rating == 5):
    bonus_percentage = 20

elif experience >= 3 and rating >= 3:
    bonus_percentage = 10

else:
    bonus_percentage = 5

# Calculate bonus amount
bonus_amount = salary * bonus_percentage / 100

# Calculate final salary
final_salary = salary + bonus_amount

# Display employee details
print("\n------ EMPLOYEE BONUS DETAILS ------")
print(f"Employee Name       : {emp_name}")
print(f"Employee Salary     : Rs. {salary:.2f}")
print(f"Years of Experience : {experience}")
print(f"Performance Rating  : {rating}")
print(f"Bonus Percentage    : {bonus_percentage}%")
print(f"Bonus Amount        : Rs. {bonus_amount:.2f}")
print(f"Final Salary        : Rs. {final_salary:.2f}")
print("------------------------------------")





