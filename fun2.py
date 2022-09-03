#Задача 1
def a(x):
    return len(str(abs(x)))
n=int(input('Число:'))
print('разрядов:',a(n))

#Задача 2
import math
a=input('1-круг,2-треугольник,3-прямоугольник:')
if a=='1':
    def S():
        return math.pi*r**2
    r=float(input('Радиус:'))
    print('площадь=',S())
elif a=='2':
    def S2():
        return 0.5*b*h
    b=float(input('Сторона:'))
    h=float(input('Высота:'))
    print('площадь',S2())
elif a=='3':
    def S3():
        return a*b
    a=float(input('длинна:'))
    b=float(input('ширина:'))
    print('площадь',S3())
else:
    print('Неверно')

#Задача 3
import random
def mas():
    a=list()
    b = int(input('От:'))
    c = int(input('До:'))
    while len(a)<10:
        a.append(random.randint(b,c))
    print(a)
mas()

#Задача 4
k=int(input('Введите кол-во секунд:'))
def sek():
    b=k//86400
    n=k-(b*86400)
    c=n//3600
    n=n-(c*3600)
    d=n//60
    e=n-(d*60)
    return 'дней',b,'часов',c,'минут',d,'секунд',e
print(sek())

#Задача 5
a=input('Строка:')
def coun():
    gl=0
    sog=0
    for i in a:
        if i in 'eyuioa':
            gl+=1
        else:
            sog+=1
    return 'г',gl,'c',sog
print(coun())

#Задача 6
a=int(input('Введите число:'))
def sw():
    b=str(a)*2
    c=str(a)*3
    e=a+int(b)+int(c)
    return e
print(sw())

#Задача 7
def a(x):
    if type(x) == tuple:
        for i in x:
            print(i,'-Длинна:',len(i))
    elif type(x) == list:
        b=0
        c=0
        for i in x:
            if type(i) is int:
                c+=1
            else:
                b+=1
        print('букв:',b,'цифр:',c)
    elif type(x) == int:
        d=0
        for i in str(x):
            if int(i)%2!=0:
                d+=1
        print('нечётных цифр:',d)
    elif type(x) == str:
        print('букв:', len(x))
    else:
        print('Неизвестный тип')

a(('Hello','ywye','2323e'))
a([1, 2, 3, 4, 'a', 'b', 'c'])
a(32479)
a('abcd')
a({1: 2})

#Задача 8
def func(x):
    if -5<=x<=5:
        return x*x
    elif x < -5:
        return 2*abs(x)-1
    else:
        return 2*x
for i in range(-10,11):
    print(func(i),end=' ')

