#вывести первые N чисел кратные M и больше K
n  = int(input())
m  = int(input())
k  = int(input())
for i in range(k + 1, k + ((n + 1) * m)):
    if i % m == 0:
        print(i)

