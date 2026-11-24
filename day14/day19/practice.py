def power(a, b):
    if b == 0:
        return 1

    else:
        return a * power(a, b - 1)
a = int(input('enter the base:'))
b = int(input('enter the exponent: ')) 
result =  power(a, b)   
print('power of a number:', result)
#multiplicate table
def table(n, i):

    if i > 10:
        return

    print(n, "x", i, "=", n * i)

    table(n, i + 1)


n = int(input("Enter a number: "))
table(n, 1) 
#fibanocci series
def fib(n):
    if n == 0:
       return 0
    elif n == 1:
            return 1 
    else:
      return fib(n-1) + fib(n-2)
n=int(input("enter the number: "))
for i in range(n):
    print(fib(i), end=' ')
#polidrone
def reverse_num(n, rev):
    if n == 0:
        return rev
    digit = n % 10
    rev = rev * 10 + digit
    return reverse_num(n//10, rev)
num = int(input("enter a number: "))
reverse = reverse_num(num, 0)
if num == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number") 

"""Find GCD of Two Numbers

    Find the Greatest Common Divisor using recursion.

Example: gcd(12, 18) → 6  """
