
# Accept customer details
customer_name = input("Enter Customer Name: ")
product_name = input("Enter Product Name: ")
price = float(input("Enter Product Price: "))
quantity = int(input("Enter Quantity: "))
membership = input("Enter Membership Type (Regular/Silver/Gold): ").lower()
location = input("Enter Delivery Location (Local/Other City): ").lower()

# Calculate original amount
original_amount = price * quantity

# Calculate membership discount
if membership == "gold":
    membership_discount = original_amount * 10 / 100

elif membership == "silver":
    membership_discount = original_amount * 5 / 100

elif membership == "regular":
    membership_discount = 0

else:
    membership_discount = 0
    print("Invalid Membership Type")

# Calculate additional discount
if original_amount >= 5000:
    additional_discount = original_amount * 5 / 100
else:
    additional_discount = 0

# Calculate final purchase amount after discounts
total_discount = membership_discount + additional_discount
final_purchase = original_amount - total_discount

# Calculate delivery charges
if final_purchase >= 5000:
    delivery_charge = 0

elif location == "local":
    delivery_charge = 50

elif location == "other city":
    delivery_charge = 100

else:
    delivery_charge = 0
    print("Invalid Delivery Location")

# Calculate final payable amount
final_amount = final_purchase + delivery_charge

# Display bill details
print("\n*********** SHOPPING BILL ************")
print(f"Customer Name       : {customer_name}")
print(f"Product Name        : {product_name}")
print(f"Product Price       : Rs. {price:.2f}")
print(f"Quantity            : {quantity}")
print(f"Membership Type     : {membership.title()}")
print(f"Original Amount     : Rs. {original_amount:.2f}")
print(f"Membership Discount : Rs. {membership_discount:.2f}")
print(f"Additional Discount : Rs. {additional_discount:.2f}")
print(f"Total Discount      : Rs. {total_discount:.2f}")
print(f"Delivery Charges    : Rs. {delivery_charge:.2f}")

print(f"Final Payable Amount: Rs. {final_amount:.2f}")

