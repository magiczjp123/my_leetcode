def power(a, n):
    ret = 1
    while n:
        if n % 2 == 1:
            ret = ret * a
        a = a * n
        n = n // 2

    return ret

power(10,2)