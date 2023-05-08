n = int(input())
def sum_digits(x):
    s = 0
    while x:
        s += x % 10
        x //= 10
    return s
sn = sum_digits(n)
primes = []
for num in range(2, n + sn + 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
for p in primes:
    if p > n:
        i = primes.index(p)
        break
print(primes[i+sn-1])