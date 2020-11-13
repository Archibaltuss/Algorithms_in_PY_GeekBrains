# Определить, какое число в массиве встречается чаще всего.

import random

size = 10
min = 0
array = [random.randint(min, size // 1.5) for _ in range(size)]
print(array)

num = array[0]
frequency = 1
for i in range(len(array)):
    spam = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            spam += 1
        if spam > frequency:
            frequency = spam
            num = array[i]

print(f'Число {num} встречается {frequency} раз' if frequency > 1 else 'Все значения уникальны')
