#checking prime or not
def factors(n):
    for i in range(2,n//2+1):
        if n%i==0:
            return"not a prime number"
        return" is prime number"
print(factors(int(input("enter a number: ")))) 

def factors(n):
    c=0
    for i in range(n):
        if n%i==0:
         c+=1
        if c>2:
            print("not prime number")    
        else:
            print("prime number")

factors(int(input("enter the number: ")))                

