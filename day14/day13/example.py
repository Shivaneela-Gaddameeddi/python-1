l = [2,4,5,8,30,9,6,41,37,90]
search = int(input("enter the number:"))

for i in range(len(l)):
    if l[i] == search:
        print(f"{search} is found at {i}")
        break

else:
    print(f"{search} is not found at {i}")    
