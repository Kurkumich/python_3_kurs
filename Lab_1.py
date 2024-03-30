#--*-- encoding: cp1251 --*--
import numpy as np
import math
number = int(input('Введите число: '))
co_prime_count = number
dividers = []
i = 2
while i<=number:
    if number%i:
        i+=1
    else:
        number = number//i
        dividers.append(i)
dividers = list(set(dividers))
for i in range(0,len(dividers)):
    co_prime_count *= (1-1/dividers[i])
print(int(co_prime_count))