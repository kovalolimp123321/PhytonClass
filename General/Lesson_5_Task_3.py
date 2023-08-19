#-*-coding:cp1251-*-
a=int(input('Сколько денег у Майкла '))
b=int(input('Сколько денег у Ивана '))
x=int(input('Минимальная сумма для вложения '))
c=a+b
if (a>=x) and (b>=x):
    print(2)
elif (a>=x) and (b<x):
    print('Mike')
elif (a<x) and (b>=x):
    print('Ivan')
elif (c>=x):
    print(1)
elif(a<x) and (b<x):
    print(0)
