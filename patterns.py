def pyramid(n: int):
    for i in range(1, n+1):
        print("*" * i)

def inverted_pyramid(n: int):
    for i in range(n, 0, -1):
        print("*" * i)

def centered_pyramid(n: int):
    for i in range(1, n + 1):
        print(" "*(n-i) + "*"*(2*i-1))

if __name__ == "__main__":
    n = int(input("Rows: "))
    pyramid(n)
    inverted_pyramid(n)
    centered_pyramid(n)
