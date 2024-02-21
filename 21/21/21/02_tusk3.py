def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"Год {year} - високосный")
    else:
        print("Этот год не високосный")
год=int(input("Введите год:"))
is_leap_year(год)