# Напишите код, который запрашивает число и сообщает, является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def check_prime_number(num: int):
    tmp = True
    start_num = 2
    for i in range(start_num, num):
        if num % i == 0:
            tmp = False
    return tmp


def num_input(x):
    bottom_line = 0
    upper_bound = 100000
    while True:
        if bottom_line < x < upper_bound:
            if not check_prime_number(x):
                print('Число составное.')
                break
            else:
                print('Число простое.')
                break
        else:
            print('Число не входит в заданный интервал. Попробуйте снова.')
            x = int(input('\nВведите число для проверки (от 1 до 100000): '))


number = int(input('Введите число для проверки (от 1 до 100000): '))
num_input(number)
