from statistics import median
import random

def get_median(arr: list):
    return f'Input data: {arr}\nMedian: {median(arr)}'

print(get_median([random.randint(-100,100) for _ in range(25)]))