def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

def factorial(num):
    if num <= 2:
        return num
    else:
        return num * factorial(num - 1)
    
res = factorial(3)

print(res)