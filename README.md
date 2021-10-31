# tyuta**

import random
import time

def convert_sent(input_lst):
    for i in input_lst:
        temp = "_" * len(i)
        _currnt_ls.append(temp)
    return _currnt_ls


_main_ls = [['always', 'be', 'yourself'],['beilive', 'in', 'yourself'],['never', 'say', 'never'],['dreams', 'comes', 'true'],['always', 'stay', 'strong'],['keep', 'it', 'cool'],['trust', 'in', 'yourself'],['whatever', 'you', 'like'],['the', 'rolling', 'stones'],['guns', 'and', 'roses']]
_choice = random.randint(0,9)
print(_choice)
_currnt_ls = []
lst_words = _main_ls[_choice]

print(convert_sent(lst_words))
_letter = input("please guess letter")

 def check_letter(_letter):
     for i in lst_words:
         if _letter == i:
