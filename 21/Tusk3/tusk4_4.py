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


