"""
2.  Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
        заданный случайными числами на промежутке [0; 50).
    Выведите на экран исходный и отсортированный массивы.

"""
import random

def merge_sort_optimized(data):
    input_data = data.copy()
    if len(data) < 20:
        return sorted(data)
    sorted_data = []
    mid = int(len(data) / 2)
    left = merge_sort_optimized(data[:mid])
    right = merge_sort_optimized(data[mid:])
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_data.append(right[j])
            j += 1
        else:
            sorted_data.append(left[i])
            i += 1
    sorted_data += left[i:]
    sorted_data += right[j:]
    return f'Merge Sort\n{input_data}\n->\n{sorted_data}'


print(merge_sort_optimized([random.uniform(0,49) for _ in range(25)]))