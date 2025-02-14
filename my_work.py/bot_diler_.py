import pandas as pd

# Укажите путь к вашему файлу
file_path = "price.xls"  # Или "price.xlsx"

# Загружаем файл (автоматически выбираем движок)
df = pd.read_excel(file_path, engine="xlrd" if file_path.endswith(".xls") else "openpyxl")

# Проверяем, какие есть колонки
print("Колонки в файле:", df.columns)

# Укажите названия колонок
dealer_price_col = "Дилерская цена"
market_price_col = "Рыночная цена"
model_col = "Модель"  # Название модели техники

# Функция для расчёта итоговой цены
def calculate_final_price(row):
    dealer_price = row[dealer_price_col]
    market_price = row[market_price_col]
    
    if market_price < dealer_price:
        return dealer_price * 1.15  # +15%
    return market_price

# Создаём новый датафрейм с нужными колонками
new_df = pd.DataFrame()
new_df["Модель"] = df[model_col]
new_df["Дилерская цена"] = df[dealer_price_col]
new_df["Рыночная цена"] = df[market_price_col]
new_df["Итоговая цена"] = df.apply(calculate_final_price, axis=1)

# Сохраняем результат в новый файл
output_file = "final_prices.xlsx"
new_df.to_excel(output_file, index=False)

print(f"Новый файл создан: {output_file}")
