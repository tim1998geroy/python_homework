# # 1 Задание
# input_string = input('Введите строку: ')

# upper_string = input_string.upper()

# format_output = f' Исходная строка - {input_string}, \nстрока после изменения регистра - {upper_string}'
# print(format_output)

#2 Задание

# slovo1 = input('Введите несколько слов: ')

# simvol = slovo1.replace(' ', '-')
# print(simvol)

#3 Задание 
# stroca1 = input('Напишите строку: ')

# probel = stroca1.replace(' ', '')

# if probel.isalpha():
#     print('У вас используется буквы')
# elif probel.isdigit():
#     print('У вас написаны символы: ')
# else:
#     print('Вы используете то и другое')

#4 Задание

# my_string = 'Пример строки'

# print(dir(my_string))

#5 Задание

# pred1 = input ('Напишите предложения: ')

# #a 
# print('Первый символ: ', pred1[0])

# #b
# print('Выведен послдний символ: ', pred1[-1])

# #c 
# words = pred1.split()
# if len(words) > 1:
#     slic_sent = ' '.join(words[1:])
#     print('Предложение без первого слова: ', slic_sent)
# else:
#     print('Предложение  состоит из одного слова, срезать нечего. ')

# #d
# rev_sent = pred1[::-1]
# print('Отзеркаленное предложение: ', rev_sent)


#Условные операторы 

# Задание 1 
# number1 = int(input('Введите число: '))

# if number1 % 2 == 0:
#     print(f'Число - {number1} является четным')
# else:
#     print(f'Число - {number1} не является четным')


# Задание 2
# number = int(input('Введите число: '))

# if number % 2 ==0:
#     print(f'Число {number} является четным')
# else:
#     print('Число {number} не является четным')

# #
# if number % 3 == 0:
#     print(f'Число {number} делится на 3 без остатка')
# else:
#     print(f'Число {number} не делится на 3 без остатка')

# #
# if number ** 2 > 1000:
#     print(f'Число {number} в квадрате больше 1000')
# else:
#     print(f'Число {number} в квадрате не больше 1000')

# #Задание 3
# a = int(input('Введите первое число (a): '))
# b = int(input('Введите второе число (b): '))

# if a > 0 and b > 0: 
#     print(f'Число {a} и {b} является положительными')

#Задание 4 
# age = int(input('Введите ваш возраст: '))

# if age < 0 or age > 120: 
#     print('Недопустимый возраст! ')
# elif age >= 18:
#     print('Совершеннолетний')
# elif age <= 4:
#     print('Ребенок')
# else:
#     print('Несовершенолетний')

#Задание 5
# x = 13

# x = x**2

# if x<172: 
#     print(f'x={x}, но x все еще меньше 172. Возводим в квадрат снова. ')
#     x = x**2 

# print(f'Результат: x = {x}')