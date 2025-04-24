# Задача 1: Оценка по шкале

def check_grade(score):
    if score >= 90:
        return f"Оценка за {score} баллов: Отлично"
    elif 89 >= score >= 75:
        return f"Оценка за {score} баллов: Хорошо"
    elif 74 >= score >= 50:
        return f"Оценка за {score} баллов: Удовлетворительно"
    else:
        return f"Оценка за {score} баллов: Неудовлетворительно"

print(check_grade(95))
print(check_grade(85))
print(check_grade(65))
print(check_grade(47))

# # Задача 2: Чётное или нечётное число

def is_even(number):
    if number == 0:
        return "Введите число отличное от 0."
    return f"Число {number} является чётным." if number % 2 == 0 \
        else f"Число {number} является нечётным."

print(is_even(0))
print(is_even(4))
print(is_even(7))

# Задача 3: Максимальное из двух чисел
def find_max(a, b):
    if a == b:
        return("Введите числа не равные друг другу")
    if a > b:
        return f"Максимальное из чисел {a} и {b}: {a}."
    else:
        return f"Максимальное из чисел {a} и {b}: {b}."

print(find_max(10, 20))
print(find_max(15, 9))
print(find_max(11, 11))


# Задача 4: Проверка числа на положительность и чётность
def check_number(number):
    if number > 0:
        if number % 2 == 0:
            return f"Число {number} положительное и чётное."
    elif number == 0:
        return "Это ноль"
    else:
        return f"Число {number} отрицательное."

print(check_number(8))
print(check_number(-5))
print(check_number(0))


# Задача 5: Проверка длины строки

def check_string_length(string, length):
    return f"Длина строки {string} достаточная" if len(string) >= length \
        else f"Строка {string} слишком короткая"

print(check_string_length("Python", 5))
print(check_string_length("Hi", 5))