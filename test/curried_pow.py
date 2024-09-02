def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

print(curried_pow(3)(3))

def map_to_range(start, end, f):
    while start < end:
        print(f(start))
        start = start + 1
        
map_to_range(1,10, curried_pow(2))