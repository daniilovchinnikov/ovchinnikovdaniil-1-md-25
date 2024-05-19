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

#     if filename.lower().endswith((".png", ".jpg")):
#         input_path = os.path.join(ex, filename)
#         output_path = os.path.join(im, filename)
#
#         image = Image.open(input_path)
#         processed_image = convert_to_grayscale(image)
#         processed_image.save(output_path)