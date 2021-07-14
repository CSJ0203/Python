#multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)

a = "Apple is A Banna is B"
print(len(a))
print(a[4])

a = "Apple is A Banna is B Cheese is C Delete is D"
print(a[3])
print(a[7])
print(a[-2])
print(a[-1])
print(a[0]+a[1]+a[2]+a[3]+a[4])
print(a[0:5])

a = "20010331Rainy"
year = a[:4]
date = a[4:8]
weather = a[8:]
print(year)
print(date)
print(weather)

a = 'Pithon'
a[:1]
print(a[:1])
print(a[2:])
print(a[:1] + 'y' + a[2:])

# 문자열 포매팅 아래 문장에서 %3의 경우를 포맷코드라 칭함
a = "I eat %s apples." %"five"
print(a)

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." %(number, number)
print(a) # %s는 졸라 똒똑하다.... 걍 아무거나 다 치환해서 넣을수가 이따

test = "Error is %d%%." %98
print(test)

a = "I eat {0} apples".format(3)
print(a.lower())

a = [1,2,3,4,5]
print(a[0]+a[2])
print(a[-1])

a=[1,2,3,['a','b','c']]

print(a[0])
print(a[-1])
print(a[3])
print(a[-1][0])
print(a[-1][1])

a = [1, 2, ['a','b',['Life','is']]]
print(a[2][2][0])

a = [1,2,3,4,5]
len(a)

a.append(6)
print(a)

b = [1,3,6,2,7]
b.sort();

a = ['a','b','c']
a.reverse();
print(a)

a = [1,2,3]
print(a.index(2))

a = [1,2,3]
a.insert(0,4)
print(a)
a = [1,2,3]
a.pop()
print(a)

t1 = (1,2,'a','b')
t2 = (3,4)
t3 = (5,6)

t4 = (1.,2,'a','b')
print(len(t4))

dic = {'name':'pey', 'phone':'01011112222', 'birth': '1118'}
print(dic)

a = {1:'a'}
a[2] = 'b'
a['name'] = 'pey'
a[3] = [1,2,3]
print(a)

del a[1]
print(a)

grade = {'pey' : 10, 'jully' : 99}
print(grade['pey'])

a = {'name' : 'pey', 'phone' : '01011112222', 'birth' : '1995'}
print(a.keys())

print(a.items())
print(a.values())

for k in a.keys():
    print(k)

print(list(a.keys()))
 
b = {'name' : 'pey', 'phone' : '01011114444', 'birth' : '1118'}

print(b.get('name'))
b.get('foo','bar')
print(b.get('bar'))
print('name' in b)

s1 = set([1,2,3])
print(s1)

s2 = set("hello")
print(s2)

s3 = set([1,2,3,4])
l3 = list(s3)
print(l3)
print(l3[1])

t4 = tuple(s3)
print(t4)

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

print(s1 & s2)

print(s1.intersection(s2))

print(s1 | s2)

s1 = set([1,2,3])
s1.add(4)
print(s1)

s1 = set([1,2,3])
s1.update([4,5,6])
print(s1)

s1 = set([1,2,3])
s1.remove(2)
print(s1)

a = True
b = False
print(type(a))

print(1==1)

a = [1,2,3,4]
while a:
    print(a.pop())

bool ('python')
print(bool ('python'))

print(bool(''))

print(bool([1,2,3]))

a = [1,2,3]
b = a
print(b)

print(id(a))
print(id(b))

print(a is b)

a[1] = 4
print(a)
print(b)

b = a[:]
a[1] = 4

from copy import copy
a = [1,2,3]
b = copy(a)

print(b is a)

a = [1,2,3]
b = a.copy()

print(b)

a,b = ('python', 'life')
print(a,b)

[a,b] = ['pyhon','life']
print([a,b])

a = b = 'python'
print(a, b)

print(1 % 2)

a = 80
b = 75
c = 55
print((a+b+c)/3)

print(13%2)

a = "881120-1068234"
yyyymmdd = a[:6]
print(yyyymmdd)
num = a[7:]
print(num)

a = 33242*6
b = 30400
print(a+b/7)

a = "a:b:c:d"
b = a.replace(":","#")
print(b)

a = [1,3,5,4,2]
a.sort()
a.reverse()
print(a)

a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)

a = (1,2,3)
a = a + (4,)
print(a*2)

a = "가나다"
print(a*2)

a = {1,2,3}
print(id(a))

a = a + (4,)
print(a)