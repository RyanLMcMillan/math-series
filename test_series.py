from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_input_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_input_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_input_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_input_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_input_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_input_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_input_6():
    actual = fibonacci(6)
    expected = 8
    assert actual == expected

def test_fibonacci_input_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected




def test_lucas_input_1():
    actual = lucas(1)
    expected = 2
    assert actual == expected

def test_lucas_input_2():
    actual = lucas(2)
    expected = 1
    assert actual == expected


def test_lucas_input_3():
    actual = lucas(3)
    expected = 3
    assert actual == expected


def test_lucas_input_4():
    actual = lucas(4)
    expected = 4
    assert actual == expected


def test_lucas_input_5():
    actual = lucas(5)
    expected = 7
    assert actual == expected


def test_lucas_input_6():
    actual = lucas(6)
    expected = 11
    assert actual == expected

def test_lucas_input_7():
    actual = lucas(7)
    expected = 18
    assert actual == expected

def test_lucas_input_8():
    actual = lucas(8)
    expected = 29
    assert actual == expected



def test_sum_series_1():
    actual = sum_series(1)
    expected = 0
    assert actual == expected

def test_sum_series_2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected

def test_sum_series_3():
    actual = sum_series(3)
    expected = 1
    assert actual == expected
