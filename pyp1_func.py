# 1. Функции
def greet_user(name):
    return f"Привет, {name}! Добро пожаловать в мир Python!"
def calculate_sum(a, b):
    return a+b
def functions_intro():
    name = input("Введите ваше имя: ")
    print(greet_user(name))
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    sum_of_ab = calculate_sum(a,b)
    answer = f"Сумма чисел: {sum_of_ab}"
    return answer

print(functions_intro())


# 2. Условия и ветвления
def age_message():
    age = int(input("Введите год вашего рождения: "))
    if 18 <= age <= 65:
        return "Отличный возраст для карьерного роста!"
    elif 18 >= age:
        return "Вы еще молоды, учеба — ваш путь!"
    else:
        return "Пора наслаждаться заслуженным отдыхом!"

print(age_message())

# # 3. Циклы
def number_sum():
    numbers = ""
    sum_of_numbers = []
    a = 1
    n = int(input("Введите число: "))
    while a < n+1:
        numbers = numbers + f"{a} "
        sum_of_numbers.append(a)
        a += 1
    print(f"Числа: {numbers}")
    return f"Сумма чисел: {sum(sum_of_numbers)}"

print(number_sum())

# 4. Расширенные функции
def triangle_check(a, b, c):


    if a > (b+c) or b > (a+c) or c > (b+a):
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
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /): ")
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        if b == 0:
            return "На 0 делить нельзя"
        return a / b
    else:
        return "Введены некорректные данные"
print(nested_functions())



# 6. Таблица умножения

def multiplication_table():
    size = int(input("Введите размере таблицы"))
    table = [[i*j for j in range(1, size+1)] for i in range(1, size+1)]
    for row in table:
        print(''.join(f'{num:4}' for num in row))
    pass

print(multiplication_table())


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