import random
import time

def convert_sent(input_lst):
    _currnt_ls = ["_" * len(i) for i in input_lst]
    return _currnt_ls

def check_letter(a):
    current1 = []
    for i in lst_words:
        str2 = ''
        for j in i:
            if j == _letter:
                str2 = str2 + j
            else:
                str2 = str2 + '_'
        current1.append(str2)
    return current1




_main_ls = [['always', 'be', 'yourself'],['beilive', 'in', 'yourself'],['never', 'say', 'never'],['dreams', 'comes', 'true'],['always', 'stay', 'strong'],['keep', 'it', 'cool'],['trust', 'in', 'yourself'],['whatever', 'you', 'like'],['the', 'rolling', 'stones'],['guns', 'and', 'roses']]
_choice = random.randint(0,9)
print(_choice, _main_ls[_choice])
_currnt_ls = []
lst_words = _main_ls[_choice]


print(convert_sent(lst_words))

_letter = input("please guess letter")

print(check_letter(_letter))
