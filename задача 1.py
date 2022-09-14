def recurs(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return recurs(a, n/2)**2
    else:
        return a*recurs(a, n-1)
a = int(input())
n = int(input())
print(recurs(a, n))
