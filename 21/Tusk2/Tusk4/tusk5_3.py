def z3():
    days = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    number = int(input("Сколько выходных дней на неделе вы хотите? "))
    weekend_days = days[-number:]
    work_days = days[:-number]
    print("Ваши выходные дни:", ', '.join(weekend_days))
    print("Ваши рабочие дни:", ', '.join(work_days))
z3()