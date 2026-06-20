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
    """
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

def isprime(n: int) -> bool:
    """
    Checks if n is prime
    :param n:
    :return:
    """
    return True if len(getfactorsof(n)) == 2 else False

def iseven(n: int) -> bool:
    """
    Checks if n is even
    :param n:
    :return:
    """
    return True if n % 2 == 0 else False

def gcd(a: int, b: int) -> int:
    """
    Returns the greatest common divisor of a and b.
    :param a:
    :param b:
    :return:
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Returns the least common multiple of a and b.
    :param a:
    :param b:
    :return:
    """
    return abs(a*b) // gcd(a, b)

def factorial(n: int) -> int:
    """
    Returns the factorial of a number.
    :param n:
    :return:
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
    :return:
    """
    sum_ = 0.0
    for num in nums:
        sum_+=num
    return sum_ / len(nums)

def median(nums: list[int | float]) -> int | float:
    """
    Returns the median of a list of numbers.
    :param nums:
    :return:
    """
    nums.sort()
    for i, num in enumerate(nums):
        if i == len(nums) // 2:
            return num
    raise AvergagingError("Median not found")

def max(a: int | float, b: int | float) -> int | float:
    """
    Returns the largest option
    :param a:
    :param b:
    :return:
    """
    return a if a > b else b

def min(a: int | float, b: int | float) -> int | float:
    """
    Returns the smallest option
    :param a:
    :param b:
    :return:
    """
    return a if a < b else b

def sqrt(num: int) -> float:
    """
    Returns the square root of num
    :param num:
    :return:
    """
    return num ** 0.5

def cbrt(num: int) -> int:
    """
    Returns the cube root of num
    :param num:
    :return:
    """
    return num ** (1/3)

def sum(a: int | float, b: int | float) -> int | float:
    """
    Returns the sum of two numbers
    :param a:
    :param b:
    :return:
    """
    return a + b

def mod(a: int | float, b: int | float) -> int | float:
    """
    Returns the remainder of two numbers
    :param a:
    :param b:
    :return:
    """
    return a % b

def square(a: int) -> int:
    """
    Returns the square of a
    :param a:
    :return:
    """
    return a ** 2

def cube(a: int) -> int:
    """
    Returns the cube of a
    :param a:
    :return:
    """
    return a ** 3
