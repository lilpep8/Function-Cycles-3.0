# Задача 1: Вычисление площади прямоугольника
def rectangle_area(a: int, b: int):
    area = a*b
    print(f"Площадь прямоугольника с длиной {a} и шириной {b} равна {area}.")
    return area


# Задача 2: Перевод времени из секунд в часы и минуты
def convert_seconds(seconds: int):

    def time_calculation(seconds: int) -> [int, int]:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60 if (seconds % 3600) % 60 == 0 \
            else (seconds % 3600) // 60 + 1
        return [hours, minutes]

    result = time_calculation(seconds)
    print(f"В {seconds} секундах содержится {result[0]} час(ов) и {result[1]} минут(ы).")
    return result

print(convert_seconds(3672))
print(convert_seconds(3600))
print(convert_seconds(7254))
print(convert_seconds(5555))
print(convert_seconds(0))
print(convert_seconds(1))


# Задача 3: Функция с аргументом по умолчанию
def power_of(number: int, exponent = 2):
    power_of_number = number ** exponent
    if exponent == 2:
        print(f"Квадрат числа {number} равен {power_of_number}.")
        return power_of_number
    else:
        print(f"Число {number} в степени {exponent} равно {power_of_number}.")
        return power_of_number

(power_of(3, 4))
(power_of(5))


# Задача 4: Подсчёт элементов
def count_items(*args):
    return len(args)

print(count_items(1, 2, 3, 4, 5))
print(count_items("apple", "banana", "cherry"))