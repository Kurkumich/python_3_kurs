##--*-- encoding: cp1251 --*--
#num = int(input('Введите число: '))
#print(123//100)
num = 161723
div = []
while num!=0:
    if num%10%3 == 0:
        div.append(num%10)
    num = num//10
div = list(reversed(div))
print(sum(div))