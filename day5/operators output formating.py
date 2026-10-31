Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
"BITWISE OPERATOR"
'BITWISE OPERATOR'
5&14
4
11&12
8
8|3
11
11|122
123
11|12
15
8|9
9
11^12
7
12^11
7
2<<2
8
2<<3
16
2<<5
64
15>>1
7
15>>4
0
15>>2
3
15>>6
0
~20
-21
~90
-91
~50
-51
~43
-44
~34
-35
a = input("enter the string:")
enter the string:sdfg
a
'sdfg'
a = input()
a
432
432
type(a)
<class 'str'>
a = inpt(input())
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a = inpt(input())
NameError: name 'inpt' is not defined. Did you mean: 'input'?
a = int(input))
SyntaxError: unmatched ')'
a = int(intput())
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    a = int(intput())
NameError: name 'intput' is not defined. Did you mean: 'input'?
a =
SyntaxError: invalid syntax
a = input()
a
234
234
a = int(input("enter the integer:"))
enter the integer:23
a
23
a = float (float("enter the float:"))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    a = float (float("enter the float:"))
ValueError: could not convert string to float: 'enter the float:'
a = float (input("enter the float:"))
enter the float:34
a
34.0
a = list  (input())
23 45
a
['2', '3', ' ', '4', '5']
map(int ,a)
<map object at 0x000001C829E53CA0>
list (map(int, a))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    list (map(int, a))
ValueError: invalid literal for int() with base 10: ' '
map(int, a)
<map object at 0x000001C829EBCE80>
list (map(int, a))
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    list (map(int, a))
ValueError: invalid literal for int() with base 10: ' '
a = list(map(int,input().split()))
1 3 4 43 23 45
a
[1, 3, 4, 43, 23, 45]
a = list(map(float, input().split()))
a
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    a = list(map(float, input().split()))
ValueError: could not convert string to float: 'a'
a = list(map(float, input().split()))
23 21 3 4 5.6 8.64
a
[23.0, 21.0, 3.0, 4.0, 5.6, 8.64]
a = tuple(map(int, input().split()))
34 5 65 1 2
a
(34, 5, 65, 1, 2)
a,b,c = list(map(int,input().split()))
123
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a,b,c = list(map(int,input().split()))
ValueError: not enough values to unpack (expected 3, got 1)
1 2 3
SyntaxError: invalid syntax
a,b,c = list(map(int, intput().split()))
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c = list(map(int, intput().split()))
NameError: name 'intput' is not defined. Did you mean: 'input'?
a,b,c = list(map(int, input().split()))
1 2 3
a
1
b
2
c
3
a,b,c = list(map(float, input().split()))
23.4 34.1 5 6
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    a,b,c = list(map(float, input().split()))
ValueError: too many values to unpack (expected 3)
a,b,c = list(map(float, input().split()))
1 2 3
a
1.0
b
2.0
c
3.0
email,password = input().split()
sowmya@coodegnen
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    email,password = input().split()
ValueError: not enough values to unpack (expected 2, got 1)
email,password = input().split()
sam@gmail.com 3567
email
'sam@gmail.com'
password
'3567'
a = eval(input())
[1,2,3,4]
a
[1, 2, 3, 4]
a = eval(input())
"sdwe"
a
'sdwe'
a = eval(input())
(1,2,3)
a
(1, 2, 3)
a = eval(input())
2.3 1.3 4.1 9.0
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    2.3 1.3 4.1 9.0
        ^^^
SyntaxError: invalid syntax
a = eval(input())
(2.3 3.1)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a = eval(input())
  File "<string>", line 1
    (2.3 3.1)
     ^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
a = eval(input())
[2,4,5]
a
[2, 4, 5]
a = eval(input())
"wmkl"
a
'wmkl'
a = eval(input())
{1:2,2:2,3:1}
>>> a
{1: 2, 2: 2, 3: 1}
>>> a = eval(input())
2+5j
>>> a
(2+5j)
>>> a=10
>>> b=20
>>> c="codegnan"
>>> a
10
>>> b
20
>>> c
'codegnan'
>>> print(a,b,c)
10 20 codegnan
>>> print(b,a,c)
20 10 codegnan
>>> print("a=",a,"b",b,"c",c)
a= 10 b 20 c codegnan
>>> print("a=",a,"b",b,"c",c,sep='')
a=10b20ccodegnan
>>> print("a=",a,"b",b,"c",c,sep='-')
a=-10-b-20-c-codegnan
>>> print("a=",a,"b",b,"c",c,end='\n\n')
a= 10 b 20 c codegnan

>>> print("a=",a,"b",b,"c",c,end='@')
a= 10 b 20 c codegnan@
>>> print(f'a={a} b={b}')
a=10 b=20
>>> print('a=%d b=%f '%(a,b))
a=10 b=20.000000 
>>> print('a={} b={}' .format(a,b))
a=10 b=20
>>> print('a={} b={}' .format(b,a))
a=20 b=10
