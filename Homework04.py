# Задача 22

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))

set1 = set()
set2 = set()

print("Введите элементы первого множества:")
for i in range(n):
    element = int(input())
    set1.add(element)

print("Введите элементы второго множества:")
for i in range(m):
    element = int(input())
    set2.add(element)

intersection = sorted(set1.intersection(set2))

print("Числа, которые встречаются в обоих множествах:")
for element in intersection:
    print(element)
    

# Задача 24
   
N = int(input("Введите количество кустов: "))

berries = list(map(int, input("Введите урожайность каждого куста черники через пробел: ").split()))

max_berries = 0

for i in range(N):
    curr_berries = berries[i] + berries[(i+1)%N] + berries[(i+2)%N]
    if curr_berries > max_berries:
        max_berries = curr_berries

print("Максимальное число ягод, которое может собрать собирающий модуль, равно", max_berries)