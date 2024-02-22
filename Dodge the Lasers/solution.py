from decimal import *

def S(a, n):
    if n == 0:
        return 0
    np = int((a - 1) * n)
    return n * np + n * (n + 1) / 2 - np * (np + 1) / 2 - S(a, np)


def solution(s):
    getcontext().prec = 101
    return str(S(Decimal(2).sqrt(), int(s)))