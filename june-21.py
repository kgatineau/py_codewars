def tribonacci(signature, n):
    i = 2
    if n <= 3:
        return signature[:n]

    while i < n - 1:
        signature.append((signature[i - 2]) + (signature[i - 1]) + signature[i])
        i += 1
    return signature


if __name__ == '__main__':
    print(tribonacci([1, 2, 3], 4))

#  'Best Practice' June 21/22 - still learning how to work with Python arrays
#
#  def tribonacci(signature, n):
#    res = signature[:n]
#    for i in range(n - 3): res.append(sum(res[-3:]))
#    return res