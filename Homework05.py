# Задача 26

def power(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b/2) * power(a, b/2)
    else:
        return a * power(a, b-1)

a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

result = power(a, b)
print(f"{a} в степени {b} равно {result}")

# Задача 28

def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a ^ b, (a & b) << 1)

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

result = sum(a, b)
print(f"Сумма чисел {a} и {b} равна {result}")

