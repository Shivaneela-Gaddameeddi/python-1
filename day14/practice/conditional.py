num = int(input("Enter a number: "))

if num > 0:
    print("The number is Positive")

elif num < 0:
    print("The number is Negative")

else:
    print("The number is Zero")


num = int(input('Enter the number:'))
if num > 0:
    print("The number is even")
elif num < 0:
    print("The number is odd")  
else:
          print("The number is zero")

# voting eligibility
name = str(input('enter the name:'))
age = int(input("enter the age:"))
country = str(input('Enter the country:'))
if age > 18:
     print("You are eligible to vote")
elif age < 18:
     print("You are not eligible to vote") 


# student grade calculations system
name = str (input("enter the Student name:"))
marks = list(map(int,input().split()))
total=sum(marks)
percentage=(total/(len(marks)*100))*100
print("name of the student")
print("marks of the student")
print("percentage of the student")    
if percentage >= 90:
     print("grade a")
else:
     print("grade b")
     
if percentage < 70:
     print("grade c")

else:
     print("grade d")

       