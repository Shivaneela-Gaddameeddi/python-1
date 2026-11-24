def  sumdigits(n):
    sum = 0
    while n>0:
        sum+= n%10
        n //=10
    return sum
print(sumdigits(12344)) 
print(sumdigits(9876))  

#reverse of a number

def   resv(n):
    sum = 0
    while n>0:
        sum+=  (sum*10) + n%10
        n //=10
    return sum
print(resv(12344)) 
print(resv(9876))   