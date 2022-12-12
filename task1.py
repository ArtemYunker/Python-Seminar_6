# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b),
# возвращающая наибольший общий делитель (НОД) двух чисел.
# вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
#  Ввод чисел продолжается до ввода пустой строки.
# Входные данные Выходные данные
# 36 6
# 12
# 144
# 18

import math
from functools import reduce

string =[]
n= 0
while n != ' ':

    n = str(input('введите число '))
    string.append(n)
del string[-1]
print(string)

digit = list(filter(lambda x: x.isdigit(),string))
print(digit)


newlist =[]
for i in range(len(digit)):
    newlist.append(int(digit[i]))

print(newlist)


res = reduce(math.gcd, newlist)

print(res)