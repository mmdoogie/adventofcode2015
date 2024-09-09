from functools import reduce
from operator import mul

def product(x):
    return reduce(mul, x)
