# Задача 16

import random
n = int(input("Введите размер массива N: ")) 
x = int(input("Введите число X: "))
n_array = []

for i in range(n):
    n_array.append(random.randint(0, n//2))
    
count = 0
for i in n_array:
    if i == x:
        count += 1
    
print(
    f"Количество раз: {count}")

# Задача 18

n = int(input("Введите количество элементов в массиве: "))
list_1 = []
list_1.append(int(input("Введите элемент массива: ")))
k = int(input("Введите число, для которого нужно найти ближайший элемент: "))
min_diff = abs(list_1[0] - k)
closest_num = list_1[0]
for num in list_1:
    diff = abs(num - k)
    if diff < min_diff:
        min_diff = diff
        closest_num = num
print("Ближайшее число к", k, ":", closest_num)


# Задача 20

dictionary = {
'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1,
'd':2, 'g':2,
'b':3, 'c':3, 'm':3, 'p':3,
'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
'k':5,
'j':8, 'x':8,
'q':10, 'z':10,
'а':1, 'в':1, 'е':1, 'и':1, 'н':1, 'о':1, 'р':1, 'с':1, 'т':1,
'д':2, 'к':2, 'л':2, 'м':2, 'п':2, 'у':2,
'б':3, 'г':3, 'ё':3, 'ь':3, 'я':3,
'й':4, 'ы':4,
'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
'ш':8, 'э':8, 'ю':8,
'ф':10, 'щ':10, 'ъ':10
}

word = input('Введите слово -> ')
word = word.lower()

result = 0
for i in word:
    result += dictionary[i]

print('Количество очков за слово:', result)