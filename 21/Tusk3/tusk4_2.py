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