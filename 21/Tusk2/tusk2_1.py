n = int(input("Введите количество слов: "))
a = ""
for i in range(n):
    word = input("Введите слово: ")
    a += word + " "
print("Результат объединения слов:", a)