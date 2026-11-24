email=list(map(str,input().split()))
for i in email:
    if i.count('@')!=1:
        print(f"Invalid Email:{i}")
    else:
        first_part,second_part=i.split('@')
        print(second_part)

        secret_number=25
i=0
while True:
    l=int(input())
    if l==secret_number:
        print("Correct guess")
        break
    elif l<secret_number:
        print("too low")
    else:
        print("too high")