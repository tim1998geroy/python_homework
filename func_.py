# Функции 
# Задание 1 
# def calculate_return(loan_amount, interest_rate=7.89):
#     interest_amount = loan_amount * (interest_rate / 100)
#     return round(loan_amount + interest_amount, 2)

# def get_loan_amount():
#     while True:
#         try:
#             loan_amount = float(input('Введите сумму займа (не меньше 100 000): ').replace(' ', ''))
#             if loan_amount < 100000:
#                 print('Ошибка: сумма займа должна быть не меньше 100 000')
#                 continue
#             return loan_amount
#         except ValueError:
#             print('Ошибка: введите числовое значение.')

# loan_amount = get_loan_amount()
# total_to_return = calculate_return(loan_amount)
# format_total = f'{total_to_return:,.2f}'.replace(',', ' ')
# print(f'Сумма к возврату: {format_total}')


# Задание 2
# def extr_numbers(text):
#     numbers = ''.join(filter(str.isdigit, text))
#     return int(numbers) if numbers else None

# def main():
#     user_input = input('Введите текст цифрами: ')
#     result = extr_numbers(user_input)
#     if result is not None:
#         print('Извлеченное число: ', result)
#     else:
#         print('В тексте нет цифр.')

# if __name__ == '__main__':
#     main()


# Задание 3
# def calculate_days():
#     try:
#         years = int(input('Введите количество лет: '))
#         month = int(input('Введите количество месяцев: '))

#         total_days = (years * 12 + month) * 30
#         print(f'Общее количество дней: {total_days}')
#     except ValueError:
#         print('Ошибка: пожалуйста, введите целые числа.')

# calculate_days()

# Задание 4
# def generate_cub_dict():
#     return {num: num**3 for num in range(1, 11)}

# def main():
#     cubed_dict = generate_cub_dict()
#     print('Словарь с кубами чисел:\n', cubed_dict)

# if __name__ == '__main__':
#     main()

# Задание 5
# def sum_1_to_50():
#     return sum(range(1,51))

# result = sum_1_to_50()
# print(result)