from math import sqrt, ceil
def sieve_of_eratosthenes(n):
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]


def sieve_of_atkin(number):
    assert number > 0
    lng = ((number - 1) // 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((number - 1) / 4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(number - x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((number - 1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(number - x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4 - 8 * (1 - number))) / 4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= number: y_min = (((int(ceil(sqrt(x2 - number))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if number <= 3:
        return primes[:max(0, number - 2)]

    for n in range(5 >> 1, (int(sqrt(number)) + 1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, number, 2 * aux):
                sieve[k >> 1] = False

    s  = int(sqrt(number)) + 1
    if s  % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, number, 2) if sieve[i >> 1]])

    return primes


def sundaram(number):
    numbers = list(range(3, number + 1, 2))
    half = (number) // 2
    initial = 4

    for step in range(3, number + 1, 2):
        for i in range(initial, half, step):
            numbers[i-1] = 0
        initial += 2*(step+1)

        if initial > half:
            return [2] + list(filter(None, numbers))
