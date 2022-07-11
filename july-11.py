import math


def zeros(n):
    i = 1
    j = 0

    while n / (5 ** i) > 1: j += math.floor(n / (5 ** i)); i += 1
    return j


if __name__ == '__main__':
    print(zeros(6))

#  'Best Practice' Solution
#   def zeros(n):
#   x = n/5
#   return x+zeros(x) if x else 0
