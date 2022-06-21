#  made use of the Python 3.10 "match/case" feature

def likes(names):
    match len(names):
        case 0:
            return "no one likes this"
        case 1:
            return str(' '.join([str(name) for name in names]) + " likes this")
        case 2:
            return str(' and '.join([str(name) for name in names]) + " like this")
        case 3:
            return str(', '.join(str(name) for name in names[:2]) + " and " + str(names[2]) + " like this")
        case _:
            return str(', '.join([str(name) for name in names[:2]]) + " and " + str(len(names)-2)
                       + " others like this")


if __name__ == '__main__':
    print(likes(["Bob", "Mary", "Steve"]))

#  'Best Practice' Solution as of June 20
#  def likes(names):
#      n = len(names)
#      return {
#          0: 'no one likes this',
#          1: '{} likes this',
#          2: '{} and {} like this',
#          3: '{}, {} and {} like this',
#          4: '{}, {} and {others} others like this'
#      }[min(4, n)].format(*names[:3], others=n-2)
