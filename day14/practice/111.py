n = int(input("enter the positive number:"))
for  i in range(1, n+1):
     print(i)
while i <= n:
    print(i)
    i = i + 1      
#table of 5
n = int(input("enter the  number: "))
for i in range(1, 21):
    print(f"{n} x {i} = {n * i}")

#sum and average numbers
n = int(input("Enter a positive number: "))

total = 0
count = 0
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):

    total = total + i
    count = count + 1

    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

average = total / count
print(f"Sum of numbers : {total}")
print(f"Average        : {average:.2f}")
print(f"Count          : {count}")
print(f"Sum of even    : {even_sum}")
print(f"Sum of odd     : {odd_sum}")

#student marks analysis system
n = int(input(enter the ))
  