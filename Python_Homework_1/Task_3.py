from random import randint

# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
# числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


def check_random(num):
    count = 9
    x = int(input('Введите число: '))
    while count > 0:
        if x > num:
            print('Загаданное число меньше')
            count -= 1
            x = int(input('Введите число: '))
        elif x < num:
            print('Загаданное число больше')
            count -= 1
            x = int(input('Введите число: '))
        else:
            print('Ура! Вы угадали!')
            break
    if count == 0:
        print('Закончились попытки. Загаданное число:', num)


number = randint(0, 1000)
check_random(number)
