# Задание 1
# def before_exec(func):
#     def wrapper(*args, **kwargs):
#         print('Выполнение функции...')
#         return func(*args, **kwargs)
#     return wrapper

# @before_exec
# def my_func():
#     print('Функция выполнена!')

# my_func()
# Задание 2
# def multi_result_by_2(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result * 2
#     return wrapper

# @multi_result_by_2
# def add(a, b):
#     return a + b

# print(add(3,5))
# Задание 3
# def add_exclamation_mark(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result + "!"
#     return wrapper

# @add_exclamation_mark
# def greet(name):
#     return f'Hello, {name}'

# print(greet('Alice'))

# Задание 4
# def limit_calls(max_calls):
#     def decorator(func):
#         call_count = 0

#         def wrapper(*args, **kwargs):
#             nonlocal call_count
#             if call_count < max_calls:
#                 call_count +=1
#                 return func(*args, **kwargs)
#             else:
#                 print('Функция больше недоступна')
#         return wrapper
#     return decorator

# @limit_calls(3)
# def my_function():
#     print('Функция выполнена')

# my_function()
# my_function()
# my_function()
# my_function()

# Задание 5
import functools

def log_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Вызов {func.__name__} с аргументами: args={args}, kwargs = {kwargs}')
        return func(*args, **kwargs)
    return wrapper


@log_arguments
def example_function(a,b, c=10):
    return a + b + c

print('Результат:', example_function(1, 2, c=3))