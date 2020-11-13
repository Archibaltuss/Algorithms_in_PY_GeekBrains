# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

size = 10
min = 0
max = 100
array = [random.randint(min, max) for _ in range(size)]
print(array)

i = 0
index = -1
while i <len(array):
    if array[i] < 0 and index == -1:
        index = i
    elif 0 > array[i] > array[index]:
        index = i
    i += 1

if index != -1:
    print(f'Макс отрицательное число {array[index]} '
          f'находится в {index}')
