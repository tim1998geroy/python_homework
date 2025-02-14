# cd Desktop 
#mkdir metalabs 
#cd metalabs
#touch metalabs.py
#cd .. 
#mkdir lesson 
#rm -r lesson metalabs
#mkdir hidden 
#cd hidden
#touch .secret .env
#ls -a
#mkdir hello 
#mv .env hello
#cd .. 
#mv .secret .metalabs
#cd ..
#cd..
#ls -a Desktop/hidden/hello


#===========Data-types=============
# from datetime import datetime
# Задача a
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите число которое хотите умножить эти числа: '))

# s = num1 + num2
# p = num1 * num3
# k = num2 * num3
# kvad1 = num1 ** 2
# kvad2 = num2 ** 2
# minus1 = kvad1 - 5555
# minus2 = kvad2 - 5555
# print('Сложения два числа: ', num1 + num2, '\nУмножение двух чисел: ', '\nПервое: ',p,'\nВторое:',k)
# print('Возведены в квадрат два числа', '\nПервое число: ', kvad1, '\nВторое число: ', 
#       kvad2, '\nМинусовали одно число 5555: ', '\nПервое: ', minus1, '\nВторое', minus2)

# Задание номер 2
# god = int(input('Введите свой год рождения: '))
# current_date = datetime.now().year

# voz = current_date - god
# print('Ваш возраст: ',voz,'\nВам через два года будет:', voz + 2, 
#       '\nВам через два года назад было: ', voz - 2, 
#       '\nУмножим ваш возраст на 365: ', voz * 365)

# #задание 3

# god = int(input('Введите свой год рождения: '))
# current_date = datetime.now().year

# voz = current_date - god

# sec1 = voz * 365 * 24 * 60 * 60

# print('Ваш год: ', god, '/nСколько вам лет:', voz, '\nСколько вы секунд прожили: ', sec1)

#Задача 4

# chocolad_price = float(input('Введите стоимость одной штуки шоколада: '))
# milk_price = float(input('Введите стоимость одной штуки молока: '))
# coffe_price = float(input('Введите стоимость одной упаковки кофе: '))

# chocolad_qwanti = int(input('Введите количество шоколада в корзине: '))
# milk_qwanti = int(input('Введите количество упаковок молока в корзине: '))
# coffe_qwarti = int(input('Введите количество упаковок кофе в корзине: '))

# total_price = (chocolad_price * chocolad_qwanti) + (milk_price * milk_qwanti) + (coffe_price * coffe_qwarti)

# print(f'Общая стоимость товаров в корзине: {total_price} сом')


# Задание 5
# num1 = float(input('Введите шерину треугольник: '))
# num2 = float(input('Введите длину треугольника: '))

# sum = 2 * (num1+ num2)

# print(f'Периметр прямоугольника: {sum}')
