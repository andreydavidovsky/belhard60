#Сделать калькулятор: у пользователя
#спрашивается число, потом действие и второе число
n1 = (int(input("введите число")))
print("какое действие хотите выполнить * , +, -, /?")
x = input("")
n2 = (int(input("введите второе число")))
while n1 in range(n1, n1 + 1):
    if x == "*":
        print(n1 * n2)
        break
    elif x == "+":
        print(n1 + n2)
        break
    elif x =="-":
        print(n1 - n2)
        break
    elif x == "/":
        print(n1 / n2)
        break

