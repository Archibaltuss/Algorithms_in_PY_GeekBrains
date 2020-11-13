# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
start = 2
end = 99
start_div = 2
end_div = 9

for i in range(start_div, end_div + 1):
    frequency = 0
    for i in range(start, end + 1):
        if j % i == 0:
            frequency += 1
    print(f'Числу {i} кратно {frequency} чисел')