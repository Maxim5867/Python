k = int(input('''Введите сколько человек вмещается в автобус'''))
n = int(input('''Введите количество детей'''))
m = int(input('''Введите количество взрослых'''))
if (n%(k-2))!=0:
    d = (n//(k-2))+1
else:
    d = (n//(k-2))
if k<3:
    print('0')
elif (m//2)<d:
    print('0')
else:
    a = (m+n)//k
    if((m+n)%k)!=0:
        a += 1
    print(a)
