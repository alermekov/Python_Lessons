# m = int(input("Введите количество минут "))
# s = int(input("Введите количество секунд "))
# print (m*60 + s, "секунд")

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('1, 8, 9'))