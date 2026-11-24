#  account details
name = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: "))
amount = float(input("Enter Withdrawal Amount: "))
pin = int(input("Enter ATM PIN: "))

# Correct ATM PIN
correct_pin = 1234

# Validate withdrawal
if pin != correct_pin:
    print("Invalid ATM PIN")

elif amount <= 0:
    print("Invalid Withdrawal Amount")

elif amount > balance:
    print("Insufficient Balance")

elif amount % 100 == 0:
    balance = balance - amount
    print("Withdrawal Successful")

else:
    print("Invalid Amount! Please enter multiples of 100.")


print("\n------ ATM TRANSACTION DETAILS ------")
print(f"Account Holder : {name}")
print(f"Withdrawal Amount : Rs. {amount:.2f}")
print(f"Remaining Balance : Rs. {balance:.2f}")


