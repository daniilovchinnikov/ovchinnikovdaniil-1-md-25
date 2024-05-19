# 8.1-8.3

def z81():
    from PIL import Image

    image = Image.open("123.jpg")

    left = 100
    upper = 50
    right = 300
    lower = 250

    output = image.crop((left, upper, right, lower))

    output.save("image.jpg")

 def z82():
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg

    cards = {
        "Новый год": "new_year.jpg",
        "Рождество": "christmas.jpg",
        "День Святого Валентина": "valentines_day.jpg",
        "8 Марта": "womens_day.jpg",
        "1 Апреля": "april_fools_day.jpg"
    }

    holiday = input("К какому празднику вам нужна открытка? ")
    if holiday in cards:
        filename = cards[holiday]
    else:
        print("Извините, у нас нет открыток к этому празднику.")
        exit()

    img = mpimg.imread(filename)
    plt.imshow(img)
    plt.axis('off')
    plt.show()

def z83():
    from PIL import Image, ImageDraw, ImageFont
    image = Image.open("img.png")
    draw = ImageDraw.Draw(image)
    name = input("Введите имя того, кого вы хотите поздравить: ")
    text = f"{name.title()}, поздравляю!"
    font_size = 40
    font = ImageFont.truetype("ofont.ru_Rubik.ttf", font_size)
    text_color = (255, 0, 0)
    draw.text((image.width * 0.5, image.height * 0.2), text, font=font, anchor="mm", fill=text_color)
    image.save("output_image.png", "PNG")

# 9.1-9.3

def z91():
    from PIL import Image
    import os
    ex = "export"
    im = "import"
    if not os.path.exists(ex):
        os.makedirs(ex)
    def convert_to_grayscale(image):
        return image.convert("L")
    for filename in os.listdir(ex):
        input_path = os.path.join(ex, filename)
    output_path = os.path.join(im, filename)
    image = Image.open(input_path)
    processed_image = convert_to_grayscale(image)
    processed_image.save(output_path)

def z92():
    from PIL import Image
    import os
    ex = "export"
    im = "import"

    if not os.path.exists(ex):
        os.makedirs(ex)
    def convert_to_grayscale(image):
        return image.convert("L")
    for filename in os.listdir(ex):
        if filename.lower().endswith((".png", ".jpg")):
            input_path = os.path.join(ex, filename)
    output_path = os.path.join(im, filename)
    image = Image.open(input_path)
    processed_image = convert_to_grayscale(image)
    processed_image.save(output_path)

def z93():
    import csv

    products = []
    with open("product.csv", "r", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=",")
        for row in reader:
            if row["Продукт"]:
                products.append(row)

    total_sum = 0
    print("Нужно купить:")
    for product in products:
        name = product["Продукт"]
        quantity = int(product["Количество"]) if product["Количество"] else 0
        price = int(product["Цена"]) if product["Цена"] else 0
        product_sum = quantity * price
        total_sum += product_sum
        print(f"{name} - {quantity} шт. за {price} руб.")

    print(f"Итоговая сумма: {total_sum} руб.")


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


# 11.1-11.3

def z111():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print("Ресторан открыт!")
    new_restaurant = Restaurant("Pizza Planet", "итальянская")
    print(new_restaurant.restaurant_name)
    print(new_restaurant.cuisine_type)
    new_restaurant.describe_restaurant()
    new_restaurant.open_restaurant()

def z112():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")
    restaurant1 = Restaurant("McDonald's", "фастфуд")
    restaurant2 = Restaurant("KFC", "фастфуд")
    restaurant3 = Restaurant("Subway", "фастфуд")
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()

def z113():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating=0):
            self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.rating = rating
    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
    print(f"Тип кухни: {self.cuisine_type}")
    print(f"Рейтинг: {self.rating}")
    def update_rating(self, new_rating):
        self.rating = new_rating
    restaurant1 = Restaurant("McDonald's", "фастфуд")
    restaurant2 = Restaurant("KFC", "фастфуд")
    restaurant3 = Restaurant("Subway", "фастфуд", rating=4)
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()
    print()
    restaurant1.update_rating(3)
    restaurant2.update_rating(2)
    restaurant3.update_rating(5)
    restaurant1.describe_restaurant()
    print()
    restaurant2.describe_restaurant()
    print()
    restaurant3.describe_restaurant()

