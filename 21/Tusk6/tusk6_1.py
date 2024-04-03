def z1():
    a = {
        "Россия": "Москва",
        "США": "Вашингтон",
        "Китай": "Пекин",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Испания": "Мадрид",
        "Италия": "Рим"
    }

    # a)
    print("na) Пары ключ-значение:")
    for country, capital in a.items():
        print(f"{country} - {capital}")

    # b)
    b = "Россия"
    if b in a:
        print(f"nb) Столица страны {b} - {a[b]}")
    else:
        print(f"nb) Для страны {b} информация о столице отсутствует")

    # c)
    print("nc) Словарь в алфавитном порядке:")
    for country in sorted(a.keys()):
        print(f"{country} - {a[country]}")

def z2(word):
    a = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    score = 0
    for letter in word.upper():
        if letter in a:
            score += a[letter]

    return score

word = input("Введите слово: ")
result = z2(word)
print(f"Слово {word} имеет стоимость {result} очков.")
z2(word)



def z3():
    c = {
        'Даниил': {'английский', 'французский', 'немецкий'},
        'Алена': {'английский', 'испанский'},
        'Дима': {'китайский',  'арабский'},
        'Ксюша': {'русский', 'китайский'}
    }
    a = set()
    for languages in c.values():
        a.update(languages)
    d = sorted(a)
    print("Список всех языков, которые знают студенты:")
    print(d)

    cn = [student for student, languages in c.items() if 'китайский' in languages]
    print("Студенты, которые знают китайский язык:")
    print(cn)

z3()