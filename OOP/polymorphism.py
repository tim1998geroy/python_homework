import math
# Задание 1
# class Document:
#     def print_info(self):
#         print('Это базовый Document')

# class PDFDocument(Document):
#     def print_info(self):
#         print('Это документ в формате PDF.')

# class WordDocument(Document):
#     def print_info(self):
#         print('Это документ в формате WORD.')

# def print_document_info(self):
#     doc.print_info()

# documents = {
#     Document(),
#     PDFDocument(),
#     WordDocument(),
#     PDFDocument(),
#     Document(),
#     WordDocument()
# }

# for doc in documents:
#     print_document_info(doc)

# Задание 2
# class Animal:
#     def make_sound(self):
#         print('Животное издает звук')

# class Dog(Animal):
#     def make_sound(self):
#         print('Гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('Мяу')

# class Cow(Animal):
#     def make_sound(self):
#         print('Муу')

# def make_animals_talk(animals:list):
#     for animal in animals:
#         animal.make_sound()

# animals = [
#     Dog(),
#     Cat(),
#     Cow(),
#     Dog(),
#     Cat()
# ]

# make_animals_talk(animals)

# Задание 3
# class Toy:
#     def play_sound(self):
#         print('Игрушка издает звук.')

# class Car(Toy):
#     def play_sound(self):
#         print('Бип-бип')

# class Doll(Toy):
#     def play_sound(self):
#         print('Мама')

# class Drum(Toy):
#     def play_sound(self):
#         print('Бум-бум')

# toys = [
#     Car(),
#     Doll(),
#     Drum(),
#     Car(),
#     Drum(),
#     Doll()
# ]

# print('В магазине игрушек началась демонстрация.')

# for toy in toys:
#     toy.play_sound()

# Задание 4
# class Shape:
#     def area(self):
#         ...

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# class Reactangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

# class Triangle(Shape):
#     def __init__(self, base, haight):
#         self.base = base
#         self.haight = haight

#     def area(self):
#         return 0.5 * self.base * self.haight
    
# shapes = [
#     Circle(5),
#     Reactangle(4,6),
#     Triangle(3, 8),
#     Circle(2.5),
#     Reactangle(10,3)
# ]

# # Выводит площади всех фигур
# print('Площади фигур: ')
# for shape in shapes:
#     print(f'{shape.__class__.__name__}: {shape.area():.2f}') #shape.__class__ получает класс текущего объекта __name__ возвращает имя этого класса в виде строки 

# Задание 5
# class Card:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def withdraw(self, amount):
#         ...

# class CreditCard(Card):
#     def withdraw(self, amount):
#         self.balance -= amount
#         print(f'С кредитной кары списано {amount}. Текущий баланс: {self.balance}')

# class DebitCard(Card):
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print(f'Нельзя списать {amount}. На дебетовой карте только {self.balance}')
#         else:
#             self.balance -= amount
#             print(f'С дебетовой карты списано {amount}. Остаток: {self.balance}')

# my_credit = CreditCard(1000)
# my_debit = DebitCard(500)

# my_credit.withdraw(300)
# my_credit.withdraw(800)
# my_debit.withdraw(200)
# my_debit.withdraw(400)