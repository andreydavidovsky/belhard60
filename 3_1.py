#Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами#
text = input('введи предложение')
print(text.replace(' ', '-'))
text_2 = text.split()
text = '-'.join(text_2)
print(text)
