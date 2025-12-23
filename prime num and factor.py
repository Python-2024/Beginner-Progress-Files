a = int(input("Enter a number: "))

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_factors(n):
    factors = []
    for j in range(1, n + 1):
        if n % j == 0:
            factors.append(j)
    return factors

if is_prime(a):
    print("The input number is Prime")
else:
    print("The input number is Not prime")

factors = get_factors(a)
print("And its factors are:", factors)