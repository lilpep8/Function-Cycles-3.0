# Задача 1: Оценка по шкале
def check_grade(score: int):
    if score >= 90:
        print(f"Оценка за {score} баллов: Отлично")
        return score
    elif 89 >= score >= 75:
        print(f"Оценка за {score} баллов: Хорошо")
        return score
    elif 74 >= score >= 50:
        print(f"Оценка за {score} баллов: Удовлетворительно")
        return score
    else:
        print(f"Оценка за {score} баллов: Неудовлетворительно")
        return score

(check_grade(95))
(check_grade(85))
(check_grade(65))
(check_grade(47))


# # Задача 2: Чётное или нечётное число
def is_even(number: int):
    if number == 0:
        print("Введите число отличное от 0.")
        return number

    if number % 2 == 0:
        print(f"Число {number} является чётным")
        return number
    else:
        print(f"Число {number} является нечётным.")
        return number

(is_even(0))
(is_even(4))
(is_even(7))


# Задача 3: Максимальное из двух чисел
def find_max(a: int, b: int):
    if a == b:
        print("Введите числа не равные друг другу")
        return None
    if a > b:
        print(f"Максимальное из чисел {a} и {b}: {a}.")
        return a
    else:
        print(f"Максимальное из чисел {a} и {b}: {b}.")
        return b

(find_max(10, 20))
(find_max(15, 9))
(find_max(11, 11))


# Задача 4: Проверка числа на положительность и чётность
def check_number(number: int):
    if number > 0:
        if number % 2 == 0:
            print(f"Число {number} положительное и чётное.")
            return number
        else:
            print(f"Число {number} положительное и нечётное.")
            return number
    elif number == 0:
        print("Это ноль")
        return number
    else:
        print(f"Число {number} отрицательное.")
        return number

(check_number(8))
(check_number(-5))
(check_number(0))
(check_number(5))


# Задача 5: Проверка длины строки
def check_string_length(string: str, length: int):
    if length > 0 and len(string) > 0:
        if len(string) >= length:
            print(f"Длина строки {string} достаточная")
            return length
        else:
            print(f"Строка {string} слишком короткая")
            return length
    print("Длина строки должна быть больше 0 и строка должна быть заполнена")
    return length

(check_string_length("Python", 5))
(check_string_length("Hi", 5))