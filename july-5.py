def solution(s):
    if len(s) % 2 != 0:
        s = s + "_"
    return [s[i:i + 2] for i in range(0, len(s), 2)]


if __name__ == '__main__':
    solution("abcdef")

#  'Best Practice' Solution
# import re
#
# def solution(s):
#     return re.findall(".{2}", s + "_")
