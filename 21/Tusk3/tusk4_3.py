def z4():
    try:
        day, month, year = map(int, date.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
    except (TypeError, ValueError):
        return False
date = input("Введите дату : ")
if z4():
    print("Это магическая дата!")
else:
    print("Это не магическая дата.")