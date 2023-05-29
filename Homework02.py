# Задача 10. Монетки

import random
 
try:
    num_coins = int(input('Введите число монет: '))
    heads = 0 
    coins = [] 
    for i in range(num_coins):
        coins.append(random.randint(0, 1))
        
    print(f'Ваш результат: {coins}')     
    heads = sum(coins)
    print(heads)
    tails = num_coins - heads 
    
    if heads == 0 or heads == num_coins:
        print('Все монетки лежат одинаковой стороной вверх или монеток нет! Переворачивать ничего не требуется!')   
    elif heads == tails:
        print(f'Можно перевернуть любые монетки! Их выпало равное количество! Превернуть придется {heads}')
    elif heads < tails:
        print(f'Необходимо перевернуть монетки, которые лежат решкой вверх - {heads}')    
    else: print(f'Необходимо перевернуть монетки, которые лежат орлом вверх - {tails}')
        
except:
    print('Вы не книгу пишете, введите положительное число!')

# Задача 12. Сумма и произведение чисел

try:
    s = int(input('Введите сумму чисел: '))
    p = int(input('Введите произведение чисел: '))

    solution_exists = 0
    for i in range(s):
        if i * (s - i) == p:
            print(f'Петя загадал числа {i} и {s-i}')
            solution_exists = 1
            break
    if solution_exists == 0: 
        print('Таких натуральных чисел нет!') 

except:
    print('Некорректный ввод. Попробуйте еще раз!')



# Задача 14. Квадраты положительных чисел.
try:
    N = int(input('Введите число N: '))
    s = 1
    while s <= N:
        print(s)
        s *= 2
except:
    print('Некорректный ввод. Попробуйте еще раз!')    
