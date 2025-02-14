#Lists 
#Задаине 1
# numbers1 = [1, 2, 3, 4, 5]
# numbers1.append(6)
# print(numbers1)

# #Задание 2
# numbers1 = [1, 2, 3, 4, 5]

# remov_elem = numbers1.pop(numbers1.index(3))

# print(f'Удаление элемент списка - {remov_elem}, обновленный список - {numbers1}')

#Задание 3
# list1 = ['яблоко', 'банан', 'вишня']
# list1[list1.index('банан')] = 'персик'
# print(list1)

# Задание 4
# list1 = [42, 13, 89, 7, 64, 22]

# ascen = sorted(list1)
# desce = sorted(list1, reverse=True)

# print(f'Список по возрастанию: {ascen}, \nсписок по убыванию: {desce}')

#Задание5
# list1 = [[1,2], [3,4], [5,6]]

# list1.append([7,8])

# print(list1)

#Loops
#Задание 1
# x = 1

# while x <= 10:
#     print(x, end=' ')
#     x += 1


# for x in range(1, 11):
#     print(x, end=' ')

#Задание 2
# x = 1

# while x <= 100:
#     if x % 3 == 0 and x % 5 == 0:
#         print(x, end=' ')
#     x += 1

# for x in range(1, 101):
#     if x % 3 == 0 and x % 5 == 0:
#         print(x, end=' ')

#Задание 3
# x = 1

# while x <= 100:
#     if x % 2 == 0 and x % 9 == 0: 
#         print(x, end=' ')
#     x += 1

# for x in range(1, 101):
#     if x % 2 == 0 and x % 9 == 0:
#         print(x, end=' ')

# #Задание 4 
# for x in range(1, 301, 2):
#     if x == 237: 
#         break
#     print(x, end=' ')

#Задание 5 
# str1 = my_string = "Ботнет IPStorm, в который ранее входили лишь Windows-машины, увеличился до 13 500 зараженных систем"

# for char in str1:
#     if char.isdigit():
#         num = int(char)
#         result = num * 2 
#         print(result, end=' ')
