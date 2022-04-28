# Fibonacci and Lucas functions using 1 argument and recursive method
from mimetypes import init


def lucas(n)-> int:
    """
        The Lucas Numbers are a related series of integers that start with the values 2 and 1, each number is the sum of the two previous numbers. The resulting series looks like this:
            # 2, 1, 3, 4, 7, 11, 18, 29, ...

        This function use the directly recursion method.

        Input:
            n: integer, n is the nth number in the series.
        Output:
            Return the nth value of Lucas Series.
    """

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n-1) + lucas(n-2)
def fibonacci(n) -> int:
    """
        The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two.The series looks like this:
            # 0, 1, 1, 2, 3, 5, 8, 13, ...

        This function use the directly recursion method.
        Input:
            n: integer, n is the nth number in the series.
        Output:
            Return the nth value of Fibonacci Series.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)


# Fibonacci and Lucas functions using 1 argument and iteration method
def fib_iterate(n) -> int:
    """

        The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two.The series looks like this:
            # 0, 1, 1, 2, 3, 5, 8, 13, ...

        This function use the iteration method.
        Input:
            n: integer, n is the nth number in the series.
        Output:
            Return the nth value of Fibonacci Series.

    """
    first = 0
    second = 1
    total = 0
    i = 1
    if n == 0:
        return first
    if n == 1:
        return second

    while True:
        if i == n:
            break
        total = first + second
        first = second
        second = total
        i += 1
    return total


def lucas_iterate(n) -> int:
    """
        The Lucas Numbers are a related series of integers that start with the values 2 and 1, each number is the sum of the two previous numbers. The resulting series looks like this:
            # 2, 1, 3, 4, 7, 11, 18, 29, ...

        This function use the iteration method.

        Input:
            n: integer, n is the nth number in the series.
        Output:
            Return the nth value of Lucas Series.
    """
    first = 2
    second = 1
    total = 0
    i = 1
    if n == 0:
        return first
    if n == 1:
        return second

    while True:
        if i == n:
            break
        total = first + second
        first = second
        second = total
        i += 1
    return total


# Fibonacci and Lucas functions using 1 required argument and 2 defult arguments with recursive method
def fibonacci_lucas(n, base_0, base_1) -> int:
    """
        This function is a dynamic function to generate any series based on the starting arguments, you can use it to generate series like Fibonacci or Lucas.

        This function use the directly recursion method.
        Input:
            n: integer number, n is the nth number in the series.
            base_0: integer number, base_0 is the first number of the series.
            base_1: integer number, base_1 is the second number of the series.
        Output:
            Return the nth value of the series.
    """
    if n == 0:
        return base_0
    if n == 1:
        return base_1

    return fibonacci_lucas(n-1, base_0, base_1) + fibonacci_lucas(n-2, base_0, base_1)


# Fibonacci and Lucas functions using 1 required argument and 2 defult arguments with iteration method
def fibonacci_lucas_iterate(n, base_0, base_1) -> int:
    """
        This function is a dynamic function to generate any series based on the starting arguments, you can use it to generate series like Fibonacci or Lucas.

        This function use the iteration method.
        Input:
            n: integer number, n is the nth number in the series.
            base_0: integer number, base_0 is the first number of the series.
            base_1: integer number, base_1 is the second number of the series.
        Output:
            Return the nth value of the series.
    """
    first = base_0
    second = base_1
    total = 0
    i = 1
    if n == 0:
        return first
    if n == 1:
        return second

    while True:
        if i == n:
            break
        total = first + second
        first = second
        second = total
        i += 1
    return total


def sum_series(n, def_1=0, def_2=1) -> int:
    return fibonacci_lucas(n, def_1, def_2)


print(sum_series(3))
