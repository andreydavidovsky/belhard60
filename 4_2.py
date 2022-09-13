#Без использования collections, написать программу, которая будет
#создавать словарь для подсчитывания количества вхождений каждой
#буквы в текст введенный с клавиатуры
my_dict = {}
text = input()
for i in text:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
for i in my_dict.items():
            #print(my_dict)
            #print(i)
            print(len(my_dict))

