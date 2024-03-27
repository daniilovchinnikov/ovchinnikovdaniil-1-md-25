def z1():
    numbers = [5, 10, 20, 30, 40]
    a = int(input("Введите число: "))
    if a in numbers:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
    print("Исходный список:", numbers)

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

def z3():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    number = int(input("Сколько выходных дней на неделе вы хотите? "))
    weekend_days = days[-number:]
    work_days = days[:-number]
    print("Ваши выходные дни:", ', '.join(weekend_days))
    print("Ваши рабочие дни:", ', '.join(work_days))

def z4():
    md25 = ['Постников', 'Петров', 'Овчинников', 'Свириденко', 'Крюков', 'Карпенко', 'Гусева', 'Бричалова', 'Поспелова', 'Идрисова']
    group2 = ['Соколов', 'Ткаченко', 'Иванов', 'Федоров', 'Харитонов', 'Цветков', 'Чернов', 'Шестаков', 'Щербаков', 'Юдин']
    sports_team = tuple(md25[:5] + group2[:5])
    print("Список студентов в группе 1:", md25)
    print("Список студентов в группе 2:", group2)
    print("Спортивная команда:", sports_team)
    print("Длина спортивной команды:", len(sports_team))
    sports_team1 = sorted(sports_team)
    print("Отсортированная спортивная команда:", sports_team1)
    name = sports_team1.count('Иванов')
    if name > 0:
        print("Фамилия 'Иванов' входит в спортивную команду.")
        print("Количество участников с фамилией 'Иванов':", name)
    else:
        print("Фамилии 'Иванов' нет в спортивной команде.")
z1()