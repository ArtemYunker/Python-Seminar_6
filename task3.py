# 3.Задача Измените код одной-двух решенных ранее задач (с прошлых семинаров или домашних работ),
#  применив лямбды, filter, map, zip, enumerate, списочные выражения.

import math
from functools import reduce

string =[]
n= 0
while n != ' ':
    n = str(input('введите число '))
    string.append(n)
del string[-1]

digit = list(filter(lambda x: x.isdigit(),string))

newlist=[]
temp = [newlist.append(int(digit[i])) for i in range(len(digit))]
print(newlist)

res = reduce(math.gcd, newlist)

print(res)

