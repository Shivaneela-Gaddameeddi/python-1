#recursion is function call itself until satiesfying the base condition
#printing 1 to 10
def display(n):
    if n>10: 
       return
    print(n)
    display(n+1)

display(1)
#printing 10 to 1
#hit is if we want to order 1 to 10 then print() should before if 10 to 1 then print() should be after 
def display(n):
    if n>10: 
        return
    display(n+1)
    print(n)
display(1)
#string into  characters

     
def display(n):
    if n == len(s):
        print()
        return
    print(s[n])
    display(n+1)
s="python programming"  
display(0)
#string into reverse order
def display(n):
    if n == len(s):
        print()
        return
    print(s[n], end=' ')
    display(n+1)
    print(s[n], end=' ')
s="python programming"  
display(0)

#
def display(n):
    if n == len(s):
     return
    print(s[:n+1])
    display(n+1)
    
s="python programming"  
display(0)
#
def display(n,w):
    if n >len(s)-w:
        return
    print(s[n:n+w])
    display(n+1,w)
s= 'codegnan'
display(0,3)
#sum of n number
def display(n):
    if n < 1:
        return 0
    return n + display(n-1)
print(display(10))
#factorial of number **********importent
def display(n):
    if n < 1:
        return 1
    return n * display(n-1)
print(display(6))
#sum of numbers in list
def display(n):
    if n == len(l):
     return 0
    return l[n] + display(n+1)
   
l=[2,3,4,54,6,77,55]