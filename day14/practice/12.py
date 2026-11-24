n = int(input("Enter the size: "))
m=n//2
for row in range(n):
    for col in range(n):
       if row == 0  or col== n-1 or m<=n-1:
         print("*", end=" ")
    print()

# Right-Angled Triangle using Nested for Loops

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
       
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(j):
        print("*", end=" ")
    print()


# Increasing Number Triangle using for loop

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#Alphabet Triangle Pattern 
n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()




# Multiplication Tables Grid Generator

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for i in range(start, end + 1):

    print(f"\nMultiplication Table of {i}")


    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

    print()

      
