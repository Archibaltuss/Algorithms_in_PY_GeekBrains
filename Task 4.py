# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сколько элементов сложить: '))
item = 1
sum = 0
for _ in range(n):
    sum += item
    item /= -2
print(sum)