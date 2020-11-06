# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input('Введите трехзначное число')
number = int(number)

a = number // 100
b = number % 100 // 10
c = number % 10

summ = a + b + c
comp = a * b * c

print(f'Сумма = {summ}')
print(f'Произведение = {comp}')
