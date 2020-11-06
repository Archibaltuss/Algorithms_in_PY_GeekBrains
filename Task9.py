# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
print('Введите три разных целых числа: ')
a = int(input('1-e: '))
b = int(input('1-e: '))
c = int(input('1-e: '))

if a > b > c and a > c:
    print('Среднее число:', b)
elif a > b and a > c > b:
    print('Среднее число:', c)
elif a > b and c < a:
    print('Среднее число:', a)
elif a > b > c and a > c:
    print('Среднее число:', a)
elif a > b > c and c < a:
    print('Среднее число:', c)
elif a > b and c > b:
    print('Среднее число:', b)
    
