Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"set methods"
'set methods'
s={34,8,40,12,13,50,56,90,29}
s
{34, 8, 40, 12, 13, 50, 56, 90, 29}
sorted(s)
[8, 12, 13, 29, 34, 40, 50, 56, 90]
len(s)
9
max(s)
90
min(s)
8
any(s)
True
all(s)
True
sum(s)
332
s.add(14)
s
{34, 8, 40, 12, 13, 14, 50, 56, 90, 29}
s.updte({12,34,14,64,10})
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s.updte({12,34,14,64,10})
AttributeError: 'set' object has no attribute 'updte'. Did you mean: 'update'?
s.update({12,13,45})
s
{34, 8, 40, 12, 13, 14, 45, 50, 56, 90, 29}
s
{34, 8, 40, 12, 13, 14, 45, 50, 56, 90, 29}
s.pop(14)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    s.pop(14)
TypeError: set.pop() takes no arguments (1 given)
s.pop()
34
s.remove(14)
s
{8, 40, 12, 13, 45, 50, 56, 90, 29}
s.discard(50)
s
{8, 40, 12, 13, 45, 56, 90, 29}
s.clear()
s
set()
a={1,2,3}
a
{1, 2, 3}
b={5,6}
b
{5, 6}
b.add(8)
b
{8, 5, 6}
a
{1, 2, 3}
b=a
a
{1, 2, 3}
c=a.copy()
c.add(14)
c
{1, 2, 3, 14}
a
{1, 2, 3}
"dictonary"
'dictonary'
d={}
d
{}
d={1:1,2:2,3:3}
type(d)
<class 'dict'>
d
{1: 1, 2: 2, 3: 3}
d[1]='int'
d
{1: 'int', 2: 2, 3: 3}
d[1.1]='float'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float'}
#mut dyn ord
d['str']='str'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float', 'str': 'str'}
d[2+4j]='com'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float', 'str': 'str', (2+4j): 'com'}
d[(1,2,3)]='tuple'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float', 'str': 'str', (2+4j): 'com', (1, 2, 3): 'tuple'}
d[False]='bool'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float', 'str': 'str', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d[[1,2]]='list'
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    d[[1,2]]='list'
TypeError: unhashable type: 'list'
d[{1,2}]='set'
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d[{1,2}]='set'
TypeError: unhashable type: 'set'
d[{1:1,2:2}]='dic'
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    d[{1:1,2:2}]='dic'
TypeError: unhashable type: 'dict'
d
{1: 'int', 2: 2, 3: 3, 1.1: 'float', 'str': 'str', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d[1]=1
d
{1: 1, 2: 2, 3: 3, 1.1: 'float', 'str': 'str', (2+4j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d.clear()
d
{}
d[1]=1
d[1.1]=1.1
d[1]=1
d[2]=12.1
d[3]='str'
d[4]=3+4j
d[5]=(1,2,3)
d[6]=[7,6,5]
d[7]={1:2,4:3}
d[8]={1,2}
d[9]=False
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False}
d[10]=1
d[11]=1
d[12]=1
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
"dic operations{"
'dic operations{'
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d[2]
12.1
d[10]
1
d[4]
(3+4j)
d[6]
[7, 6, 5]
d[8]
{1, 2}
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d.get(13)
d.get(17)
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d.get(18)
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d.get(18)
d.get(18,'key is not there')
'key is not there'
d.get(7,'key is not there')
{1: 2, 4: 3}
d.get(90,'key is not there')
'key is not there'
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
'str' in d
False
1 in d
True
12.2 in d
False
12 in d
True
[1,2]  in d
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    [1,2]  in d
TypeError: unhashable type: 'list'
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d[8]='dict'
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1}
d[5]=14
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: 14, 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1}
d.update({1200:1300,1400:1600})
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: 14, 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 1200: 1300, 1400: 1600}
d[13]=100
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: 14, 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 1200: 1300, 1400: 1600, 13: 100}
d[14]=125
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: 14, 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 1200: 1300, 1400: 1600, 13: 100, 14: 125}
d.popitem()
(14, 125)
d.popitem()
(13, 100)
d.pop(4)
(3+4j)
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 5: 14, 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 1200: 1300, 1400: 1600}
del d[7]
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 5: 14, 6: [7, 6, 5], 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 1200: 1300, 1400: 1600}
d.clear()
d
{}
d={1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}d.popitem()
SyntaxError: invalid syntax
d={1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
"dict methods"
'dict methods'
d.keys()
dict_keys([1, 1.1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
d.values()
dict_values([1, 1.1, 12.1, 'str', (3+4j), (1, 2, 3), [7, 6, 5], {1: 2, 4: 3}, {1, 2}, False, 1, 1, 1])
d.items()
dict_items([(1, 1), (1.1, 1.1), (2, 12.1), (3, 'str'), (4, (3+4j)), (5, (1, 2, 3)), (6, [7, 6, 5]), (7, {1: 2, 4: 3}), (8, {1, 2}), (9, False), (10, 1), (11, 1), (12, 1)])
len(d)
13
sorted(d)
[1, 1.1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
min(d)
1
max(d)
12
d
{1: 1, 1.1: 1.1, 2: 12.1, 3: 'str', 4: (3+4j), 5: (1, 2, 3), 6: [7, 6, 5], 7: {1: 2, 4: 3}, 8: {1, 2}, 9: False, 10: 1, 11: 1, 12: 1}
a={1:1,2:2}
b=a
b[3]=3
>>> a
{1: 1, 2: 2, 3: 3}
>>> b
{1: 1, 2: 2, 3: 3}
>>> c=a.copy()
>>> c[4]=4
>>> c
{1: 1, 2: 2, 3: 3, 4: 4}
>>> a
{1: 1, 2: 2, 3: 3}
>>> d= dict.fromkeys(['a','b','c','d','e'],0)
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
>>> d.setdefault('a')
0
>>> d.setdefault('h')
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
>>> d.setdefault('k',1)
1
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> d.setdefault('c',1)
0
>>> d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
>>> s=frozenset({1,2,3,4])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> s=frozenset({1,2,3,4})
>>> s
frozenset({1, 2, 3, 4})
>>> len(s)
4
>>> max(s)
4
>>> min(s)
1
>>> type(s)
<class 'frozenset'>
