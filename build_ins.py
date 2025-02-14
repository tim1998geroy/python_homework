# # Задание 1
# names = ['Nikita', 'Katana', 'Toma']
# ages = [25, 30, 35]

# print(dict(zip(names, ages)))

# Задание 2
# text = "python"
# print('\n'.join(map(lambda x: f'{x[0]} {x[1]}', enumerate(text, start = 1))))

# Задание 3
# numbers = ["10", "20", "30", "40"]
# print(list(map(int, numbers)))


# Задание 4
# words = ["apple", "banana", "cherry", "dog", "elephant"]
# print(list(filter(lambda x: x[0].lower() in 'd', words)))

# Задание 5
# numbers = [1, -2, 3, -4, 5, -6]

# print(list(map(lambda x: x**2, filter(lambda x: x > 0, numbers))))   
# Задание 6
students = ["Alice", "Bob", "Charlie", "David"]
scores = [85, 92, 78, 90]

print(list(enumerate(filter(lambda x: x[1]>80, zip(students, scores)), start = 1)))