def find_it(seq):
    for num in seq:  # loop through the seq array
        if seq.count(num) % 2 == 1:  # return the odd value
            return num


