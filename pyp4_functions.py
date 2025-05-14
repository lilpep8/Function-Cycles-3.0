# Задача 1: Сумма чисел от 1 до N
def sum_numbers(n: int):
    if n <= 0:
        print("n должно быть положительным")
        return n

    numbers = []
    for i in range(0, n + 1):
        numbers.append(i)

    sum_of_numbers = sum(numbers)
    print(f"Сумма чисел от 1 до {n}: {sum_of_numbers}")
    return sum_of_numbers

print(sum_numbers(5))
print(sum_numbers(10))
print(sum_numbers(0))
print(sum_numbers(-5))


# Задача 2: Поиск минимального числа в списке
def find_min(numbers: list) -> int:
    if not numbers:
        raise ValueError("Список не должен быть пустым")

    min_number = numbers[0]
    for i in numbers:
        if i < min_number:
            min_number = i

    print(f"Минимальное число в списке {numbers}: {min_number}")
    return min_number

print(find_min([3, 1, 4, 1, 5]))
print(find_min([2, 2, 3 ,1, -1, 21]))
print(find_min([2, 2, 3 ,1, 0, 21]))


# Задача 3: Подсчёт гласных в строке
def count_vowels(string: str) -> int:
    vowels = 0
    lower_string = string.lower()
    for i in lower_string:
        if i in ["a", "e", "i", "o", "u"]:
            vowels += 1

    print(f'Количество гласных в строке "{string}": {vowels}')
    return vowels

print(count_vowels("Hello World"))


### **Задача 4: Ромбовидный треугольник**
def print_diamond(rows: int) -> None:
    for i in range(1, rows + 1):
        print('* ' * i)

    for i in range(rows - 1, 0, -1):
        print('* ' * i)


print_diamond(4)


# Задача 5: Обратный отсчёт
def countdown() -> None:
    for i in range(11,1,-1):
        print(i-1)
    print("Старт!")

countdown()


# Задача 6: Обратный отсчёт - 2
def countdown() -> None:
    st  = 11
    while st != 1:
        st -= 1
        print(st)
    print("Старт!")

countdown()
