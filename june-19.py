def spin_words(sentence):
    list = sentence.split()  # creates list of words from sentence param
    for idx, word in enumerate(list):
        if len(word) >= 5:
           list[idx] = word[::-1]  # reverses words only >= length of 5
    return ' '.join(list)  #  returns the list joined as a string

if __name__ == '__main__':
    print(spin_words("test sentence"))

#  'Best Practice' Solution as of June 19 2022
#
#  def spin_words(sentence):
#    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])