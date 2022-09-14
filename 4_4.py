# судоку 9*9 что б заполненая генерировалось меньше секунды
# вводиться чисо n псчитать сумм чисел от 1 до n

n = int(input())
#for i in range(1, n + 1):
numbers = [i for i in range(1, n+1)]
print(sum(numbers))
