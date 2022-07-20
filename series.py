def fibonacci(n):
    if n <= 1:
        return n
    #return n * fibonacci(n - 1)
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, num1=0, num2=1):
    if n == 1:
        return num1
    elif n == 2:
        return num2
    else:
        return sum_series(n-1, num1, num2) + sum_series(n-2, num1, num2)