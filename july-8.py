def narcissistic(value):
    x = 0
    for n in str(value):
        x += (int(n) ** int(len(str(value))))
    return True if x == value else False


if __name__ == '__main__':
    print(narcissistic(371))

#  'Best Practice' Solution
#
#  def narcissistic(value):
#     return value == sum(int(x) ** len(str(value)) for x in str(value))
