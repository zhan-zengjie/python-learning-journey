# 计算倒数序列和
def sum_of_reciprocal_series(n):
    if not isinstance(n, int) or n <= 0:
        return None
    result = 0
    if n % 2 == 0:
        for num in range(2, n + 1, 2):
            result += 1 / num
        return result
    for num in range(1, n + 1, 2):
        result += 1 / num
    return result


print(sum_of_reciprocal_series(5))
print(sum_of_reciprocal_series(4))
print(sum_of_reciprocal_series(-1))
print(sum_of_reciprocal_series(4.0))