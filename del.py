a = int(input('''Введите число a'''))
b = int(input('''Введите число b'''))

if (a==0 and b==0):
    print('INF')

if (a==0 and b!=0):
    print('NO')

if (a!=0 and b%a!=0):
    print('NO')

if (a!=0 and b%a==0):
    n = int(-b/a)
    print(n)


