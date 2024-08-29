def pi_sum_2(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total


def pi_term(x):
    return 8 / ((4*x-3) * (4*x-1))

print(pi_sum_2(1e6, pi_term))