
def   resv(n):
    sum = 0
    while n>0:
        sum =  (sum*10) + n%10
        n //=10
    return sum
print(resv(12344)) 
print(resv(9876))  

#types of functions
#-positional arguments
def display(name,email,password):
    print("name",name)
    print("emial",email)
    print("pass",password)
display("abc","abc@gmail.com","abc@123")
display("abc@gmail.com","abc","abc@123")
display("abc@123","abc@gmail.com","abc")    
