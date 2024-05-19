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
