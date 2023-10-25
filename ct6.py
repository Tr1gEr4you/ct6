import re

with open("журнал.txt", "r", encoding="utf-8") as input_file, open("преобразованный_журнал.txt", "w", encoding="utf-8") as output_file:
    pattern = r"Рейс (\d+) (прибыл|отправился) (из|в) ([а-яА-Я\s]+) в (\d{2}:\d{2}:\d{2})"

    for line in input_file:
        match = re.search(pattern, line)
        if match:
            number = match.group(1)
            action = match.group(2)
            direction = match.group(3)
            city = match.group(4)
            time = match.group(5)

            output_line = f"[{time}] - Поезд № {number} {'из' if direction == 'из' else 'в'} {city}\n"
            output_file.write(output_line)

print("Преобразование завершено. Результат записан в файл 'преобразованный_журнал.txt'.")