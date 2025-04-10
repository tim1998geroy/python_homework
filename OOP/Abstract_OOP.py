from abc import ABC, abstractmethod
import math
# Задание 1
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         ...

# class Car(Transport):
#     def move(self):
#         print('Car is moving on the road')

# class Plane(Transport):
#     def move(self):
#         print('Plane is flying in the sky')

# car = Car()
# plane = Plane()

# car.move()
# plane.move()

# Задание 2
# class PaymentMethod(ABC):
#     def pay(self, amount):
#         ...

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         print(f'Оплата {amount} через PayPal')

# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         print(f'Оплата {amount} через PayPal')

# credit_card = CreditCard()
# paypal = PayPal()

# credit_card.pay(1000)
# paypal.pay(500)

# Задание 3
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         ...

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2 
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height
    
# circle = Circle(5)
# rectangle = Rectangle(10, 20)

# print(f'Площадь круга: {circle.area():.1f}') #округляем до 1 знака после запятой 
# print(f'Плозадь прямоугольника: {rectangle.area()}')

# Задание 4 
# class OutputDevice(ABC):
#     @abstractmethod
#     def display(self,text):
#         ...

# class Monitor(OutputDevice):
#     def display(self, text):
#         print(f'[Monitor] {text}')

# class Printer(OutputDevice):
#     def display(self, text):
#         print(f'[Printer] {text}')

# monitor = Monitor()
# printer = Printer()

# monitor.display('Hello world!')
# printer.display('Hello world!')

# Задание 5
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         ...

# class Dog(Animal):
#     def make_sound(self):
#         print('Гав')

# class Cat(Animal):
#     def make_sound(self):
#         print('Мяу')

# dog = Dog()
# cat = Cat()

# dog.make_sound()
# cat.make_sound()

# Задание 6
# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         ...

# class Develop(Employee):
#     def __init__(self, salary, bonus):
#         self.salary = salary
#         self.bonus = bonus

#     def calculate_salary(self):
#         return self.salary + self.bonus

# class Manager(Employee):
#     def __init__(self, hours, rate):
#         self.hours = hours
#         self.rate = rate

#     def calculate_salary(self):
#         return self.hours * self.rate
    
# dev = Develop(50000, 10000)
# mng = Manager(160, 2000)

# print('Зарплата разработчика:', dev.calculate_salary())
# print('Зарплата менеджера:', mng.calculate_salary())

# Задание 7
# class Database(ABC):
#     @abstractmethod
#     def connect(self):
#         ...

#     @abstractmethod
#     def disconnect(self):
#         ...

# class MySQLDatabase(Database):
#     def connect(self):
#         print('Подключение к MySQL')

#     def disconnect(self):
#         print('Отключение от MySQL')

# class PostgreSQLDatabase(Database):
#     def connect(self):
#         print('Подключение к PosterSQL')
    
#     def disconnect(self):
#         print('Отключение от PostgreSQL')

# db1 = MySQLDatabase()
# db2 = PostgreSQLDatabase()

# db1.connect()
# db1.disconnect()
# db2.connect()
# db2.disconnect()

