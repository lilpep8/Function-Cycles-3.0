# Задача 1: Вычисление площади прямоугольника
def rectangle_area(a, b):
    return f"Площадь прямоугольника с длиной {a} и шириной {b} равна {a*b}."


# Задача 2: Перевод времени из секунд в часы и минуты
def convert_seconds(seconds):
    if seconds % 3600 / 60 > 0:
        minutes = seconds % 3600 // 60 + 1
    else:
        minutes = seconds % 3600 // 60
    hours = seconds // 3600
    answer = (hours,minutes)
    print(f"В {seconds} секундах содержится {hours} час(ов) и {minutes} минут(ы).")

    return answer

print(convert_seconds(3672))
print(convert_seconds(3600))
print(convert_seconds(7254))

# Задача 3: Функция с аргументом по умолчанию
def power_of(number,exponent = 2):
    power_of_number = number ** exponent
    if exponent == 2:
        print(f"Квадрат числа {number} равен {power_of_number}.")
        return power_of_number
    else:
        print(f"Число {number} в степени {exponent} равно {power_of_number}.")
        return power_of_number

print(power_of(3, 4))
print(power_of(5))


# Задача 4: Подсчёт элементов
def count_items(*args):
    return len(args)

print(count_items(1, 2, 3, 4, 5))
print(count_items("apple", "banana", "cherry"))