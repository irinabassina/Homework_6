# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. 
# не меньше заданного минимума и не больше заданного максимума)
# Пример:
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

def indexes(lst, min_v, max_v):
    lst1 = []
    for i in range (len(lst)):
        if min_v <= lst[i] <= max_v:
            lst1.append(i)
    return lst1

lst = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7]    
min_v = -1
max_v = 2
print(indexes(lst, min_v, max_v))


