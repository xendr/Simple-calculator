# Пример простого калькулятора на Python

def add(x, y):
    """Сложение двух чисел"""
    return x + y

def subtract(x, y):
    """Вычитание одного числа из другого"""
    return x - y

def multiply(x, y):
    """Умножение двух чисел"""
    return x * y

def divide(x, y):
    """Деление одного числа на другое"""
    if y == 0:
        raise ValueError("Деление на ноль невозможно!")
    return x / y

print("Выберите операцию:")
print("1. Сложение")
print("2. Вычитание")
print("3. Умножение")
print("4. Деление")

choice = input("Введите номер операции (1/2/3/4): ")

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

if choice == '1':
    print("Результат сложения:", add(num1, num2))
elif choice == '2':
    print("Результат вычитания:", subtract(num1, num2))
elif choice == '3':
    print("Результат умножения:", multiply(num1, num2))
elif choice == '4':
    try:
        print("Результат деления:", divide(num1, num2))
    except ValueError as e:
        print(e)
else:
    print("Некорректный ввод")
