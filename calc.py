try:
    a, b = map(float, input("Введите два числа через пробел: ").split())
except ValueError:
    print("Ошибка: нужно ввести два числа через пробел")
else:
    operation = input("Выберите операцию (+, -, *, /): ")

    if operation == "+":
        result = a + b
        print("Результат:", result)
    elif operation == "-":
        result = a - b
        print("Результат:", result)
    elif operation == "*":
        result = a * b
        print("Результат:", result)
    elif operation == "/":
        if b == 0:
            print("Ошибка: деление на ноль")
        else:
            result = a / b
            print("Результат:", result)
    else:
        print("Ошибка: неизвестная операция")