# 分解质因数
def prime_factorization(n):
    if n == 1:
        print(1)
        return

    i = 2

    while i**2 <= n:
        if n % i == 0:
            print(i, end="*")
            n //= i
        else:
            i += 1

    if n > 1:
        print(n)


prime_factorization(90)
