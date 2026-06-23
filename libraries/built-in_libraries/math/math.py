from exceptions import run_exceptions

# first 100 digits of pi
pi: float = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
"""
The ratio between the diameter and the circumference of a circle
"""
e: float = (1 + 1/1000000) ** 1000000
"""
(1 + 1/n)**n\n
As n -> infinity, the expression approaches e
"""

def getfactorsof(n: int) -> list[int]:
    """
    Returns the factors of n.
    :param n:
    :returns: list of factors
    """
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

def isprime(n: int) -> bool:
    """
    Checks if n is a prime number
    :param n:
    :return: if n is a prime number
    """
    return True if len(getfactorsof(n)) == 2 else False

def iseven(n: int) -> bool:
    """
    Checks if n is even
    :param n:
    :return: if n is even
    """
    return True if n % 2 == 0 else False

def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.
    :param a:
    :param b:
    :return: greatest common divisor
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Returns the lowest common multiple of a and b.
    :param a:
    :param b:
    :return: lowest common multiple
    """
    return abs(a*b) // gcd(a, b)

def factorial(n: int) -> int:
    """
    Returns the factorial of a number.
    :param n:
    :return: factorial of n
    """
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def pow(a: int, b: int, m=None):
    """
    Returns the  of a and optionally, gets the modulus without calculating the full exponent
    :param a:
    :param b:
    :param m:
    :return:
    """
    if m is None:
        return a ** b
    else:
        result = 1
        a = a % m

        while b > 0:
            if b % 2 == 1:
                result = (result * a) % m
            a = (a * a) % m
            b //= 2
        return result

def mean(nums: list[int | float]) -> float:
    """
    Returns the mean of a list of numbers.
    :param nums:
    :return: mean of nums
    """
    sum_ = 0.0
    for num in nums:
        sum_+=num
    return sum_ / len(nums)

def median(nums: list[int | float]) -> int | float:
    """
    Returns the median of a list of numbers.
    :param nums:
    :return: median of nums
    """
    nums.sort()
    for i, num in enumerate(nums):
        if i == len(nums) // 2:
            return num
    raise run_exceptions.AveragingError("Median not found")

def max(a: int | float, b: int | float) -> int | float:
    """
    Returns the largest option
    :param a:
    :param b:
    :return: largest number
    """
    return a if a > b else b

def min(a: int | float, b: int | float) -> int | float:
    """
    Returns the smallest option
    :param a:
    :param b:
    :return: smallest number
    """
    return a if a < b else b

def sqrt(n: int) -> float:
    """
    Returns the square root of a number
    :param n:
    :return: square root of n
    """
    return n ** 0.5

def cbrt(n: int) -> int:
    """
    Returns the cube root of a number
    :param n:
    :return: cube root of n
    """
    return n ** (1/3)

def sum(a: int | float, b: int | float) -> int | float:
    """
    Returns the sum of two numbers
    :param a:
    :param b:
    :return: sum of a and b
    """
    return a + b

def mod(a: int | float, b: int | float) -> int | float:
    """
    Returns the remainder of two numbers
    :param a:
    :param b:
    :return: mod of a and b
    """
    return a % b

def square(n: int) -> int:
    """
    Returns the square of a number
    :param n:
    :return: square of a
    """
    return n ** 2

def cube(n: int) -> int:
    """
    Returns the cube of a number
    :param n:
    :return: cube of a
    """
    return b ** 3
