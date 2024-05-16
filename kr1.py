def incr(x):
    if x <= 0:
        return 0
    if x % 2 != 0:
        return x - 2
    else:
        return x - 3


def sum_func(a, b):
    res = 1 / (a + b)
    print(f"a = {a} ; b = {b} ; result = {res}")
    return res


def row(func, inc, a, b):
    if 4 >= a + b > 0:
        return func(a, b)
    elif a + b <= 0:
        return 0
    else:
        return func(a, b) + row(func, inc, inc(inc(a)), inc(a))


def funk_town(a, b):
    a, b = min(a, b), max(a, b)
    return row(sum_func, incr, a, b)


print(funk_town(9, 11))