def z1(number):
    if number % 5 == 0:
        return True
    else:
        return False
number = int(input("Введите число: "))
if z1(number):
    print(f"{number} делится на 5!")
else:
    print(f"{number} не делится на 5.")



def z2():
    try:
        num = float(input("Введите число, на которое хотите разделить 300: "))
        result = 300 / num
        print(f"Результат деления 300 на {num}: {result}")
    except ValueError:
        print("Ошибка: Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: Пожалуйста, введите число, отличное от нуля.")
z2()



def z3(date):
    try:
        day, month, year = map(int, date.split('.'))
        if day * month == year % 100:
            return True
        else:
            return False
    except (TypeError, ValueError):
        return False
date = input("Введите дату : ")
if z3(date):
    print("Это магическая дата!")
else:
    print("Это не магическая дата.")


def z4(number):
    if len(number) % 2 != 0:
        return False

    a = len(number) // 2
    b = number[:a]
    c = number[a:]

    sumfirst = sum(int(digit) for digit in b)
    sumsecond = sum(int(digit) for digit in c)

    return sumfirst == sumsecond
number = input("Введите номер билета: ")
if z4(number):
    print("Этот билет — счастливый!")
else:
    print("Этот билет не является счастливым.")

z2()