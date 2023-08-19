#-*-coding:cp1251-*-
n=int(input('Введите число '))
a=0
for i in range(1,n+1):
    s=int(input('Введите целое число '))
    if s==0:
        a+=1
print(a)
