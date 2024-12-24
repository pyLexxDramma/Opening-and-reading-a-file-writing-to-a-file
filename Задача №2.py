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


def get_shop_list_by_dishes(dishes, person_count):
    """Возвращает список покупок для заданных блюд и количества персон."""
    shop_list = {}
    cook_book = read_recipes_file('files/recipes.txt')  # Читаем рецепты из файла

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity  # Увеличиваем количество, если ингредиент уже есть
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}  # Добавляем новый ингредиент

    return shop_list


def main():
    file_path = 'files/recipes.txt'
    create_recipes_file(file_path)
    print(f"Файл '{file_path}' успешно создан.")

    # Пример использования функции get_shop_list_by_dishes
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print("Список покупок:")
    for ingredient, details in shop_list.items():
        print(f"{ingredient}: {details['quantity']} {details['measure']}")


if __name__ == "__main__":
    main()

#create_recipes_file: Создает файл с рецептами.
#parse_ingredient: Парсит строку с ингредиентом.
#read_recipes_file: Читает рецепты из файла и возвращает словарь с блюдами и их ингредиентами.
#get_shop_list_by_dishes: Формирует список покупок на основе выбранных блюд и количества персон.
