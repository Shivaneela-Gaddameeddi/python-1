#int float str list tuple set dict bool
#int float str tuple bool
#list set dict
#when passing immutable items it won't effect the outside of the function
#when passing the mutable items it will be effect on out side of the function also.
#int
def display(n):
    n += 10
    print("Inside function:",n)

n = 10 
display(n)
print("Outside function:",n)   
#float
def display(n):
    n+=10.3
    print("Inside function:",n)
n = 10.3
display(n)
print("Outside function:",n)    
#str
def display(n):
    n="python"
    print("Inside function:",n)
n = "programming"  
display(n)
print("Outside function:",n)  
#set
def display(n):
    n.append(5,6,7)
    print("Inside function:",n)
n = (2,3,4)
print("Outside funcion:",n)    
#list
def display(n):
    n=[5,6,7]
    print("Inside function:",n)
n=[6,7,8]
print("Outside function:",n)    