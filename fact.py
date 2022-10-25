from functools import reduce


def fib(n: int) -> list:
    a = 0
    b = 1
    lst = [0, 1]
    while a + b <= n:
        c = b + a
        a = b
        b = c
        lst.append(c)
    return lst


def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def div(a, b):
    return a / b


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


def main():
    print(fib(1000))

    evens = list(filter(lambda a: a % 2 == 0, fib(1000)))

    doubles = list(map(lambda a: a * 2, fib(1000)))

    sum_1 = reduce(lambda a, b: a + b, fib(1000))

    print(evens)
    print(doubles)
    print(sum_1)


if __name__ == "__main__":
    main()
    div = smart_div(div)
    print(div(2, 4))

