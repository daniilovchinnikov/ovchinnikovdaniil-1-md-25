def z2():
    a = [10, 20, 30, 20, 40, 50, 10]
    save = set()
    double = set()
    for num in a:
        if num in save:
            double.add(num)
        else:
            save.add(num)
    if double:
        print("В списке есть повторяющиеся элементы:", double)
    else:
        print("В списке нет повторяющихся элементов.")
    print("Исходный список:", a)
z2()