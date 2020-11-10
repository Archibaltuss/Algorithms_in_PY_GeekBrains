# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

print('Введите натуральное число')
number = int(input('number: '))
result = 0

while number > 0:
    result = result * 10 + number % 10
    number = number // 10
else:
    print(f'{result}')