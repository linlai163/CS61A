def sum_cubes_2(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def cube(x):
    return x * x * x

print(sum_cubes_2(10, cube))