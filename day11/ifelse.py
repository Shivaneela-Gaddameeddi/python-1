data = ('admin@gmail.com','admin@123')
gmail =input("Enter the mail:")
password =input('Enter the password:')

if (gmail,password) ==data:
     print("Login successful")
else:
     print("Invalid  Login")

     seats ={
          's1':'Booked',
          's2':'Available',
          's3':'Available',
          's4':'Available',
          's5':'Booked',
          's6':'Available'
     }

     seatno = input("Enter the seatno(sn): ")

     if seatno in seats and seats[seatno] == 'Available':
          seats[seatno] = 'Booked'
          print(f'{seatno} is booked successfully')
          print(seats)
     else:
          print(f'{seatno} is already booked')


