def sum_cubes(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k * k * k, k + 1
    return total

print(sum_cubes(10))