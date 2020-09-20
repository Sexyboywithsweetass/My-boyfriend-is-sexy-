import random

number = random.randint(0, 100)

while True:
    answer = input('Угадай число: ')
    if answer == "" or answer == "exit":
        print("Выход из программы")
        break

    if not answer.isdigit():
        print("Введи правильное число")
        continue

    answer = int(answer)

    if answer == number:
        print('Верно!')
        break

    elif answer < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
