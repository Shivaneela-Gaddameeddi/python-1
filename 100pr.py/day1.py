#reverse string
s ="Holla"
print(s[::-1])

#string polidrome
s = "noon"
print(s==s[::-1]) 

s = "black"
print(s==s[::-1])

def is_polindrome(s):
    cleaned = " ".joined (c.lower() for c in s if c.isalnum ())
    return cleaned == cleaned[::-1]


n = 4
fact = 1 
for i in range(1, n+1): 
 fact*= i 
print(fact) 

#largest num in 
num = [2, 5, 8, 6, 9]
print(max (num) )

num = [2, 5, 8, 6, 9]
print(min (num) )

num = [8, 7, 3, 6, 11]
print(sorted(set(num)) [-2])