print(" введи 'stop'.")

while True:
    word = input("Введите слово: ")
    if word.lower() == "stop":
        print("Выполнено")
        break
    else:
        print(" '{}'.задание сделано".format(word))