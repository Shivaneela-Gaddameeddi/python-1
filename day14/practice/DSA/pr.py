numbers = [12, 3, 4, 34]
largest = numbers[0]
for i in numbers:
  if i > largest:
    largest = i
print("Largest element:", largest)   

#smallest 
numbers = [2, 3, 13, 43, 1]
smallest = numbers[0]
for i in numbers:
  if i < smallest:
    smallest = i
print("smallest element:", smallest)    

# count even or odd 
numbers = [2, 3, 4, 5, 16, 12]
even = []
for i in numbers:
  if i % 2==0:
    even.append(i)
    print(" even number:", even)
  


    