def z1():
    from PIL import Image
    image = Image.open("1.jpg")
    width, height = image.size
    print(f"Размер изображения: {width}x{height}")
    image_format = image.format
    print(f"Формат изображения: {image_format}")
    color_mode = image.mode
    print(f"Цветовая модель: {color_mode}")
z1()
def z2():
    from PIL import Image
    image_path = "2.jpg"
    image = Image.open(image_path)
    small = image.resize((image.width // 3, image.height // 3))
    small.save("small_image.jpg")
    horizontal = image.transpose(Image.FLIP_LEFT_RIGHT)
    horizontal.save("horizontal_mirror.jpg")
    vertical = image.transpose(Image.FLIP_TOP_BOTTOM)
    vertical.save("vertical_mirror.jpg")
    print("Изображения успешно сохранены.")
z2()

def z3():
    from PIL import Image, ImageFilter
    import os
    a = "filtr"
    os.makedirs(a, exist_ok=True)
    images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    filter_type = ImageFilter.EDGE_ENHANCE
    for director in images:
        b = director
        output_image_path = os.path.join(a, f"car_{director}")
        with Image.open(b) as img:
            с = img.filter(filter_type)
            с.save(output_image_path)
    print("Фильтр успешно применен к изображениям и сохранен в новую папку.")
z3()



