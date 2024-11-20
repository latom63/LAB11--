import csv

# Назва вхідного та вихідного файлів
input_file = "life_expectancy.csv"  
output_file = "population_ukraine_results.csv"

try:
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Читаємо файл у вигляді словників
        print("Вміст файлу:")
        data = list(reader)  # Зберігаємо дані для подальшої роботи
        for row in data:
            print(row)

    # Фільтрування даних для України з показником Population, total
    ukraine_data = [
        {
            "Year": year,
            "Population": row[year]
        }
        for row in data if row["Country Name"] == "Ukraine"
        for year in row.keys() if year.isdigit() and 1991 <= int(year) <= 2019
    ]

    # Знаходження найнижчого та найвищого значень
    min_population = min(ukraine_data, key=lambda x: float(x["Population"].replace(",", "")))
    max_population = max(ukraine_data, key=lambda x: float(x["Population"].replace(",", "")))

    # Запис результатів у новий файл
    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ["Year", "Population", "Type"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({"Year": min_population["Year"], "Population": min_population["Population"], "Type": "Min"})
        writer.writerow({"Year": max_population["Year"], "Population": max_population["Population"], "Type": "Max"})

    print(f"Результати записано у файл: {output_file}")
    print(f"Найнижче значення: {min_population}")
    print(f"Найвище значення: {max_population}")

except FileNotFoundError:
    print(f"Помилка: Файл '{input_file}' не знайдено. Перевірте його назву та місцезнаходження.")
except KeyError as e:
    print(f"Помилка: Вказаного стовпця не знайдено у файлі ({e}).")
except Exception as e:
    print(f"Невідома помилка: {e}")
