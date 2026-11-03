batterycharge = int(input("Enter the battery: "))

if batterycharge<20:
           print(f'Battery is low:{batterycharge}, charge your phone')

bill = int(input("Enter the bill: "))
status = eval(input("is it raining?" ))

if status:
    bill+=30
    print("Eextra Delivery chargers applied")

print(f"Final Bill: {bill}")        

product =input('Enter product:')
beestseller=eval(input('Enter status:'))
if beestseller:
        print(f'{product} is best seller.' )