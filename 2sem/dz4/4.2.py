from math import gcd
from sys import stdin
from functools import reduce

lst = list(map(int, stdin))
print(reduce(lambda x, y: gcd(x, y), lst))