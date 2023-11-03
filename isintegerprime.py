def is_prime(num):
    return num > 1 and all(num % i for i in range(2, int(num ** .5 + 1)))
print(is_prime(0), False, "0  is not prime")
print(is_prime(1), False, "1  is not prime")
print(is_prime(2), True, "2  is prime")
print(is_prime(73), True, "73 is prime")
print(is_prime(75), False, "75 is not prime")
print(is_prime(-1), False, "-1 is not prime")