#lambda is sigle line  without functions and 
# var = lamda args: #sts 
#conditional using lambda
sot = lambda a,b,c:a+b+c
print (sot(10,30,45))

#-gst
gst=lambda price: price+ price *0.18
print(gst(2000))

#-avg
avg = lambda l: sum(l)/len(l)
l=[22,32,43,31,42,55]
print(avg(l))

#-iseven
iseven= lambda n: "even"if n%2==0 else "odd"
print(iseven(55))
print(iseven(50))

#-isovel
isovel = lambda ch:"vowel"if ch in "aeiouAEIOU" else "consonant"
print(isovel('p'))
print(isovel('i'))

#-product 
check = lambda data, pro:(f"product price: {data[pro]['price']})" if data[pro]["stock"]>0 else "out of stock") if pro in data else "product is unavailable"
data ={ 
    "apple":{"stock":10,"price":17},
    "banana":{"stock":78,"price":78},
    "mango":{"stock":0,"price":65},
    "coconut":{"stock":30,"price":50}
    }
print(check(data,'mango'))
#Loops using lambda
'''def addten(l):
    for i in range(len(l)):
        l[i]+=10
    return l
l=[9,2,4,5,56,43,32]
print(addten(l))

def domain(d):
    for i in range(len(d)):
        d[i] = (d[i].slipt('@')).slipt('.')[0]
    return d
d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
print(domain(d))'''
#Map function - used to each and every value
#-addten
l=[9,2,4,5,56,43,32]
addten = list(map(lambda i:i+10 , l))
print(addten)
#-domain
d=['xyz@codegnan.com','abc@gmail.com','pqr@yahoo.com']
domain = list(map(lambda i:(i.split('@')[1]).split(',')[0],d))
print(domain)
#-upper
c = ['asdfg', 'tyui', 'hjkde']
cu = list(map(lambda i:i.upper(),c))
print(cu)
#-gst
d = {'a':20, 'b':30, 'c':1000, 'd':5000, 'e':2000}
gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
print(gst)

#Filter functions - used to based on condition

l=[1,2,3,42,5,65,7,87]
even = list(filter(lambda i:i%2==0,l))
print(even)

a=['a', 'd', 'i', 'e', 'o', 'k','j', 'l']
vowels = list(filter(lambda i:i in 'aeiouAEIOU',a))
print(vowels)

#Reduce - used to
from functools import reduce
l=[1,3,4,6,7,2,8]
sumofl= reduce(lambda sum,i:sum+i,l)
print(sumofl)

from functools import reduce
l=[1,3,4,6,7,2,8]
sumofl= reduce(lambda sum,i:sum*i,l)
print(sumofl)

from functools import reduce
l=[1,3,45,6,72,29,8]
maxofl= reduce(lambda max,i:max if max>i else i,l)
print(maxofl)

from functools import reduce
l=[7,9,45,6,72,29,8]
maxofl= reduce(lambda max,i:max if max<i else i,l)
print(maxofl)

