#Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3#
first = int(input())
second = int(input())
third = int(input())
summ = (first + second + third) / 3
print(round(summ, 3))
