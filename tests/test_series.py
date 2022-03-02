from math_series.series import sum_series, fibonacci_lucas_iterate


def test_fibonacci():
    actual = sum_series(5)
    excepted = 5
    assert actual == excepted


def test_fibonacci():
    actual = sum_series(15)
    excepted = 610
    assert actual == excepted


def test_lucas():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected


def test_fib_iterate():
    actual = fibonacci_lucas_iterate(300, 0, 1)
    expected = 222232244629420445529739893461909967206666939096499764990979600
    assert actual == expected


def test_lucas_iterate():
    actual = fibonacci_lucas_iterate(5, 2, 1)
    expected = 11
    assert actual == expected
