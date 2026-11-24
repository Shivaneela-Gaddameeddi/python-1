#local scope: when we declarering inside only inside  variable not outside.

#global scope:when we declaring globally it will in local and globally
#by using global in side of local scope we get inside and outside.
def display():
    global n
    n=10
    print("Insode function:",n)
display()
print("Outside function:",n)    

#global keyword: global keyword used to when effected outside 
#nonlocal keyword: non local keyword used to when ever no need to effect on inside the function effect on the

def dissplay():
    course="JFS"
    print("Starting course:", course)
    def update():
        nonlocal course
        course="PFS"

        print("updated:", course)
        update()
        print("final course:", course)
display()

#build scop
#never take the built in functions as variable if we take like that it will act as variable it will loose the functionality

s = "codegnan"
print(max(s))
