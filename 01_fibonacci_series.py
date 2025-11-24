"""Question 1: Fibonacci Series
Write a program to print the Fibonacci series up to n terms.
Example: For n=10, output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    fibonacci(n)
