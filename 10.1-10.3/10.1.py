# 10.1-10.3

def z101():
    import json
    with open("products.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for product in data["products"]:
        name = product["name"]
    price = product["price"]
    weight = product["weight"]
    available = product["available"]
    if available:
        availability = "В наличии"
    else:
        availability = "Нет в наличии!"
    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(availability)
    print()

def z102():
    import json
    with open("products.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    name = input("Введите название продукта: ")
    price = int(input("Введите цену продукта: "))
    weight = int(input("Введите вес продукта: "))
    available = input("Введите 'да', если продукт в наличии, или 'нет': ")
    if available.lower() == "да":
        available = True
    else:
        available = False
    new_product = {
    "name": name,
    "price": price,
    "weight": weight,
    "available": available
    }
    data["products"].append(new_product)
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    for product in data["products"]:
        name = product["name"]
    price = product["price"]
    weight = product["weight"]
    available = product["available"]
    if available:
        availability = "В наличии"
    else:
        availability = "Нет в наличии!"
    print(f"Название: {name}")
    print(f"Цена: {price}")
    print(f"Вес: {weight}")
    print(availability)
    print()


def z103():
    with open("en-ru.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    ru_en_dict = {}
    for line in lines:
        elements = line.strip().split(" - ")
        if len(elements) == 2:
            en, ru = elements
            ru_list = ru.split(", ")
            for ru_word in ru_list:
                if ru_word not in ru_en_dict:
                    ru_en_dict[ru_word] = []
                ru_en_dict[ru_word].append(en)
    output_lines = []
    for ru_word, en_list in sorted(ru_en_dict.items()):
        en_str = ", ".join(en_list)
        output_lines.append(f"{ru_word} – {en_str}")
    with open("ru-en.txt", "w", encoding="utf-8") as file:
        file.write("\n".join(output_lines))

availability = "В наличии"
else:
availability = "Нет в наличии!"
print(f"Название: {name}")
print(f"Цена: {price}")
print(f"Вес: {weight}")
print(availability)
print()