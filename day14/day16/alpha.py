
n = int(input('Enter the size: '))
m= n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1 or i==m or j==m:
            print('*', end=' ')
    else:
        print(' ',end=' ')

    print()

n = int(input('Enter the size: '))
m= n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==1  or j==1 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
            print('*', end=' ')
    else:
        print(' ',end=' ')

    print()


n = int(input('Enter the size: '))
m= n//2
for i in range(n):
    for j in range(n):
        if i==0 or j==m  or (i==n-1 and j<=m) or (j==0 and i>=m):
            print('*',end=' ')
    else:
        print(' ',end=' ')

    print()    
# M
n = int(input("enter the size: "))
m= n//2
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()                

