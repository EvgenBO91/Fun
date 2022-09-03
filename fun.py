import math
def square(n):
    a=n*4
    b=n**2
    c=math.sqrt(2)*n
    d=a,b,c
    print(tuple(d))
square(int(input('Сторона=')))

'''def is_year_leap(n):
    a=n % 4 == 0 and n % 100 != 0 or n % 400 == 0
    print(a)
is_year_leap(int(input()))'''

'''def season(n):
   if n == 12 or 1 <= n <= 2:
       print("Зима")
   elif  3 <= n <= 5:
       print("Весна")
   elif 6 <= n <= 8:
       print("Лето")
   elif 9 <= n <= 11:
       print("Осень")
   else:
       print("Неверно введён номер месяца!")
n = int(input("Введите номер месяца (1-12): "))
season(n)'''

'''def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(int(input('Введите число:'))))'''

'''import random
a=[]
while len(a)<10:
    a.append(random.randint(1,9))
print(a)
def cen():    
    sum=0
    for i in a:
        sum+=i
    return sum/len(a)
print('среднее:',cen())'''

'''while True:
    oper=input('Введите операцию:')
    if oper in '0':
        break
    a=float(input('Первое число:'))
    b=float(input('Второе число:'))
    def calc():
        try:
            if oper=='+': return a+b
            elif oper=='-': return a-b
            elif oper=='*': return a*b
            elif oper=='/': return a/b
        except ZeroDivisionError:
            print('Деление на ноль')
    print(calc())'''