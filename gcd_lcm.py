def gcd(a: int, b: int) -> int:
    a = abs(a); b = abs(b)
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a*b) // gcd(a,b)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(gcd(a,b), lcm(a,b))
