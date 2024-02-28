while True:
    word = input("Введите слово (или 'stop', чтобы завершить): ")

    if word.lower() == "stop":
        print("Программа завершена.")
        break

    if "ф" in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")