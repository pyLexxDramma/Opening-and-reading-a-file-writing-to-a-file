import os


def create_recipes_file(file_path):
    """Создает файл с рецептами."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    recipes = """Омлет
3
Яйцо | 2 | шт
Молоко | 100 | мл
Помидор | 2 | шт

Утка по-пекински
4
Утка | 1 | шт
Вода | 2 | л
Мед | 3 | ст.л
Соевый соус | 60 | мл

Запеченный картофель
3
Картофель | 1 | кг
Чеснок | 3 | зубч
Сыр гауда | 100 | г

Фахитос
5
Говядина | 500 | г
Перец сладкий | 1 | шт
Лаваш | 2 | шт
Винный уксус | 1 | ст.л
Помидор | 2 | шт
"""
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(recipes)


def parse_ingredient(line):
    """Парсит строку с ингредиентом и возвращает словарь."""
    name, quantity, measure = line.strip().split(' | ')
    return {
        'ingredient_name': name,
        'quantity': int(quantity),
        'measure': measure
    }


def read_recipes_file(file_path):
    """Читает рецепты из файла и возвращает словарь с блюдами и ингредиентами."""
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            dish_name = lines[i].strip()
            i += 1
            if i >= len(lines) or lines[i].strip() == '':
                break  # Прерываем, если достигли конца файла или пустой строки
            ingredient_count = int(lines[i].strip())
            i += 1
            ingredients = []
            for _ in range(ingredient_count):
                ingredients.append(parse_ingredient(lines[i]))
                i += 1
            cook_book[dish_name] = ingredients
            # Пропускаем пустую строку между блюдами
            if i < len(lines) and lines[i].strip() == '':
                i += 1
    return cook_book


def main():
    file_path = 'files/recipes.txt'
    create_recipes_file(file_path)
    print(f"Файл '{file_path}' успешно создан.")

    cook_book = read_recipes_file(file_path)

    # Выводим результат в формате "строка под строкой"
    for dish, ingredients in cook_book.items():
        print(f"{dish}:")
        for ingredient in ingredients:
            print(f"  {ingredient['ingredient_name']}: {ingredient['quantity']} {ingredient['measure']}")
        print()  # Пустая строка между блюдами


if __name__ == "__main__":
    main()


#Функция create_recipes_file: Создаёт файл с предопределёнными рецептами.
#Функция parse_ingredient: Парсит строку с ингредиентом и возвращает словарь с его данными.
#Функция read_recipes_file: Читает файл и формирует словарь cook_book, где ключами являются названия блюд, а значениями — списки ингредиентов.
#Функция main: Основная функция, которая создаёт файл и читает рецепты, выводя результат.
#орматирование вывода: В функции main добавлен цикл, который выводит каждое блюдо и его ингредиенты в формате "строка под строкой".
# Каждое блюдо выводится с отступом для ингредиентов, а между блюдами добавляется пустая строка для лучшей читаемости.