def compose(f, g):
    return lambda x: f(g(x))

f = compose(lambda x: x * x, lambda y: y + 1)

result = f(122)

print(result)