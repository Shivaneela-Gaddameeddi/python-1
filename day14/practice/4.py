# student grade calculations system
name = str (input("enter the Student name:"))
marks = list(map(int,input("enter marks").split()))
total=sum(marks)
percentage=(total/(len(marks)*100))*100
print("name of the student",name)
print("marks of the student",marks)
print("percentage of the student",percentage)    
if percentage >= 90:
     print("grade a")
elif percentage < 80:
     print("grade b")
     
elif percentage < 70:
      print("grade c")