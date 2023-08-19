# -*- coding: cp1251 -*-
a = input('Напишите слово ')
b = 0;
r = 0;

for i in range(0, len(a)):
    let = a[i]
    if let == 'a' or let == 'e' or let == 'i' or let == 'o' or let == 'u':
        r+=1
    else:
        b+=1

if r == 0:
    print('False');
else:
    print("Согласных", b)
    print('Гласных', r)
