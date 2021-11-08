# tyuta**

import random
import time

def check_letter(string1,ltt,string2):
    for i in range(len(string1)):
        if string1[i] == _letter:
            print(string1[i],string2[i])
            string2.replace(string2[i],_letter,i)

    return string2

_main_ls = [['always', 'be', 'yourself'],['beilive', 'in', 'yourself'],['never', 'say', 'never'],['dreams', 'comes', 'true'],['always', 'stay', 'strong'],['keep', 'it', 'cool'],['trust', 'in', 'yourself'],['whatever', 'you', 'like'],['the', 'rolling', 'stones'],['guns', 'and', 'roses']]
_choice = random.randint(0,9)
lst_words = _main_ls[_choice]
_currnt_ls = ["_" * len(i) for i in lst_words]
lst_words_str = ''.join(lst_words[0]) + ' ' + ''.join(lst_words[1]) + ' ' + ''.join(lst_words[2])
current_st = ''.join(_currnt_ls[0]) + ' ' + ''.join(_currnt_ls[1]) + ' ' + ''.join(_currnt_ls[2])
print(lst_words_str,current_st)
_letter = input("please guess letter")
print(check_letter(lst_words_str,_letter,current_st))

