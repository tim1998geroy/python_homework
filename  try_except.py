# Задание 1
# try:
#     ...
# except:
#     ...
# else:
#     ...
# finally:
#     ...

# Задание 2
# try:
#     print(perem)
# except NameError:
#     print('Такой переменой нет')

# Задание 3
# try:
#     num1 = float(input('Введите первое число: '))
#     num2 = float(input('Введите второе число: '))

#     result = num1 / num2

#     print(f'Результат деления: {result}')
# except ZeroDivisionError:
#     print('На ноль делить нельзя! ')
# except ValueError:
#     print('Ошибка: Ввыведены некорректные данные. Пожалуйста введите числа')

# Задание 4
# try:
#     str1 = float(input('Введите первое число: '))
#     str2 = float(input('Введите второе число: '))

#     print(f'Сумма чисел: {str1 + str2}')

# except ValueError:
#     print('Введите число')

# Задание 5
# my_dict = {
#     'apple':'Яблоко',
#     'banana':'Банан',
#     'orange':'апельсин'
# }

# try:
#     key = input('Введите ключ для поиска в словаре:')

#     value = my_dict[key]

#     print(f'Значение для ключа "{key}" : {value}')
# except KeyError:
#     print('Нет такого ключа')

# Задание 6
# str1 = 'Hello'
# print(str1[0])

# Задание 7
# try:
#     age = int(input('Введите ваш возраст: '))

#     if age < 18:
#         raise ValueError('Доступ запрещен') 
# except ValueError as e:

#     if str(e) == 'Доступ запрещен':
#         print('Введен некоретный возраст')
#     else:
#         print('Ошибка: Введены некорретные данные. Пожалуйста, введите число.')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания')

#  Задание 8

# try:
#     num1 = float(input('Введите первое число: '))
#     num2 = float(input('Введите второе число: '))

#     result = num1 / num2

#     print(f'Результат деления: {result}')
# except(ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')

# Задание 9
# try:
#     den = float(input('Введите сумму денег: '))

#     if den < 0:
#         raise ValueError('Сумма не может быть отрицательной!')
    
#     print(f'Введенния сумма {den}')
# except ValueError as e:
#     print(f'Ошибка: {e}')

# Задание 10
try:
    string_value = "Строка"
    number_value = 42
    result = string_value + number_value


except TypeError:
    print("Unsupported option")