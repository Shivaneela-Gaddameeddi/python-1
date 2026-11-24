
#product of numbers using recursion
def display(n):
    if n < 1:
        return 1
    return n * display(n-1)
print(display(5))
#sum  using recursion
def sumof(n):
    if n <= 0:
        return 0
    return n + display(n)
print(sumof(5))
#pass by  value pass by reference
#integer
def display(n):
    n += 10
    print("Inside function:",n)

n = 10 
display(n)
print("Outside function:",n) 

#passing string
def modify_string(s):
    s = s + " Python"
    print("Inside function:", s)


name = "programming"

modify_string(name)



#list using pass
def display(n):
    n=[5,6,7]
    print("Inside function:",n)
    n=[6,9,8]
print("Outside function:",n)    
#dic using pass

def modify_dictionary(data):
    data["city"] = "Hyderabad"
    print("Inside function:", data)


student = {
    "name": "Shiva",
    "age": 2
}

print("\nBefore function call:", student)
modify_dictionary(student)
print("After function call:", student)

#fibonacci series

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
#power using recursion

def power(a, b):
    if b == 0:
        return 1

    else:
        return a * power(a, b - 1)
a = int(input('enter the base:'))
b = int(input('enter the exponent: ')) 
result =  power(a, b)   
print('power of a number:', result)

#7 palindrome number
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
####


  