n = int(input("Enter the size: "))
for row in range(n):
    for sp in range(n-row):
        print(' ', end=' ')
    for col in range(row+1):    
        print('*' ,end=' ')

print()


n = int(input("Enter the size: "))
for row in range(n):
   for sp in range(n-1-row):
        print(' ', end=' ')
   for col in range(n-row):    
        print('*' ,end=' ')
   
   print() 
#another way
n = int(input("Enter the size: "))
m= n//2
for row in range(n):
   if  row <= m:
       for col in range(row+1):    
          print('*' ,end=' ')
   else:
       for col in range(n-row):
           print('*' ,end=' ')
   print() 
#another way
n = int(input("Enter the size: "))
m= n//2
for row in  range(n):
    if row <= m:
        print('* '*(row+1))
    else:
        print('* '*(n-row))    
#another way
n = int(input("Enter the size: "))
m= n//2
for row in  range(n):
    print('* '*(row+1) if row <= m else '* '*(n-row))



n = int(input("Enter the size: "))
for i in  range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print('*',end=' ')
        else:
            print('* ',end=' ') 

    print()          

n = int(input('Enter the size: '))
m= n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m or j==m or i+j==n-1 :
            print('*', end=' ')
    else:
        print(' ',end=' ')

    print()    


