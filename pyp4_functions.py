# Задача 1: Сумма чисел от 1 до N

def sum_numbers(n):
    num = 1
    for i in range(1,n+1):
        num += i
    return f"Сумма чисел от 1 до {n}: {num-1}"

print(sum_numbers(5))
print(sum_numbers(10))


# Задача 2: Поиск минимального числа в списке

def find_min(numbers):
    start = 0
    for i in numbers:
        if i < start:
            start = i
    return f"Минимальное число в списке {numbers}:  {start}"

print(find_min([3, 1, 4, 1, 5]))
print(find_min([2, 2, 3 ,1, -1, 21]))


# Задача 3: Подсчёт гласных в строке
def count_vowels(string):
    vowels = 0
    for i in string:
        if i in ["a", "e", "i", "o", "u"]:
            vowels += 1
    return f'Количество гласных в строке "{string}": {vowels}'

print(count_vowels("Hello World"))


### **Задача 4: Ромбовидный треугольник**
def print_diamond(rows):
    for i in range(1, rows + 1):
        print('* ' * i)
    for i in range(rows - 1, 0, -1):
        print('* ' * i)
print_diamond(4)

# Задача 5: Обратный отсчёт

def countdown():
    for i in range(11,1,-1):
        print(i-1)
    print("Старт!")
countdown()


# Задача 6: Обратный отсчёт - 2
def countdown():
    st  = 11
    while st != 1:
        st -= 1
        print(st)
    print("Старт!")
countdown()
