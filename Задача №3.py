# Создание файлов с содержимым
file_contents = {
    '1.txt': """Строка номер 1 файла номер 1
Строка номер 2 файла номер 1""",

    '2.txt': """Строка номер 1 файла номер 2"""
}

# Запись содержимого в файлы
for filename, content in file_contents.items():
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Чтение содержимого файлов и сортировка
file_data = []
for filename in file_contents.keys():
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        file_data.append((filename, len(lines), lines))

# Сортировка по количеству строк
file_data.sort(key=lambda x: x[1])

# Запись в результирующий файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for filename, line_count, lines in file_data:  # Исправлено здесь
        result_file.write(f"{filename}\n{line_count}\n")
        for i in range(line_count):
            result_file.write(f"Строка номер {i + 1} файла {filename}\n")

# Вывод содержимого результирующего файла
with open('result.txt', 'r', encoding='utf-8') as result_file:
    print(result_file.read())
