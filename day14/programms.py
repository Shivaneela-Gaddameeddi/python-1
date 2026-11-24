#using while loop
l=[12,9,3,4,5,2,4,5]

i=0
j=len(l)-1
while i<=j:
    if i==j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1
# DMART bill process


bill=0
while True:
    product=input('Enter the product name(STOP):') 
    if product=='STOP':
        print('Total bill:',bill)
        break
    price=int(input('Enter the price:'))
    quantity=int(input('Enter the quantity:'))
    bill+=price*quantity

#
product={'salt':45,'red grain':60,'sugar':55,'cold drinks':80,'pulses':75}
print('Welcome to the store'.center(50,'-'))
print('Product Name','Price')
for i in product:
    print(i.ljust(12,' '),':',product[i])
carts={}
while True:
    cart=input('Enter the Product Name(EXIT):').lower()
    if cart=='exit':
        break
    qua=int(input('Enter the quantity:'))
    carts[cart]=qua
print('Bill'.center(50,'-'))
print('Product Name Quantity Price(Rs)')
bill=0
for i in carts:
    print(i.ljust(12,' '),str(carts[i]).ljust(12,' '),product[i])
    bill+=carts[i]*product[i]     
print(f'Total bill: Rs{bill}')
print('Thanks for Shopping'.center(50,'-'))




