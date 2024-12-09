numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = [2]
not_primes = []
for i in numbers:
    if i == 1:
        continue
    for k in range(2, i):
        if i % k == 0:
            not_primes.append(i)
            break
        if not i in not_primes:
            primes.append(i)
            break

print(primes)
print(not_primes)