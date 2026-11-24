bill=0
while True:
    product=input('Enter the product name(STOP):') 
    if product=='STOP':
        print('Total bill:',bill)
        break
    price=int(input('Enter the price:'))
    quantity=int(input('Enter the quantity:'))
    bill+=price*quantity

#Employee details
emp_id = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))

hra = basic_salary * 20 / 100     
da = basic_salary * 10 / 100      
gross_salary = basic_salary + hra + da

# Display salary details

print("       EMPLOYEE SALARY DETAILS")
print("*" * 40)
print(f"Employee ID   : {emp_id}")
print(f"Name          : {name}")
print(f"Department    : {department}")
print("-" * 40)
print(f"Basic Salary  : {basic_salary:10.2f}")
print(f"HRA (20%)     : {hra:10.2f}")
print(f"DA (10%)      : {da:10.2f}")
print("-" * 40)
print(f"Gross Salary  : {gross_salary:10.2f}")
print("=" * 40)

##
std_id = int(input("Enter student  ID: "))
name = input("Enter Employee Name: ")
department = input("Enter Department: ")

