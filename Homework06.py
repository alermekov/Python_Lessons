# Задача 30

a1 = int(input("Введите первый элемент: "))
d = int(input("Введите разность: "))
n = int(input("Введите количество элементов: "))

progression = []
for i in range(n):
    progression.append(a1 + i * d)

print("Арифметическая прогрессия:", progression)

# Задача 32

min_value = int(input("Введите минимальное значение: "))
max_value = int(input("Введите максимальное значение: "))
array = list(range(10))
print(array)

for i in range(len(array)):
    if min_value <= array[i] <= max_value:
        print(i)
