from math import factorial

def is_perfect(n: int) -> bool:
    if n <= 1: return False
    s = 1
    i = 2
    while i*i <= n:
        if n % i == 0:
            s += i
            if i != n//i:
                s += n//i
        i += 1
    return s == n

def is_strong(n: int) -> bool:
    orig = n
    n = abs(n)
    total = 0
    while n:
        total += factorial(n % 10)
        n //= 10
    return total == orig

def is_harshad(n: int) -> bool:
    if n==0: return False
    s = sum(int(d) for d in str(abs(n)))
    return n % s == 0

if __name__ == "__main__":
    n = int(input())
    print(is_perfect(n), is_strong(n), is_harshad(n))
