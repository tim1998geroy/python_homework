# Задание 1
# days_dict1 = {
#     'Понедельник':1,
#     'Вторник': 2,
#     'Среда' : 3,
#     'Четверг' : 4,
#     'Пятница' : 5,
#     'Суббота' : 6,
#     'Воскресенье' : 7    
# } 

# print(days_dict1)
# b
# days = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
# numbers = range(1,8)
# days_dict2 = dict(zip(days, numbers))

# print(days_dict2)


#Задание 2 
# week =  {
#     'Понедельник':1,
#     'Вторник':2,
#     'Среда':3
# }

# print(week['Среда'])

# print(week.get('четверг', 'Нет такого дня'))

#Задание 3
# months = {}

# months['Январь'] = 31
# months['Февраль'] = 28
# months['Март'] = 31

# print(months)

#Задание 4
# grades = {'Математика': 5, 'физика': 4, 'Химия':3}

# grades['Химия'] = 4
# print(grades)

#Задание 5
# subjects = {'математика': 5, 'физика':4, 'химия': 3}
# del subjects['физика']
# print(subjects)

# #Задание 6
# products = {'яблоки':50, 'бананы': 30, 'апельсины': 70}
# product_name = input('Введите название продукта: ').strip().lower()

# price = products.get(product_name)

# if price is not None:
#     print(f'Цена {product_name}: {price} сом.')
# else:
#     print('Товар отсутствует')


#Задание 7
# config = {'theme':'dark', 'version':'1.0.1', 'debug':True}

# config_copy = config.copy()

# config_copy['debug']= False

# print('Оригинальный словарь',  config)
# print('Копия словаря', config_copy)

#Задание 8
# phonebook = {'Иван': '123-45-67', 'Мария':'789-01-23', 'Олег':'456-78-90'}

# print(list(phonebook.keys()))

#Задание 9 
# scores = {
#     'Аня' : 85,
#     'Борис' : 92,
#     'Вика' : 78,
#     'Гена' : 88
# }

# for name, score in scores.items():
#     print(f'{name} - {score}')