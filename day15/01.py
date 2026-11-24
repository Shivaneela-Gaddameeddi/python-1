for row in range(5):
    for col in range(5):
        print(int((row+col)%2==0), end=' ')
    print()    

#true false
for row in range(5):
    for col in range(5):
        print(((row+col)%2==0), end=' ')
    print() 

#01 01
for row in range(5):
    for col in range(5):
        print(col%2, end=' ' ) 
    print() 

# increaing count
c=1          
for row in range(5):
    for col in range(5):
        print(c,end=" ")
        c+=1
    print()  
    

#logic row*col
for row in range(5):
    for col in range(5):
      print((row*col), end=' ')
    print()  

# * parttern
for row in range(5):
    for col in range(row+1):
        print('*', end=' ')
    print()

n = int(input("enter the size: "))
for row in range(5):
    for col in range(n-row):
        print('*', end=' ')
    print()    
