a, b = map(float, input("Введите два числа через пробел: ").split())

operation = input("Выберите операцию (+, -, *, /): ")

if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    if b == 0:
        print("Ошибка: деление на ноль")
    else:
        result = a / b
        print("Результат:", result)
else:
    print("Неизвестная операция")

if operation in ["+", "-", "*"] or (operation == "/" and b != 0):
    print("Результат:", result)