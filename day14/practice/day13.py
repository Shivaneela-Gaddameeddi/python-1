
# Function for Addition
def add(a, b):
    return a + b

# Function for Subtraction
def subtract(a, b):
    return a - b

# Function for Multiplication
def multiply(a, b):
    return a * b

# Function for Division
def divide(a, b):
    return a / b

# Function for Modulus
def modulus(a, b):
    return a % b

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling functions and displaying results
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))

if num2 != 0:
    print("Division:", divide(num1, num2))
    print("Modulus:", modulus(num1, num2))
else:
    print("Division is not possible")
    print("Modulus is not possible")

#2

# Function definition
def display_profile(name, age, city, qualification, profession):

    print(f"Full Name     : {name}")
    print(f"Age           : {age}")
    print(f"City          : {city}")
    print(f"Qualification : {qualification}")
    print(f"Profession    : {profession}")
   



display_profile("Shivaneela", 23, "Telangana",
                "M.Sc Computer Science", "Python Developer")

# Second function call
display_profile("neela", 25, "Hyderabad",
                "B.Tech", "Software Engineer")

# Third function call
display_profile("Priya", 24,  "Hyderabad",
                "M.sc", "python devoloper")

#4

# Function to accept marks
def accept_marks():
    marks = []
    for i in range(5):
        mark = int(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)
    return marks


# Function to calculate total
def calculate_total(marks):
    return sum(marks)


# Function to calculate average
def calculate_average(total):
    return total / 5


# Function to calculate percentage
def calculate_percentage(total):
    return (total / 500) * 100


# Function to calculate grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "Fail"
student_name = input("Enter student name: ")

marks = accept_marks()

total = calculate_total(marks)
average = calculate_average(total)
percentage = calculate_percentage(total)
grade = calculate_grade(percentage)

# Display result report
print("\n STUDENT RESULT REPORT")
print(f"Student Name : {student_name}")
print(f"Subject Marks: {marks}")
print(f"Total Marks  : {total}/500")
print(f"Average      : {average}")
print(f"Percentage   : {percentage}%")
print(f"Final Grade  : {grade}")

#6

# Function to check prime number
def check_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# Function to calculate factorial
def calculate_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


# Function to find factors
def find_factors(n):
    factors = []

    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    return factors


# Function to check even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a non-negative number.")
else:
    # Calling all functions
    prime = check_prime(num)
    factorial = calculate_factorial(num)
    factors = find_factors(num)
    result = check_even_odd(num)

 

    if prime:
        print(f"{num} is a Prime Number")
    else:
        print(f"{num} is Not a Prime Number")

    print(f"Factorial of {num} = {factorial}")
    print(f"Factors of {num} = {factors}")
    print(f"{num} is an {result} Number")

# 7
#creating acccount
def display_create_account(name,  city, id ):

    print(f"Full Name     : {name}")
    print(f"city           : {city}")
    print(f"id : {id}")

# Function to create a bank account
def create_account():
    name = input("Enter customer name: ")
    account_number = input("Enter account number: ")
    mobile = input("Enter mobile number: ")

    balance = float(input("Enter initial balance: "))

    if balance < 0:
        print("Initial balance cannot be negative!")
        return None

    account = {
        "name": name,
        "account_number": account_number,
        "mobile": mobile,
        "balance": balance
    }

    print("\nAccount created successfully!")
    return account


# Function to deposit money
def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be greater than zero!")
    else:
        account["balance"] += amount
        print("Amount deposited successfully!")


# Function to withdraw money
def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be greater than zero!")
    elif amount > account["balance"]:
        print("Insufficient balance!")
    else:
        account["balance"] -= amount
        print("Amount withdrawn successfully!")


# Function to check balance
def check_balance(account):
    print(f"Available Balance: Rs.{account['balance']:.2f}")


# Function to display account details
def display_account_details(account):
    print("\n========== ACCOUNT DETAILS ==========")
    print(f"Customer Name  : {account['name']}")
    print(f"Account Number : {account['account_number']}")
    print(f"Mobile Number  : {account['mobile']}")
    print(f"Account Balance: Rs.{account['balance']:.2f}")
 


# Main program
account = create_account()

if account is not None:

    while True:
        print("\n BANKING MENU ")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Display Account Details")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            deposit(account, amount)

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            withdraw(account, amount)

        elif choice == "3":
            check_balance(account)

        elif choice == "4":
            display_account_details(account)

        elif choice == "5":
            print("\nThank you for using our banking system!")
            break

        else:
            print("Invalid choice! Please try again.")

    # Final account summary
    print("\n FINAL ACCOUNT SUMMARY ")
    display_account_details(account)

#8 Online Shopping Bill Generator Using Multiple Functions 



        