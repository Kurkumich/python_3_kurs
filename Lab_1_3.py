#--*-- encoding:cp1251 --*--
num = int(input('Введите число: '))
num1 = num
sum_ = 0
while num1:
    sum_ += num1%10
    num1 = num1//10
div = []
for i in range(2, sum_):
    if sum_%i == 0:
        div.append(i)
for i in range (2, num):
    if num%i==0 and not(i in div):
        print('Делитель взаимно простой с суммой цифр: ' + str(i))
        num1 = 1
        break;
if num1 == 0:
    print('Таких делителей нет')

#print(div)


