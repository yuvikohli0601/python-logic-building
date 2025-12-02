def reverse_number(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev

if __name__ == "__main__":
    n = int(input("Enter n: "))
    print(reverse_number(n))
