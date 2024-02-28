import random

def game():
    qwe = 0
    zxc = 0

    while zxc < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        asd = num1 + num2

        user_answer = input(f"{num1} + {num2} = ")

        if user_answer.isdigit() and int(user_answer) == asd:
            print("Правильно!")
            qwe += 1
        else:
            print("Ответ неверный")
            zxc += 1

    print(f"Игра окончена. Правильных ответов: {qwe}")

game()