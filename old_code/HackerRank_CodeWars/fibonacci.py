def fib(n):
    if n < 0:
        return 0
    elif n == 0:
        return n
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_simple(n):
    # not fast with large numbers
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    for i in range(1, 20):
        print(fib_simple(i))
