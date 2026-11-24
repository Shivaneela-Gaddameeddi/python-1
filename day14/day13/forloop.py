# sdlr
pin=1234

for i in range(5):
    epin = int(input("Enter the pin:"))
    if epin == pin:
       print("login successfull")
       break
    else:
        print("invalid pin")


else:
    print("max attemps reached ! try after 30 seconds ")    
