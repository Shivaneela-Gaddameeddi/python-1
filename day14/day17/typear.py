#types of functions

#- positional arguments
def display(name,email,password):
    print("name",name)
    print("emial",email)
    print("pass",password)
display("abc","abc@gmail.com","abc@123")
display("abc@gmail.com","abc","abc@123")
display("abc@123","abc@gmail.com","abc")  

#- Key word arguments
def display(name,email,password):
    print("name",name)
    print("emial",email)
    print("pass",password)
display(name="abc",email="abc@gmail.com",password="abc@123")
display(email="abc@gmail.com",name="abc",password="abc@123")
display(password="abc@123",email="abc@gmail.com",name="abc") 

# -default argument

def display(name,email,password,phonenumber=None):
    print("name",name)
    print("emial",email)
    print("password",password)
    print("phonenumber",phonenumber)
display(name="abc",email="abc@gmail.com",password="abc@123")
display(name="abc",email="abc@gmail.com",password="abc@123",phonenumber=9987654321)

# -variable lenth argument
def display(*n):
    print(n)

display(1,2,3,4,5)
display(1,2,3)
display(1,2,3,4)   

#- passing key word arguments
def display(**n):
    print(n)
display(n1=1,n2=2,n3=3,n4=4)
display(n1=1,n2=2,n3=3) 
display(n1=1,n2=2)  

#----
