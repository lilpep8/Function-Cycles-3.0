# 1. Функции
def greet_user(name):
    print(f"Привет, {name}! Добро пожаловать в мир Python!")
    return None


def calculate_sum(a: int, b: int):
    return a + b


def functions_intro():
    name = input("Введите ваше имя: ")
    print(greet_user(name))

    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))

    sum_of_ab = calculate_sum(a, b)
    answer = f"Сумма чисел: {sum_of_ab}"
    print(answer)
    return None


(functions_intro())


# 2. Условия и ветвления
def age_message():
    age = 2025 - int(input("Введите год вашего рождения: "))

    if 18 <= age <= 65:
        return "Отличный возраст для карьерного роста!"
    elif 18 >= age:
        return "Вы еще молоды, учеба — ваш путь!"
    else:
        return "Пора наслаждаться заслуженным отдыхом!"


print(age_message())

# # 3. Циклы
def number_sum():
    sum_of_numbers = []
    n = int(input("Введите число: "))

    for a in range(1, n + 1):
        sum_of_numbers.append(a)

    numbers = " ".join(str(num) for num in sum_of_numbers)
    print(f"Числа: {numbers}")
    return f"Сумма чисел: {sum(sum_of_numbers)}"


print(number_sum())

# 4. Расширенные функции


def triangle_check(a: int, b: int, c: int):
    if a >= (b + c) or b >= (a + c) or c >= (b + a):
        return "Нельзя построить треугольник"
    if a == b == c:
        return "Результат: Треугольник равносторонний"
    elif len({a, b, c}) == 2:
        return "Результат: Треугольник равнобедренный"
    else:
        return "Результат: Треугольник разносторонний"


a, b, c = (int(input("Введите длину первой стороны: ")),
           int(input("Введите длину второй стороны: ")),
           int(input("Введите длину третьей стороны: ")))

print(triangle_check(a, b, c))


# 5. Работа с вложенными функциями
def nested_functions():
    a = input("Введите первое число: ")
    if a == "exit":
        print("Вы вышли из калькулятора")
        return None

    b = input("Введите второе число: ")
    if b == "exit":
        print("Вы вышли из калькулятора")
        return None

    operation = input("Выберите операцию: (+, -, *, /) ")
    if operation == "exit":
        print("Вы вышли из калькулятора")
        return None

    def validity_check(a: str, b: str, operation: str):
        if not a.lstrip('-').isdigit() or not b.lstrip('-').isdigit():
            print("Введите корректные данные \nили введите 'exit', чтобы выйти ")
            return None
        if operation not in ('+', '-', '*', '/'):
            print("Выберите операцию из предложенных: (+, -, *, /) \nили введите 'exit', чтобы выйти")
            return None
        return [int(a), int(b)]

    def operate(numbers: list, operation: str):
        if operation == "+":
            return sum(numbers)
        elif operation == "-":
            return numbers[0] - numbers[1]
        elif operation == "*":
            return numbers[0] * numbers[1]
        elif operation == "/":
            if numbers[1] == 0:
                print("На 0 делить нельзя")
                return None
            return numbers[0] / numbers[1]

    numbers = validity_check(a, b, operation)
    if numbers is None:
        return nested_functions()

    result = operate(numbers, operation)
    if result is None:
        return nested_functions()

    return result


print(nested_functions())


# 6. Таблица умножения

def multiplication_table():
    size = int(input("Введите размер таблицы"))
    table = [[i * j for j in range(1, size + 1)] for i in range(1, size + 1)]
    for row in table:
        print(''.join(f'{num:4}' for num in row))


(multiplication_table())


# 7. Сортировка чисел

def bubble_sort():
    s = input("Введите числа через запятую: ")
    l = [item.strip() for item in s.split(',')]
    l_int = []
    for i in l:
        if i.isdigit():
            l_int.append(int(i))
    n = len(l_int)
    for i in range(n):
        for j in range(0, n - i - 1):
            if l_int[j] > l_int[j + 1]:
                l_int[j], l_int[j + 1] = l_int[j + 1], l_int[j]
    return l_int


print(bubble_sort())
