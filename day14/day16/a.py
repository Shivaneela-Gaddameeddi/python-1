n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 and j > 0 and j < n-1 or i == m or j == 0 and i > 0 or j == n-1 and i > 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#b
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or i == m or i == n-1 or (j == n-1 and i != 0 and i != m and i != n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#c
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i ==n-1 or j == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    

#D
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n-1) or (i == n-1 and j < n-1) or (j == n-1 and i > 0 and i < n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()  
#E
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == m or i == n-1 or j == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 

#F
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == m or j == 0:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#H
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i == m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#i
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    
#j
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if (i == 0 and j >= m) or j == n-1 or (i == n-1 and j <= m) or (j == 0 and i >= n-2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()    
#k
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or (i <= m and j == n-1-2*i) or (i >= m and j == 2*(i-m)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#l
n = int(input("Enter the size: "))

for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#m
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= m) or (i+j == n-1 and i <= m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#n   
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or i== j: 
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
#o
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if (i == 0 or i == n-1) and j > 0 and j < n-1 or (j == 0 or j == n-1) and i > 0 and i < n-1:
            print('*', end=' ')
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print() 
#P
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n-1) or (i == m and j < n-1) or (j == n-1 and i > 0 and i < m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#Q
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if ((i == 0 or i == n-1) and j > 0 and j < n-1) or ((j == 0 or j == n-1) and i > 0 and i < n-1) or (i == j and i > m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#R
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if j == 0 or (i == 0 and j < n-1) or (i == m and j < n-1) or (j == n-1 and i > 0 and i < m) or (i == j and i > m):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
#S
n = int(input("Enter the size: "))
m = n // 2

for i in range(n):
    for j in range(n):
        if ((i == 0 or i == n-1) and j > 0 and j < n-1) or i == m or (j == 0 and i > 0 and i < m) or (j == n-1 and i > m and i < n-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

