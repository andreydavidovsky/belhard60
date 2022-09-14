#Заполнить список степенями числа 2 (от 2^1 до 2^n)
#my_list = []
#for i in range(1, 20):
#my_list.append(2 ** i)
#print(my_list)

n = int(input())
my_list = [2**i for i in (range(1, n))]
print(my_list)