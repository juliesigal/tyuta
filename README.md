# tyuta**

פונקציה שמקבלת מילה ומחזירה אותה חבויה:
 
 
import random
import time

_main_ls = [['always', 'be', 'yourself'],['beilive', 'in', 'yourself'],['never', 'say', 'never'],['dreams', 'comes', 'true'],['always', 'stay', 'strong'],['keep', 'it', 'cool'],['trust', 'in', 'yourself'],['whatever', 'you', 'like'],['the', 'rolling', 'stones'],['guns', 'and', 'roses']]
_choice = random.randint(0,9)
print(_choice)
lst_words = _main_ls[_choice]

def convert_sent(lst_words):
    _currnt_ls = []
    for i in lst_words: #[_choice]:
        temp = "_" * len(i)
        _currnt_ls.append(temp)
    return _currnt_ls #convert_word(_currnt_ls)
