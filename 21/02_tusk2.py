a=int(input("Введите номер вашего места"))
if a>22 and a%2==0:
    print("Верхнее боковое")
elif a>22 and a%2!=0:
    print("Нижнее боковое")
elif a%2!=0:
    print("Нижнее купе")
else:
    print("Верхнее купе")