"""Question 2: Armstrong Number
Write a program to check if a number is an Armstrong number.
An Armstrong number is a number that is equal to the sum of cubes of its digits.
Example: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
"""

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    sum_of_powers = sum(int(digit) ** power for digit in digits)
    return sum_of_powers == num

if __name__ == "__main__":
    number = int(input("Enter a number: "))
    if is_armstrong(number):
        print(f"{number} is an Armstrong number")
    else:
        print(f"{number} is not an Armstrong number")
