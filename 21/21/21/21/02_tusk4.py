def смешивание_цветов(a, b):
    if (a == 'красный' and b == 'синий') or (a == 'синий' and b == 'красный'):
        return 'фиолетовый'
    elif (a == 'красный' and b == 'желтый') or (a == 'желтый' and b == 'красный'):
        return 'оранжевый'
    elif (a == 'синий' and b == 'желтый') or (a == 'желтый' and b == 'синий'):
        return 'зеленый'
    else:
        return 'Ошибка: введите только названия красный, синий или желтый'

a = input('Введите название первого цвета: ')
b = input('Введите название второго цвета: ')

c = смешивание_цветов(a, b)
print(c)