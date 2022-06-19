def find_it(seq):
    for num in seq:  # loop through the seq array
        if seq.count(num) % 2 == 1:  # return the odd value
            return num


if __name__ == '__main__':
    print(find_it([1, 1, 1, 2, 2, 4, 4, 10, 10]))
