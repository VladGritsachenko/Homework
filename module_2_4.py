numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in numbers:
    for k in range(2, i):
        is_prime = True
        if i % k == 0:
            is_prime = True
            primes.append(i)
            break
        else:
            is_prime = False
            not_primes.append(i)
            break

print(primes)
print(not_primes)