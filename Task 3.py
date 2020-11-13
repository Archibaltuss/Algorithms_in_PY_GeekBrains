# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

n = 10
min = 0
max = 100
array = [random.randint(min, max) for _ in range(n)]
print(array)

ind_min = 0
ind_max = 0
for i in range(len(array)):
    if array[i] < array[ind_min]:
        ind_min = 1
    elif array[i] > array[ind_max]:
        ind_max = 1

array[ind_min], array[ind_max] = array[ind_max], array[ind_min]
print(array)
