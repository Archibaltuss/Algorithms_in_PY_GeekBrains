import primes, sys

for n in [10**1, 10**2, 10**3, 10**4, 10**5]:
    print(f'Sieve of Atkin({n} elements) - {sys.getsizeof(primes.sieve_of_atkin(n))} b')
    print(f'Sieve of Eratosthenes({n} elements) - {sys.getsizeof(primes.sieve_of_eratosthenes(n))} b')
    print(f'Sieve of Sundaram({n} elements) - {sys.getsizeof(primes.sundaram(n))} b\n')


'''
Sieve of Atkin(10 elements) - 56 b
Sieve of Eratosthenes(10 elements) - 44 b
Sieve of Sundaram(10 elements) - 44 b

Sieve of Atkin(100 elements) - 164 b
Sieve of Eratosthenes(100 elements) - 128 b
Sieve of Sundaram(100 elements) - 128 b

Sieve of Atkin(1000 elements) - 808 b
Sieve of Eratosthenes(1000 elements) - 700 b
Sieve of Sundaram(1000 elements) - 700 b

Sieve of Atkin(10000 elements) - 5580 b
Sieve of Eratosthenes(10000 elements) - 4944 b
Sieve of Sundaram(10000 elements) - 4944 b

Sieve of Atkin(100000 elements) - 43216 b
Sieve of Eratosthenes(100000 elements) - 38396 b
Sieve of Sundaram(100000 elements) - 38396 b


Решето Эратосфена и Сундарама показали одинаковые значения по выделяемой памяти.
Но если брать в расчет 3е дз, то решето Эратосфена показало лучшие результаты по времени 
=>
Следовательно, самым лучшим решением при нахождении простых чисел будет: 
                                                                        <Решето Эратосфена>

Использовался Python 3.8.3 on win32
'''