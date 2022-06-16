import math


def is_square(n):
    if n >= 0:  # if n is larger than or equal to 0, square root it and set it to 'sq'
        sq = math.sqrt(n)
    else:  # else return false
        return False
    if sq - int(sq) == 0:  # checks to see if the 'sq' value is a whole number
        return True
    return False


if __name__ == '__main__':
    print(is_square(10))

# 'Best Practice' Solutions (can't believe I forgot about the modulo!)
#
#  import math
#  def is_square(n):
#  return n > -1 and math.sqrt(n) % 1 == 0;
