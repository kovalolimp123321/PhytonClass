#-*-coding:cp1251-*-
a=int(input())
b=a%2
if (a>0) and (b==0):
 print('положительное четное число')
elif (a>0) and (b==1):
 print('положительное нечетное число')
elif(a==0):
 print('нулевое число')
elif(a<0) and (b==0):
 print('отрицательное четное число')
elif(a<0) and (b==1):
 print('отрицательное нечетное число')
 