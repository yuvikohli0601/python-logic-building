def sum_of_digits(n: int) -> int:
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

def product_of_digits(n: int) -> int:
    n = abs(n)
    if n == 0:
        return 0
    prod = 1
    while n > 0:
        prod *= (n % 10)
        n //= 10
    return prod

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(sum_of_digits(n))
    print(product_of_digits(n))
